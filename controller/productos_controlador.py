from model.entidades import Producto
from model.productos_db import listar_producto_db
from tkinter import messagebox


def listar_productos_controlador():
    return listar_producto_db()