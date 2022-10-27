#hay un metodo para ordenar listas mergesort
def mergesort (lista):
    if (len(lista) <= 1):
        return lista
    else:
        medio= len(lista)//2
        izquierda = []
        for i in range (0,medio):
            izquierda.append(lista[i])
        izquierda =mergesort(izquierda)
        derecha= mergesort (derecha)
        if (izquierda[medio-1]<= derecha[0]):
           izquierda += derecha
           return izquierda
        resultado = merge(izquierda,derecha) 
        return resultado 
        
