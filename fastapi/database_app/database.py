from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import psycopg2


# SQLALCHEMY_DATABASE_URL = "sqlite:///./database_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@0.tcp.in.ngrok.io:17528/postgres"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()