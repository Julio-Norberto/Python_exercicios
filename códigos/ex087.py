matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
soma = list()
maior = list()
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Informe um número para preencher a matriz:'))
        if matriz[l][c] % 2 == 0:
            pares = pares + matriz[l][c]

soma.append(matriz[0][2])
soma.append(matriz[1][2])
soma.append(matriz[2][2])

for l in range(0, 3):
    for c in range(0, 3):
        print(matriz[l][c], end='')
    print()
print(matriz[l][c])
print(f'A soma dos números pares digitados é de: {pares}')
print(f'A soma dos valores da coluna 3 é de: {soma[0] + soma[1] + soma[2]}')
print(f'O maior valor da linha 2 é: {max(matriz[1])}')