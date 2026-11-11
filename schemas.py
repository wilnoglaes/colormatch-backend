from pydantic import BaseModel
from typing import List

class FormulaBase(BaseModel):
    pigmento_nombre: str
    ml_por_litro: float

class ColorBase(BaseModel):
    codigo: str
    nombre: str
    categoria: str
    hex: str
    lab_l: float
    lab_a: float
    lab_b: float

class ColorResponse(ColorBase):
    id: int
    formulas: List[FormulaBase] = []

    class Config:
        from_attributes = True