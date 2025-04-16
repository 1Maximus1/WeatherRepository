# # The session factory should be created after Base
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.config import Config

# Connection settings (must match alembic.ini)
SQLALCHEMY_DATABASE_URL = Config.get_config_postgres()

# Important: we create the engine first
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a single Base instance for the entire project
Base = declarative_base()


def get_db_url():
    alembic_db = os.getenv("ALEMBIC_DB", "postgres")
    if alembic_db == "mysql":
        return Config.get_config_mysql()
    else:
        return Config.get_config_postgres()


def get_db_engine(db_type="postgres"):
    """Создает engine в зависимости от типа БД"""
    if db_type == "mysql":
        db_url = Config.get_config_mysql()
    else:
        db_url = Config.get_config_postgres()

    return create_engine(
        db_url,
        pool_pre_ping=True,
        pool_recycle=3600,
        connect_args={"connect_timeout": 30},
    )


def get_session_factory(engine):
    """Создает фабрику сессий для указанного engine"""
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


# SQLALCHEMY_DATABASE_URL = get_db_url()

# print(SQLALCHEMY_DATABASE_URL)

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
