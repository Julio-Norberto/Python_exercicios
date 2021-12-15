valores = list()
for c in range(1, 6):
    valores.append(int(input('Informe um valor: ')))
menor = min(valores)
maior = max(valores)
print(f'O menor valor desses números é {min(valores)} e ele está na posição {valores.index(menor) + 1}')
print(f'O maior valor desses números é {max(valores)} e ele está na posição {valores.index(maior) + 1}')
