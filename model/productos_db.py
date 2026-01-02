import mysql.connector
from model.entidades import Producto


def nuevo_producto(producto : Producto):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="southern_honey_group"
    )
    cursor = conexion.cursor()

    instruccion_sql = """INSERT INTO productos (nombre, categoria, unidad_medida, precio, cantidad) 
                        VALUES (%s, %s, %s, %s, %s)"""

    valores = (producto.nombre, producto.categoria,
               producto.unidad_medida, producto.precio, producto.cantidad)

    cursor.execute(instruccion_sql, valores)
    conexion.commit()

    cursor.close()
    conexion.close()


def editar_producto(id_producto, producto : Producto):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="southern_honey_group"
    )
    cursor = conexion.cursor()

    instruccion_sql = ("UPDATE productos SET nombre=%s, categoria=%s, unidad_medida=%s, "
                       "precio=%s, cantidad=%s WHERE id = %s")

    valores = (producto.nombre, producto.categoria, producto.unidad_medida,
               producto.precio, producto.cantidad, id_producto)

    cursor.execute(instruccion_sql, valores)

    conexion.commit()
    cursor.close()
    conexion.close()


def eliminar_producto(id_producto):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="southern_honey_group"
    )
    cursor = conexion.cursor()

    instruccion_sql = """DELETE FROM productos WHERE id = %s"""
    valor = (id_producto,)
    cursor.execute(instruccion_sql, valor)
    conexion.commit()

    cursor.close()
    conexion.close()


def buscar_producto_nombre(nombre_producto):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="southern_honey_group"
    )
    cursor = conexion.cursor()

    instruccion_sql = "SELECT id, nombre, categoria, cantidad FROM productos WHERE nombre LIKE %s"
    valor = (f"%{nombre_producto}%",)

    cursor.execute(instruccion_sql, valor)
    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()
    return resultados


def buscar_producto_id(id_producto):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="southern_honey_group"
    )
    cursor = conexion.cursor()

    instruccion_sql = "SELECT id, nombre, categoria, cantidad FROM productos WHERE id LIKE %s"
    valor = (f"%{id_producto}%",)

    cursor.execute(instruccion_sql, valor)
    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()
    return resultados