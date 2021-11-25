totprimo = 0
n = int(input('Informe um número: '))
for c in range (1, n + 1):
    if n % c == 0:
        print('\033[32m', end='')
        totprimo += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='' )
print('\n')
if totprimo > 2:
    print('\033[m O número não é primo, pois pode ser dividido por {} números'.format(totprimo))
else:
    print('\033[m O número é primo pois só pode ser dividido por 1 e por ele mesmo.')