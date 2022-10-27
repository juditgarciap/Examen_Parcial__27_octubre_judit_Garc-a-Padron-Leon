

matriz = [[2,6,7,5,5], [3,0,3,5,0], [1,8,1,2,9], [4,5,8,4,4],[4,5,0,0,0]]

def cogerfactor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]

def determinante(matriz):

    if len(matriz)==2:
        valor = matriz[0][0] * matriz [1][1] - matriz [1][0]

    suma = 0

    for columna_actual in range(len(matriz)):

        signo = (-1) ** (columna_actual)
        sub_det = determinante(cogerfactor(matriz, 0, columna_actual))
        suma += (signo * matriz[0][columna_actual] * sub_det)

    return suma

print("El determinante es:", determinante(matriz))