#cremos la tabla

def tabla(size):
    tabla = [None] * size 
    return tabla

#definimos la funcion hash 
def fhash (dato, tamanio_tabla):
    return dato % tamanio_tabla

def agregar(tabla, dato, conver):
    posicion = funcion_hash(ord(dato), len(tabla))

    if (tabla[posicion] is None):
        if conver:
            tabla[posicion] = conver8chr(dato)
        else:
            tabla[posicion] = dato
    else:
        print('existe una colision')


def conver8chr(s: str) -> str:
    if not s.isascii():
        raise ValueError("ASCII only allowed")
    return " ".join(f"{ord(i):08b}" for i in s)

def binaryToDecimal(n):
    return int(n,2)

tabla1 = crear_tabla(255)
tabla2 = crear_tabla(255)




