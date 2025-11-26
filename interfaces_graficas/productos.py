import tkinter as tk
from utilidades.configuracion import *

def productos():
    ventana_productos = tk.Toplevel()
    ventana_productos.title("Productos")
    ventana_productos.minsize(450, 600)
    ventana_productos.resizable(False, False)

    # GEOMETRIA Y POSICION
    ventana_productos.grid()

if __name__ == "__main__":
    productos()