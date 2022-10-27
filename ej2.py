#en los apuntes podemos  encontrar este algoritmo y creo que tambien se puede resolver con este
def centinela(lista,buscado):

posicion = -1
for i in range (0,len(lista)):
    if (lista[i] == buscado):
        posicion = i
        break 
    return posicion

print (centinela(lista,145))
if 145 not in lista:
    print(-1)







#hay un metodo para ordenar listas mergesort ( no se si esto se debe usar así)

from csv import list_dialects


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
        resultado = mergesort(izquierda,derecha) 
        return resultado 

#función para mezclar las listas
def merge(izquierda,derecha):
    lista_mezcla =[]
    while (len(izquierda>0)) and (len(derecha> 0):
        if (izquierda[0]< derecha[0]):
            lista_mezcla.append (izquierda.pop(0)
        else:
            lista_mezcla.append(derecha.pop(0))
    if(len(izquierda)>0):
        lista_mezcla += izquierda 
    if (len(derecha)>0):
        lista_mezcla += derechaç
    return lista_mezcla


lista = [8, 50, 210, 80, 145, 333, 70, 30] 
print(mergesort(lista))




if __name__ == "__name__":
    import doctest 
    doctest.tesmode()