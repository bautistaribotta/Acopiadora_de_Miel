import tkinter as tk
from tkinter import ttk
from utilidades.configuracion import *


def proveedores():
    ventana_proveedores = tk.Toplevel()
    ventana_proveedores.title("Proveedores")
    ventana_proveedores.geometry("800x600+550+85")
    ventana_proveedores.resizable(False, False)
    ventana_proveedores.configure(bg=color_principal)


    # CONFIGURACION DEL GRID DE LA VENTANA
    ventana_proveedores.grid_rowconfigure(0, weight=0)  # Buscador y Botones
    ventana_proveedores.grid_rowconfigure(1, weight=1)  # Contenido principal
    ventana_proveedores.grid_columnconfigure(0, weight=1)


    # FRAME SUPERIOR - BUSCADOR Y BOTONES
    frame_superior = tk.Frame(ventana_proveedores, bg=color_principal)
    frame_superior.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))


    # BUSCADOR A LA IZQUIERDA
    label_busqueda = tk.Label(frame_superior, text="Buscar:", font=fuente1, bg=color_principal, fg=color_secundario)
    label_busqueda.pack(side="left", padx=(0, 10))
    barra_busqueda = tk.Entry(frame_superior, bg=color_secundario, fg=color_principal, font=fuente1, width=25)
    barra_busqueda.pack(side="left")


    # BOTONES A LA DERECHA
    boton_eliminar = tk.Button(frame_superior, bg=color_secundario, fg=color_principal, text="Eliminar", width=10,
                               font=fuente1)
    boton_eliminar.pack(side="right", padx=(5, 0))

    boton_editar = tk.Button(frame_superior, bg=color_secundario, fg=color_principal, text="Editar", width=10,
                             font=fuente1)
    boton_editar.pack(side="right", padx=5)

    boton_agregar = tk.Button(frame_superior, bg=color_secundario, fg=color_principal, text="Añadir", width=10,
                              font=fuente1)
    boton_agregar.pack(side="right", padx=5)


    # FRAME TABLA
    frame_tabla = tk.Frame(ventana_proveedores, bg=color_principal)
    frame_tabla.grid(row=1, column=0, sticky="nsew", padx=20, pady=(10, 20))


    # SCROLL BARRA
    barra_scroll = ttk.Scrollbar(frame_tabla)
    barra_scroll.pack(side="right", fill="y")


    # TREEVIEW (TABLA)
    columnas = ("id", "nombre", "localidad")
    tabla_productos = ttk.Treeview(frame_tabla, columns=columnas, show="headings", yscrollcommand=barra_scroll.set, height=20)


    # CONFIGURAR COLUMNAS
    tabla_productos.heading("id", text="ID")
    tabla_productos.heading("nombre", text="Nombre")
    tabla_productos.heading("localidad", text="Localidad")

    tabla_productos.column("id", width=100, anchor="center")
    tabla_productos.column("nombre", width=300, anchor="w")
    tabla_productos.column("localidad", width=200, anchor="w")

    tabla_productos.pack(side="left", fill="both", expand=True)
    barra_scroll.config(command=tabla_productos.yview)


if __name__ == "__main__":
    # ESTO ES SOLO A MODO DE PRUEBA, PARA NO ABRIR TODO EL TIEMPO LA PANTALLA PRINCIPAL
    root = tk.Tk()  # Crea una ventana principal oculta
    # root.withdraw()  # La oculta (porque no la necesito visible)
    proveedores()  # Abre la ventana Toplevel de proveedores
    root.mainloop()  # Mantiene la aplicación corriendo