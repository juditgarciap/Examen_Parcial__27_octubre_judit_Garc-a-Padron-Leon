

matriz = [[2,6,7,5,5], [3,0,3,5,0], [1,8,1,2,9], [4,5,8,4,4],[4,5,0,0,0]]

def cogerfactor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]



print("El determinante es:", determinante(matriz))