#Matriz bidimensional 10x1
matriz1 = [
    [9],
    [5],
    [3],
    [1],
    [8],
    [4],
    [2],
    [6],
    [7],
    [10]
]
#imprimir la matriz no ordenada
print("Matriz no ordenada:",matriz1)

#ordenar las filas de la matriz
matriz1.sort(key=lambda fila: min(fila))

#resultado ordenado
print("Matriz ordenada por Valor Mimimo en la fila:")
for fila in matriz1:
    print(fila)

print("fin")