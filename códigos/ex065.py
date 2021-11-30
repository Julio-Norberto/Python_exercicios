maior = 0
menor = 9999999
tot_num = 0
soma = 0
resp = 'sim'
while resp == 'sim':
    n = int(input('Informe um número: '))
    resp = str(input('Quer continuar? (sim / não): ')).lower()
    soma = soma + n
    tot_num += 1
    if n < menor:
        menor = n
    if n > maior:
        maior = n

if menor == maior:
    print('Os números são iguais')
else:
    print('O menor número foi {} e o maior {}'.format(menor, maior))
media = soma / tot_num
print('A média dos valores digitados foi de: {}'.format(media))
