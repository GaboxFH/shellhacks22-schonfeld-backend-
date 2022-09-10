from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# postgresql://admin@name:password@name.postgres.database.azure.com:5432/postgres
SQLALCHEMY_DATABASE_URL = "postgresql://securiquery:sh3llHacks@securiquery.postgres.database.azure.com:5432/postgres"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
