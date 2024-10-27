#### API REST de Inventario de Productos ####

Este proyecto implementa una API REST en Python para gestionar un inventario de productos. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una base de datos SQLite. Utiliza FastAPI como framework para construir la API y gestionar los endpoints, y SQLite para la persistencia de datos.


## Requisitos

- Python 3.10 o superior
- Flask
- FastAPI
- Uvicorn
- SQLite3

## Instalación
1. **Clona el repositorio** en tu máquina:
   	```bash
   	git clone https://github.com/tu-usuario/tu-repo.git cd tu-repo
2. Crea un entorno virtual y activa:
    	python -m venv .venv
	.\.venv\Scripts\activate
3. Instala las dependencias:
    	pip install -r requirements.txt

## Ejecución
Ejecuta la aplicación:
    	uvicorn main:app --reload

La API estará disponible en `http://localhost:8000/productos/`.

## Endpoints

la documentación interactiva para pruebas estará disponible en:

http://localhost:8000/docs

ó

http://localhost:8000/redoc

## Ejemplos de Uso:

#1. Crear Productos.

{
  "id": 1,
  "nombre": "Huevo AAA",
  "descripcion": "Huevo Rojo",
  "precio": 18000,
  "cantidad": 40
},
{
  "id": 2,
  "nombre": "Huevo AA",
  "descripcion": "Huevo",
  "precio": 15000,
  "cantidad": 20
},
{
  "id": 3,
  "nombre": "Huevo A",
  "descripcion": "Huevo",
  "precio": 13000,
  "cantidad": 30
},
{
  "id": 4,
  "nombre": "Huevo B",
  "descripcion": "Huevo",
  "precio": 12000,
  "cantidad": 20
},
{
  "id": 5,
  "nombre": "Huevo C",
  "descripcion": "Huevo",
  "precio": 10000,
  "cantidad": 30
}

#2. Actualizar Productos.


  "id": 3,
{
  "id": 3,
  "nombre": "Huevo A",
  "descripcion": "Huevo",
  "precio": 14000,
  "cantidad": 12
},

  "id": 4,
{
  "id": 4,
  "nombre": "Huevo B",
  "descripcion": "Huevo",
  "precio": 11000,
  "cantidad": 40
},

#3. Buscar Productos.

 Búsqueda por Nombre: "AA"

 Búsqueda por Preci0: "18000"

 Búsqueda por Cantidad: "12"

#4. Eliminar Productos.

 Eliminar: "id": 2

 Eliminar: "id": 4# API_REST_Inventarios
