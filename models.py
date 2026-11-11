from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Color(Base):
    __tablename__ = "colores"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, index=True)
    nombre = Column(String)
    categoria = Column(String)
    hex = Column(String)
    lab_l = Column(Float)
    lab_a = Column(Float)
    lab_b = Column(Float)

class Formula(Base):
    __tablename__ = "formulas"
    id = Column(Integer, primary_key=True, index=True)
    color_id = Column(Integer, ForeignKey("colores.id"))
    pigmento_nombre = Column(String)
    ml_por_litro = Column(Float)