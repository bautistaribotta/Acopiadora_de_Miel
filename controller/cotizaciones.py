import requests


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
