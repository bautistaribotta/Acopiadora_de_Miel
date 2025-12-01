import tkinter as tk
from utilidades.configuracion import *


def remitos():
    ventana_remitos = tk.Toplevel()
    ventana_remitos.title("Remitos")
    ventana_remitos.resizable(False, False)
    ventana_remitos.config(bg=color_primario)
    centrar_ventana(ventana_remitos, 400, 600)

    # GEOMETRIA Y POSICION
    ventana_remitos.grid()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    remitos()
    root.mainloop()