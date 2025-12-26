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