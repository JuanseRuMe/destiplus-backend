# Este código define una clase `Settings` que gestiona la configuración de la aplicación utilizando
# las variables de entorno definidas en un archivo `.env`. La configuración incluye detalles 
# sobre la base de datos PostgreSQL, el nombre del proyecto y el modo de depuración.
# También proporciona una propiedad para obtener y modificar la URL de la base de datos si 
# utiliza un esquema "postgres://" (común en entornos heredados), cambiándolo a "postgresql://".

from pydantic_settings import BaseSettings
from typing import Optional

# Definición de la clase Settings que hereda de BaseSettings para manejar las configuraciones.
class Settings(BaseSettings):
    # Cadena de conexión de la base de datos PostgreSQL.
    DATABASE_URL: str
    # Nombre de usuario de la base de datos PostgreSQL.
    POSTGRES_USER: str
    # Contraseña del usuario de la base de datos PostgreSQL.
    POSTGRES_PASSWORD: str
    # Nombre de la base de datos PostgreSQL.
    POSTGRES_DB: str
    # Variable booleana que indica si la aplicación está en modo depuración. Por defecto es False.
    DEBUG: bool = False
    # Nombre del proyecto, por defecto se define como "API_test".
    PROJECT_NAME: str = "API_test"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Turismo Local API"
    
    # Definición de una propiedad para obtener la URL de la base de datos.
    @property
    def get_database_url(self) -> str:
        # Asigna la URL de la base de datos a la variable 'url'.
        url = self.DATABASE_URL
        # Si la URL empieza con 'postgres://', la reemplaza con 'postgresql://'.
        if url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql://", 1)
        # Devuelve la URL modificada o sin cambios.
        return url
    
    # Configuración adicional para la clase Settings.
    class Config:
        # Indica que las variables de entorno se cargarán desde un archivo llamado ".env".
        env_file = ".env"
        # Define que las variables de entorno son sensibles a mayúsculas y minúsculas.
        case_sensitive = True
        # Permite campos adicionales que no estén definidos explícitamente en la clase.
        extra = "allow"

# Instancia un objeto de la clase Settings para acceder a las configuraciones.
settings = Settings()
