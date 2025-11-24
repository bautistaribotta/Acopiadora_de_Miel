import tkinter as tk
from main import color_principal, color_secundario, color_terciario


def pantalla_principal():
    ventana_principal = tk.Tk()
    ventana_principal.configure(bg=color_principal)
    ventana_principal.state("zoomed")
    ventana_principal.title("Menu principal")

    opciones_top = tk.Frame(ventana_principal)
    opciones_top.configure(bg=color_secundario)
    opciones_top.pack()

    ventana_principal.mainloop()

#pantalla_principal()