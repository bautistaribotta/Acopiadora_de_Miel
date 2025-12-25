import tkinter as tk
import requests
from tkinter import messagebox


def validar_solo_letras(texto_nuevo):
    # 1. Permito borrar y dejar el texto vacio
    if texto_nuevo == "":
        return True

    # 2. Reviso cada caracter
    for char in texto_nuevo:
        # Si el caracter NO es letra Y NO es espacio: ERROR
        if not (char.isalpha() or char.isspace()):
            messagebox.showwarning("Caracter inválido", "Solo se permiten letras")
            return False
    return True


def validar_solo_numeros_punto(texto_nuevo):
    if texto_nuevo == "":
        return True
    # Pregunto si cuando le quito el punto al texto quedan solo numeros y luego cuento la cantidad de "."
    if texto_nuevo.replace(".", "", 1).isdigit() and texto_nuevo.count(".") <= 1:
        return True
    else:
        messagebox.showwarning("Caracter inválido", "Solo se permiten números y un punto decimal.")
        return False


def validar_solo_numeros(texto_nuevo):
    # 1. Permito borrar y dejar el texto vacio
    if texto_nuevo == "":
        return True

    # 2. Reviso cada caracter
    for char in texto_nuevo:
        # Si el caracter NO es letra Y NO es espacio: ERROR
        if not (char.isdigit() or char.isspace()):
            messagebox.showwarning("Caracter inválido", "Solo se permiten numeros")
            return False
    return True


def centrar_ventana(ventana, aplicacion_ancho, aplicacion_alto):
    ancho = ventana.winfo_screenwidth()
    alto = ventana.winfo_screenheight()
    x = int(ancho / 2) - int(aplicacion_ancho / 2)
    y = int(alto / 2) - int(aplicacion_alto / 2) - 40 # Resto 40 para que quede mas arriba
    ventana.geometry(f"{aplicacion_ancho}x{aplicacion_alto}+{x}+{y}")


def get_cotizacion_oficial_venta():
    url_dolar_oficial = "https://dolarapi.com/v1/dolares/oficial"
    respuesta = requests.get(url_dolar_oficial, verify=True)

    resp_json = respuesta.json()
    valor_dolar_oficial_venta = resp_json["venta"]
    return valor_dolar_oficial_venta


def get_cotizacion_blue_venta():
    url_dolar_blue = "https://dolarapi.com/v1/dolares/blue"
    respuesta = requests.get(url_dolar_blue, verify=True)

    resp_json = respuesta.json()
    valor_dolar_blue_venta = resp_json["venta"]
    return valor_dolar_blue_venta


# Guardo el color y las fuentes en un solo archivo para hacer mas facil las modificaciones
color_primario = "#2B303A"
color_secundario = "#EEE5E9"
color_terciario = ""

fuente_titulos = "Arial", 16, "bold"
fuente_texto = "Arial", 12, "bold"