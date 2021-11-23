ano = int(input('Informe o ano de nascimento: '))
idade = 2021 - ano

if idade <= 9:
    print('Sua categoria é: MIRIM')
elif idade > 9 and idade <= 14:
    print('Sua categoria é: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Sua categoria é: JUNIOR')
elif idade > 19 and idade <= 25:
    print('Sua categoria é: SÊNIOR')
elif idade > 25:
    print('Sua categoria é: MASTER')
