from typing import Optional, List
from models import Producto
from database import Database
from fastapi import HTTPException
from sqlite3 import Error

class ProductoCRUD:
    def __init__(self, database: Database):
        self.database = database

    def agregar_producto(self, producto: Producto):
        try:
            with self.database.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO productos (nombre, descripcion, precio, cantidad) VALUES (?, ?, ?, ?)",
                               (producto.nombre, producto.descripcion, producto.precio, producto.cantidad))
                conn.commit()
                producto.id = cursor.lastrowid
                return producto
        except Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def actualizar_producto(self, producto_id: int, producto: Producto):
        try:
            with self.database.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE productos SET nombre = ?, descripcion = ?, precio = ?, cantidad = ? WHERE id = ?",
                               (producto.nombre, producto.descripcion, producto.precio, producto.cantidad, producto_id))
                if cursor.rowcount == 0:
                    raise HTTPException(status_code=404, detail="Producto no encontrado")
                conn.commit()
                return producto
        except Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def listar_productos(self, nombre: Optional[str] = None, precio: Optional[float] = None, cantidad: Optional[int] = None) -> List[Producto]:
        try:
            with self.database.get_connection() as conn:
                cursor = conn.cursor()
                query = "SELECT * FROM productos WHERE 1=1"
                params = []

                if nombre:
                    query += " AND nombre LIKE ?"
                    params.append(f"%{nombre}%")
                if precio is not None:
                    query += " AND precio = ?"
                    params.append(precio)
                if cantidad is not None:
                    query += " AND cantidad = ?"
                    params.append(cantidad)

                cursor.execute(query, params)
                rows = cursor.fetchall()
                return [Producto(id=row[0], nombre=row[1], descripcion=row[2], precio=row[3], cantidad=row[4]) for row in rows]
        except Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def eliminar_producto(self, producto_id: int):
        try:
            with self.database.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
                if cursor.rowcount == 0:
                    raise HTTPException(status_code=404, detail="Producto no encontrado")
                conn.commit()
                return {"message": "Producto eliminado"}
        except Error as e:
            raise HTTPException(status_code=500, detail=str(e))