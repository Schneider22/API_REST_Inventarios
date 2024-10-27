from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    id: Optional[int] = None
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    cantidad: int