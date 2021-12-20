valores = list()
pares = list()
impares = list()
for c in range(0, 6):
    v = int(input('Informe um valor: '))
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
valores.append(pares[:])
valores.append(impares[:])
print(valores)
