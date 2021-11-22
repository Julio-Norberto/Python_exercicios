print('=' * 20)
print('CONVERSOR DE BASES')
print('=' * 20)

print('\033[34m 1 - PARA BINÁRIO\033[m')
print('\033[33m 2 - PARA OCTAL\033[m')
print('\033[35m 3 - PARA HEXADECIMAL\033[m')
escolha = int(input('Selecione uma opção: '))
num = int(input('Informe um número: '))

if escolha == 1:
    binario = bin(num)[2:]
    print('A conversão desse número para binário é: {}'.format(binario))
elif escolha == 3:
    hexadecimal = hex(num)[2:]
    print('A conversão desse número para hexadecimal é: {}'.format(hexadecimal))
else:
    octal = oct(num)[2:]
    print('A conversão desse número em octal é? {}'.format(octal))