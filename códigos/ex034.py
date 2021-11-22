salario = float(input('Informe seu salário: '))

if salario > 1250:
    reajuste = (salario * 10 / 100)
    novo_salario = reajuste + salario
else:
    reajuste = (salario * 15 / 100)
    novo_salario = reajuste + salario

print('O seu reajuste foi de {} e o seu novo salário será de {}'.format(reajuste, novo_salario))