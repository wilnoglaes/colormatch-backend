from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Tu contraseña ya está configurada aquí
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:6dUhZgWJmzwIPxll@db.muozbpinozmanitvdjlv.supabase.co:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()