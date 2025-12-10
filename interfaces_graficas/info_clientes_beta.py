from tkinter import ttk
from utilidades.configuracion import *


def informacion_cliente():
    ventana_info_cliente = tk.Toplevel(root)
    ventana_info_cliente.title("Informacion del cliente")
    ventana_info_cliente.configure(bg=color_primario)

    # Dimensiones y centrado
    ancho_ventana = 900
    alto_ventana = 600
    centrar_ventana(ventana_info_cliente, ancho_ventana, alto_ventana)


    # --- FRAME SUPERIOR (Datos y Valores) ---
    frame_superior = tk.Frame(ventana_info_cliente, bg=color_primario)
    frame_superior.pack(side="top", fill="x", expand=False, padx=20, pady=5)


    # --- SUB-FRAME DATOS DEL CLIENTE (Izquierda) ---
    frame_datos = tk.Frame(frame_superior, bg=color_primario)
    frame_datos.pack(side="left", fill="both", expand=True)


    # ID
    label_id_titulo = tk.Label(frame_datos, text="ID:", bg=color_primario, fg="white", font=("Arial", 10, "bold"))
    label_id_titulo.grid(row=0, column=0, sticky="w", pady=1, padx=(10, 5))
    label_id_valor = tk.Label(frame_datos, text="---", bg=color_primario, fg="white", font=("Arial", 10))
    label_id_valor.grid(row=0, column=1, sticky="w", pady=1, padx=(0, 30))


    # TELEFONO
    label_telefono_titulo = tk.Label(frame_datos, text="Telefono:", bg=color_primario, fg="white",
                                     font=("Arial", 10, "bold"))
    label_telefono_titulo.grid(row=0, column=2, sticky="w", pady=1, padx=(10, 5))
    label_telefono_valor = tk.Label(frame_datos, text="---", bg=color_primario, fg="white", font=("Arial", 10))
    label_telefono_valor.grid(row=0, column=3, sticky="w", pady=1, padx=(0, 30))


    # NOMBRE
    label_nombre_titulo = tk.Label(frame_datos, text="Nombre:", bg=color_primario, fg="white",
                                   font=("Arial", 10, "bold"))
    label_nombre_titulo.grid(row=1, column=0, sticky="w", pady=1, padx=(10, 5))
    label_nombre_valor = tk.Label(frame_datos, text="---", bg=color_primario, fg="white", font=("Arial", 10))
    label_nombre_valor.grid(row=1, column=1, sticky="w", pady=1, padx=(0, 30))


    # APELLIDO
    label_apellido_titulo = tk.Label(frame_datos, text="Apellido:", bg=color_primario, fg="white",
                                     font=("Arial", 10, "bold"))
    label_apellido_titulo.grid(row=1, column=2, sticky="w", pady=1, padx=(10, 5))
    label_apellido_valor = tk.Label(frame_datos, text="---", bg=color_primario, fg="white", font=("Arial", 10))
    label_apellido_valor.grid(row=1, column=3, sticky="w", pady=1, padx=(0, 30))


    # LOCALIDAD
    label_localidad_titulo = tk.Label(frame_datos, text="Localidad:", bg=color_primario, fg="white",
                                      font=("Arial", 10, "bold"))
    label_localidad_titulo.grid(row=2, column=0, sticky="w", pady=1, padx=(10, 5))
    label_localidad_valor = tk.Label(frame_datos, text="---", bg=color_primario, fg="white", font=("Arial", 10))
    label_localidad_valor.grid(row=2, column=1, sticky="w", pady=1, padx=(0, 30))


    # CALLE
    label_calle_titulo = tk.Label(frame_datos, text="Calle:", bg=color_primario, fg="white", font=("Arial", 10, "bold"))
    label_calle_titulo.grid(row=2, column=2, sticky="w", pady=1, padx=(10, 5))
    label_calle_valor = tk.Label(frame_datos, text="---", bg=color_primario, fg="white", font=("Arial", 10))
    label_calle_valor.grid(row=2, column=3, sticky="w", pady=1, padx=(0, 30))


    # FACTURA
    label_factura_titulo = tk.Label(frame_datos, text="Factura (Si/No):", bg=color_primario, fg="white",
                                    font=("Arial", 10, "bold"))
    label_factura_titulo.grid(row=3, column=0, sticky="w", pady=1, padx=(10, 5))
    label_factura_valor = tk.Label(frame_datos, text="---", bg=color_primario, fg="white", font=("Arial", 10))
    label_factura_valor.grid(row=3, column=1, sticky="w", pady=1, padx=(0, 30))


    # CUIT
    label_cuit_titulo = tk.Label(frame_datos, text="CUIT:", bg=color_primario, fg="white", font=("Arial", 10, "bold"))
    label_cuit_titulo.grid(row=3, column=2, sticky="w", pady=1, padx=(10, 5))
    label_cuit_valor = tk.Label(frame_datos, text="---", bg=color_primario, fg="white", font=("Arial", 10))
    label_cuit_valor.grid(row=3, column=3, sticky="w", pady=1, padx=(0, 30))


    # Configurar columnas para que ocupen espacio
    frame_datos.grid_columnconfigure(1, weight=1)
    frame_datos.grid_columnconfigure(3, weight=1)


    # --- SUB-FRAME DERECHO (Valores y Botones) ---
    frame_derecho = tk.Frame(frame_superior, bg=color_primario)
    frame_derecho.pack(side="right", fill="y", padx=(20, 0))


    # SUB-FRAME PARA VALORES
    frame_valores = tk.Frame(frame_derecho, bg=color_primario)
    frame_valores.pack(side="top", pady=(0, 10))


    # VALOR KILO DE MIEL
    frame_kilo_miel = tk.Frame(frame_valores, bg=color_primario)
    frame_kilo_miel.pack(side="left", padx=10)

    label_kilo_miel = tk.Label(frame_kilo_miel, text="Kilo de Miel", bg=color_primario, fg="white",
                               font=("Arial", 10, "bold"))
    label_kilo_miel.pack()

    label_valor_kilo_miel = tk.Label(frame_kilo_miel, text="---", bg="white", fg="black", font=("Arial", 11, "bold"),
                                     width=10, relief="sunken")
    label_valor_kilo_miel.pack(pady=2)


    # VALOR DOLAR
    frame_valor_dolar = tk.Frame(frame_valores, bg=color_primario)
    frame_valor_dolar.pack(side="left", padx=10)
    valor_dolar_actual = get_cotizacion_oficial_venta()

    label_valor_dolar = tk.Label(frame_valor_dolar, text="Valor Dolar")
    label_valor_dolar.config(bg=color_primario, fg="white", font=("Arial", 10, "bold"))
    label_valor_dolar.pack()

    label_valor_dolar_numero = tk.Label(frame_valor_dolar, text=f"${valor_dolar_actual}")
    label_valor_dolar_numero.config(bg="white", fg="black", font=("Arial", 11, "bold"), width=10, relief="sunken")
    label_valor_dolar_numero.pack(pady=2)


    # PESOS ARGENTINOS
    frame_pesos_argentinos = tk.Frame(frame_valores, bg=color_primario)
    frame_pesos_argentinos.pack(side="left", padx=10)

    label_pesos_argentinos = tk.Label(frame_pesos_argentinos, text="Pesos Argentinos", bg=color_primario, fg="white",
                                      font=("Arial", 10, "bold"))
    label_pesos_argentinos.pack()

    label_valor_pesos_argentinos = tk.Label(frame_pesos_argentinos, text="---", bg="white", fg="black",
                                            font=("Arial", 11, "bold"), width=10, relief="sunken")
    label_valor_pesos_argentinos.pack(pady=2)


    # SUB-FRAME PARA BOTONES
    frame_botones = tk.Frame(frame_derecho, bg=color_primario)
    frame_botones.pack(side="top", fill="x", pady=5)


    # BOTON NUEVA
    frame_boton_nueva = tk.Frame(frame_botones, bg=color_primario)
    frame_boton_nueva.pack(side="left", padx=10, expand=True, fill="x")

    boton_nueva = tk.Button(frame_boton_nueva, text="Nueva", font=("Arial", 10, "bold"), bg="white", fg="black",
                            cursor="hand2")
    boton_nueva.pack(fill="x")


    # BOTON EDITAR
    frame_boton_editar = tk.Frame(frame_botones, bg=color_primario)
    frame_boton_editar.pack(side="left", padx=10, expand=True, fill="x")

    boton_editar = tk.Button(frame_boton_editar, text="Editar", font=("Arial", 10, "bold"), bg="white", fg="black",
                             cursor="hand2")
    boton_editar.pack(fill="x")


    # BOTON ELIMINAR
    frame_boton_eliminar = tk.Frame(frame_botones, bg=color_primario)
    frame_boton_eliminar.pack(side="left", padx=10, expand=True, fill="x")

    boton_eliminar = tk.Button(frame_boton_eliminar, text="Eliminar", font=("Arial", 10, "bold"), bg="white",
                               fg="black", cursor="hand2")
    boton_eliminar.pack(fill="x")


    # --- FRAME MEDIO (Tabla Debe/Haber) ---
    frame_medio = tk.Frame(ventana_info_cliente, bg=color_secundario)
    frame_medio.pack(side="top", fill="both", expand=True, padx=20, pady=(10, 30))


    # TREEVIEW
    columnas = ("fecha", "detalle", "debe", "haber", "saldo")
    tabla_transacciones = ttk.Treeview(frame_medio, columns=columnas, show="headings")


    # ESTILO PARA EL TREEVIEW
    estilo = ttk.Style()
    estilo.configure("Treeview", font=("Arial", 10), rowheight=22)
    estilo.configure("Treeview.Heading", font=("Arial", 11, "bold"))

    tabla_transacciones.heading("fecha", text="Fecha")
    tabla_transacciones.heading("detalle", text="Detalle")
    tabla_transacciones.heading("debe", text="Debe")
    tabla_transacciones.heading("haber", text="Haber")
    tabla_transacciones.heading("saldo", text="Saldo")

    tabla_transacciones.column("fecha", width=100, anchor="center")
    tabla_transacciones.column("detalle", width=350, anchor="w")
    tabla_transacciones.column("debe", width=100, anchor="e")
    tabla_transacciones.column("haber", width=100, anchor="e")
    tabla_transacciones.column("saldo", width=100, anchor="e")

    scrollbar = ttk.Scrollbar(frame_medio, orient="vertical", command=tabla_transacciones.yview)
    tabla_transacciones.configure(yscroll=scrollbar.set)

    tabla_transacciones.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    ventana_info_cliente.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    informacion_cliente()
    root.mainloop()