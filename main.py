from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="ColorMatch API", description="API para el catálogo de colores Contractor")

# --- CONFIGURACIÓN DE CORS (Permite que React se conecte) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para obtener la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la API de ColorMatch"}

# Endpoint para obtener todos los colores
@app.get("/colores/", response_model=List[schemas.ColorBase])
def obtener_colores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    colores = db.query(models.Color).offset(skip).limit(limit).all()
    return colores