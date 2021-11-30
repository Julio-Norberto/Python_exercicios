primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
termo = primeiro
cont = 1
total = 0
outros = 10
while outros != 0:
    total = total + outros
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    outros = int(input('Quantos termos a mais você deseja exibir? '))
print('Progressão finalizada, foram exibidos {} termos'.format(total))