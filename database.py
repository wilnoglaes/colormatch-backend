import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Render leerá la URL desde las variables de entorno
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    # Si no está en la nube, usa la URL local (para pruebas)
    SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:6dUhZgWJmzwIPxll@db.muozbpinozmanitvdjlv.supabase.co:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
