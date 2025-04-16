import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context
from models.AirQuality import AirQuality
from models.CelestialEvents import CelestialEvents
from models.Location import Location
from models.Precipitation import Precipitation
from models.Temperature import Temperature
from models.TemperatureFeels import TemperatureFeels
from models.Weather import Weather
from models.Wind import Wind

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Base
from infrastructure.postgres.base.base import Base

target_metadata = Base.metadata
print("Tables loaded in metadata:")
print(Base.metadata.tables.keys())
# Настройка логгирования
config = context.config
fileConfig(config.config_file_name)

db_type = context.get_x_argument(as_dictionary=True).get("db", "postgres")

# Set the environment variable so other parts of the app can access it
os.environ["ALEMBIC_DB"] = db_type

# Update the SQLAlchemy URL in the config
if db_type == "mysql":
    from config.config import Config

    config.set_main_option("sqlalchemy.url", Config.get_config_mysql())
else:
    from config.config import Config

    config.set_main_option("sqlalchemy.url", Config.get_config_postgres())


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()

    # Initialize data only for upgrade commands
    if "upgrade" in sys.argv:
        from data.weather.db_init import initialize_data
        from infrastructure.postgres.base.base import get_db_engine, get_session_factory

        engine = get_db_engine(db_type)
        SessionLocal = get_session_factory(engine)
        initialize_data(SessionLocal)


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
