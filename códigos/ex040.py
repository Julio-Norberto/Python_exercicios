nota1 = float(input('Inforem a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('\033[31m REPROVADO\033[m')
elif media >= 5.0 and media <= 6.9:
    print('\033[33m RECUPERAÇÃO\033[m')
else:
    print('\033[32m APROVADO\033[m')