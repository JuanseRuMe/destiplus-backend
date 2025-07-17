# Importamos la función create_engine desde SQLAlchemy, la cual se usa para crear la conexión al motor de la base de datos.
from sqlalchemy import create_engine

# Importamos sessionmaker, que es una fábrica para crear nuevas sesiones de conexión a la base de datos.
from sqlalchemy.orm import sessionmaker

# Importamos declarative_base, que es una clase base para crear modelos de SQLAlchemy.
from sqlalchemy.ext.declarative import declarative_base

# Importamos la configuración desde otro módulo en el proyecto para obtener los valores de configuración, como la URL de la base de datos.
from ..core.config import settings

# Se obtiene la URL de la base de datos utilizando la propiedad get_database_url del archivo de configuración.
DATABASE_URL = settings.get_database_url

# Se intenta crear un motor de conexión a la base de datos usando la URL proporcionada.
try:
    engine = create_engine(DATABASE_URL)
except Exception as e:
    # Si ocurre un error al intentar crear el motor, se imprime un mensaje de error.
    print(f"Error creating engine: {e}")

# Se crea una fábrica de sesiones usando sessionmaker. La sesión no realiza commits automáticos ni vacía automáticamente el buffer (autocommit=False, autoflush=False).
# Se enlaza esta fábrica de sesiones con el motor de la base de datos (bind=engine).
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Se define una clase base para los modelos declarativos de SQLAlchemy.
Base = declarative_base()

# Se define una función get_db que provee una sesión de la base de datos.
def get_db():
    # Se crea una nueva sesión de la base de datos.
    db = SessionLocal()
    try:
        # Se utiliza yield para generar la sesión que puede ser usada en otras partes del código.
        yield db
    finally:
        # Una vez que el código que usa la sesión ha terminado, se cierra la conexión.
        db.close()
