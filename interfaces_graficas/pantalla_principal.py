import tkinter as tk
from utilidades.configuracion import *
from interfaces_graficas.clientes import *
from interfaces_graficas.clientes import *
from interfaces_graficas.productos import *
from interfaces_graficas.remitos import *


def pantalla_principal():
    ventana_principal = tk.Tk()
    ventana_principal.configure(bg=color_primario)
    ventana_principal.resizable(False, True)
    ventana_principal.title("Menu principal")
    ventana_principal.state("zoomed")

    # CONFIGURACION DEL GRID DE LA VENTANA
    ventana_principal.grid_rowconfigure(0, weight=0)  # Barra: tamaño fijo
    ventana_principal.grid_rowconfigure(1, weight=1)  # Contenido: se expande
    ventana_principal.grid_columnconfigure(0, weight=1)  # Todo el ancho


    # BARRA SUPERIOR
    frame_opciones_top = tk.Frame(ventana_principal)
    frame_opciones_top.configure(bg=color_secundario, height=60)
    frame_opciones_top.grid_propagate(False)
    frame_opciones_top.grid(row=0, column=0, sticky="ew")


    # BOTONES
    boton_productos = tk.Button(frame_opciones_top, text="PRODUCTOS")
    boton_productos.configure(bg=color_primario, fg=color_secundario, command=productos)
    boton_productos.grid(row=0, column=1, padx=20, pady=15)

    boton_clientes = tk.Button(frame_opciones_top, text="CLIENTES")
    boton_clientes.configure(bg=color_primario, fg=color_secundario, command=clientes)
    boton_clientes.grid(row=0, column=2, padx=20, pady=15)

    boton_remitos = tk.Button(frame_opciones_top, text="REMITOS")
    boton_remitos.configure(bg=color_primario, fg=color_secundario, command=remitos)
    boton_remitos.grid(row=0, column=3, padx=20, pady=15)


    # LABEL VALOR DOLAR
    label_dolar = tk.Label(frame_opciones_top, text="Dolar: ")
    label_dolar.configure(bg=color_primario, fg=color_secundario)
    label_dolar.grid(row=0, column=4, padx=20, pady=15)

    label_valor_dolar = tk.Label(frame_opciones_top)


    ventana_principal.mainloop()


if __name__ == "__main__":
    pantalla_principal()