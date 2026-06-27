# Rodrichs API

Sistema de API REST desarrollado con Django REST Framework para la gestión de inventario y ventas de la empresa Rodrichs.

Este proyecto permite administrar productos, controlar el stock, gestionar compras y ventas, así como el registro de clientes y proveedores. La API está diseñada para ser consumida por una aplicación frontend en Next.js.

## 🚀 Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- PostgreSQL (o MySQL según configuración)
- JWT Authentication
- Cookies HttpOnly

## 📌 Características

- Autenticación segura con JWT
- Gestión de usuarios y roles
- CRUD de productos
- Control de inventario
- Registro de ventas y compras
- Gestión de clientes y proveedores
- API REST estructurada y escalable

## ⚙️ Instalación

```bash
git clone <url-del-repo>
cd rodrichs-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Crea un archivo `.env`:
- DJANGO_ENV= development o DJANGO_ENV= production
Luego `.env.development` o `.env.production` basado en `.env.example`
python manage.py migrate
python manage.py runserver