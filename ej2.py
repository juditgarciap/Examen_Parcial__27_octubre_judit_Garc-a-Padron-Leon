#hay un metodo para ordenar listas mergesort
def mergesort (lista):
    if (len(lista) <= 1):
        return lista
    else:
        medio= len(lista)//2
        izquierda = []
        for i in range (0,medio):