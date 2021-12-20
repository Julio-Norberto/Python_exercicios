valores = list()
pares = list()
impares = list()
for c in range(0, 7):
    v = int(input('Informe um valor: '))
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
valores.append(pares[:])
valores.append(impares[:])
valores[0].sort()
valores[1].sort()
print(f'Os valores pares são: {valores[0]}')
print(f'Os valores impares são: {valores[1]}')
