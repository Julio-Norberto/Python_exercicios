tot_nove = 0
print('Inforem quantro numeros: ')
n1 = int(input('Valor: '))
n2 = int(input('valor: '))
n3 = int(input('valor: '))
n4 = int(input('valor: '))
tupla = n1, n2, n3, n4
if n1 == 9:
    tot_nove += 1
if n2 == 9:
    tot_nove += 1
if n3 == 9:
    tot_nove += 1
if n4 == 9:
    tot_nove+= 1
if n1 % 2 == 0:
    print(f'{n1} foi um numero par')
if n2 % 2 == 0:
    print(f'{n2} foi um número par')
if n3 % 2 == 0:
    print(f'{n3} foi um número par')
if n4 % 2 == 0:
    print(f'{n4} foi um número par')
print(f'O total de números 9 foi de {tot_nove}')
print('O primeiro valor três esta na posição: ', end='')
print(tupla.index(3) + 1)