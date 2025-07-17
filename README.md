Backend TREE SUESCA

Descripción
API REST construida con FastAPI, PostgreSQL y Docker.
Tecnologías

FastAPI
PostgreSQL
Docker
SQLAlchemy
Alembic

Configuración Local
Prerequisitos

Python 3.9+
Docker y Docker Compose
Git

Pasos de Instalación

Clonar el repositorio

bashCopygit clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO

Crear archivo .env

bashCopycp .env.example .env
# Editar .env con tus configuraciones

Ejecutar con Docker

bashCopydocker-compose up --build

La API estará disponible en http://localhost:8000
Documentación en http://localhost:8000/docs

Estructura del Proyecto
📁 app/
├── 📁 api/
├── 📁 core/
├── 📁 db/
└── 📁 models/
Despliegue
El proyecto está configurado para despliegue automático en Railway.
Contribuir

Fork el proyecto
Crea tu rama de características
Commit tus cambios
Push a la rama
Abre un Pull Request