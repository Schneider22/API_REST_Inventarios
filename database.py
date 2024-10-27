import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_name="Inventarios.db"):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT,
                    precio REAL NOT NULL,
                    cantidad INTEGER NOT NULL
                )
                """)
                conn.commit()
        except Error as e:
            print(f"Error al crear la tabla: {e}")

    def get_connection(self):
        return sqlite3.connect(self.db_name)
