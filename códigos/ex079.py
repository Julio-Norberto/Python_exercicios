valores = list()
resp = 'sim'
while resp == 'sim':
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Este número já foi digitado, então não será adicionado')
    else:
       valores.append(valor)
    resp = str(input('Quer continuar? (SIM / NAO)')).lower()
print(f'A lista de valores ordenada é {sorted(valores)}')