soma = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 1:
        soma = soma + n
print('A soma dos números impares é de: {}'.format(soma))
