from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from apps.auditoria.models import Auditoria
from apps.core.utils.auditoria import registrar_auditoria
from apps.usuarios.serializers.auth import LoginSerializer
from apps.usuarios.services.auth import (
    generate_tokens_for_user,
    refresh_access_token,
    blacklist_refresh_token,
)

from rest_framework.permissions import IsAuthenticated

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)

        except serializers.ValidationError:

            registrar_auditoria(
                accion=Auditoria.Accion.LOGIN_FAILED,
                request=request,
                metadata={
                    "username": request.data.get("username"),
                    "motivo": "Credenciales inválidas"
                }
            )

            raise

        user = serializer.validated_data["user"]

        registrar_auditoria(
            accion=Auditoria.Accion.LOGIN,
            request=request,
            usuario=user,
        )

        tokens = generate_tokens_for_user(user)

        response = Response(
            {"message": "Login exitoso"},
            status=status.HTTP_200_OK
        )

        response.set_cookie(
            key="access_token",
            value=tokens["access"],
            httponly=True,
            secure=False,  # producción → True
            samesite="Lax"
        )

        response.set_cookie(
            key="refresh_token",
            value=tokens["refresh"],
            httponly=True,
            secure=False,  # producción → True
            samesite="Lax"
        )

        return response

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
        })

class RefreshView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        refresh_token = request.COOKIES.get(
            "refresh_token"
        )

        if not refresh_token:
            return Response(
                {
                    "detail": "Refresh token no encontrado."
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        tokens = refresh_access_token(
            refresh_token
        )

        response = Response(
            {
                "message": "Token renovado"
            }
        )

        response.set_cookie(
            key="access_token",
            value=tokens["access"],
            httponly=True,
            secure=False,
            samesite="Lax",
        )

        response.set_cookie(
            key="refresh_token",
            value=tokens["refresh"],
            httponly=True,
            secure=False,
            samesite="Lax",
        )

        return response
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.COOKIES.get(
            "refresh_token"
        )

        registrar_auditoria(
            accion=Auditoria.Accion.LOGOUT,
            request=request,
            usuario=request.user,
        )

        if refresh_token:
            blacklist_refresh_token(
                refresh_token
            )

        response = Response(
            {
                "message": "Logout exitoso"
            }
        )

        response.delete_cookie(
            "access_token"
        )

        response.delete_cookie(
            "refresh_token"
        )

        return response
