from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from app.db.session import Base  # Importa el Base de SQLAlchemy donde declaras tus modelos
from app.core.config import settings  # Asegúrate de que este archivo importa tu Settings

# Esto es el objeto de configuración de Alembic
config = context.config

# Interpretar el archivo de configuración para Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Define la metadata de tus modelos para autogenerar migraciones
# Asegúrate de que Base tiene el metadata de tus modelos
target_metadata = Base.metadata

# Carga la URL de la base de datos desde tu archivo de configuración (config.py)
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# Definir si ejecutar migraciones en modo offline u online
def run_migrations_offline() -> None:
    """Ejecuta las migraciones en 'modo offline'.

    Esto configura el contexto solo con una URL, sin un Engine.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecuta las migraciones en 'modo online'.

    En este escenario, se necesita crear un Engine y asociar una conexión.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
