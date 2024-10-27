from fastapi import APIRouter, Depends
from typing import List, Optional
from crud import ProductoCRUD
from models import Producto
from database import Database

router = APIRouter()
database = Database()
producto_crud = ProductoCRUD(database)

@router.post("/productos/", response_model=Producto)
def crear_producto(producto: Producto):
    return producto_crud.agregar_producto(producto)

@router.put("/productos/{producto_id}", response_model=Producto)
def actualizar_producto(producto_id: int, producto: Producto):
    return producto_crud.actualizar_producto(producto_id, producto)

@router.get("/productos/", response_model=List[Producto])
def obtener_productos(nombre: Optional[str] = None, precio: Optional[float] = None, cantidad: Optional[int] = None):
    return producto_crud.listar_productos(nombre, precio, cantidad)

@router.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int):
    return producto_crud.eliminar_producto(producto_id)