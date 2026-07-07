from rest_framework import serializers


class ModeloBaseSerializer(serializers.ModelSerializer):
    """
    Serializer base con utilidades reutilizables.
    """

    # ==========================
    # LIMPIEZA
    # ==========================

    def normalizar_string(self, value: str) -> str:
        return value.strip()

    def normalizar_upper(self, value: str) -> str:
        return value.strip().upper()

    def normalizar_lower(self, value: str) -> str:
        return value.strip().lower()

    # ==========================
    # VALIDACIONES
    # ==========================

    def validar_unico_sin_distincion_de_mayusculas_y_minusculas(
        self,
        model,
        field_name,
        value,
    ):
        queryset = model.all_objects.filter(
            **{f"{field_name}__iexact": value}
        )

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                {
                    field_name:
                    f"Ya existe un registro con ese {field_name}."
                }
            )

    def validar_longitud_celular(
        self,
        pais,
        numero_celular,
    ):
        """
        Valida la longitud del celular según el país.
        """

        if not numero_celular:
            return

        if len(numero_celular) != pais.longitud_celular:

            raise serializers.ValidationError(
                {
                    "numero_celular":
                    f"Debe tener {pais.longitud_celular} dígitos."
                }
            )

    def validar_numero_documento(
        self,
        tipo_documento,
        numero_documento,
    ):
        """
        Valida longitud y tipo del documento.
        """

        if len(numero_documento) != tipo_documento.longitud:

            raise serializers.ValidationError(
                {
                    "numero_documento":
                    f"Debe tener {tipo_documento.longitud} caracteres."
                }
            )

        match tipo_documento.tipo:

            case tipo_documento.Tipo.NUMERICO:

                if not numero_documento.isdigit():

                    raise serializers.ValidationError(
                        {
                            "numero_documento":
                            "Solo debe contener números."
                        }
                    )

            case tipo_documento.Tipo.ALFABETICO:

                if not numero_documento.isalpha():

                    raise serializers.ValidationError(
                        {
                            "numero_documento":
                            "Solo debe contener letras."
                        }
                    )

            case tipo_documento.Tipo.ALFANUMERICO:

                if not numero_documento.isalnum():

                    raise serializers.ValidationError(
                        {
                            "numero_documento":
                            "Solo debe contener letras y números."
                        }
                    )
    # ==========================
    # OBTENER VALORES
    # ==========================

    def obtener_valor(self, attrs, campo):
        if campo in attrs:
            return attrs[campo]

        if self.instance:
            return getattr(self.instance, campo)

        return None