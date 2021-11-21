nome = str(input('Informe seu nome completo: ')).strip()

print('Seu primeiro nome é: {}'.format(nome[0:nome.find(' ')]))
print('Seu último nome é: {}'.format(nome[nome.rfind(' '):]))