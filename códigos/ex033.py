num1 = float(input('Informe um número: '))
num2 = float(input('Informe um número: '))
num3 = float(input('Informe um número: '))

if num1 > num2 and num1 > num3:
    maior = num1
if num1 < num2 and num1 < num3:
    menor = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num2 < num1 and num2 < num3:
    menor = num2
if num3 > num1 and num3 > num2:
    maior = num3
if num3 < num1 and num3 < num2:
    menor = num3
if num1 == num2 and num1 == num3:
    print('Os números são todos iguais!')
else:
    print('O menor número é {} e o maior é {}'.format(menor, maior))