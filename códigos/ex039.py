ano = int(input('Informe seu ano de nascimento: '))
idade = 2021 - ano

if idade < 18:
    anos_faltando = 18 - idade
    print('Você ainda vai se alistar, e faltam {} ano(s) para isso.'.format(anos_faltando))
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    anos_passados = idade - 18
    print('Já passou da hora de se alistar, você devia ter se alistado a {} ano(s)'.format(anos_passados))