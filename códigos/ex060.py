n = int(input('Digite um número: '))
fatorial = 1
while n > 1:
    fatorial = fatorial * n
    n = n - 1
print('O fatorial desse número é: {}'.format(fatorial))