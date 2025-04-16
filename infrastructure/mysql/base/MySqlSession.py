from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config.config import Config

# Connection settings (must match alembic.ini)
SQLALCHEMY_DATABASE_URL = Config.get_config_mysql()

# Important: we create the engine first
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a single Base instance for the entire project
Base = declarative_base()

# The session factory should be created after Base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
