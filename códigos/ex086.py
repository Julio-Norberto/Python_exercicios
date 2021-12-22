matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Informe um número para preencher a matriz:'))


for l in range(0, 3):
    for c in range(0, 3):
        print(matriz[l][c], end=' ')
    print(' ')
print(matriz[l][c])