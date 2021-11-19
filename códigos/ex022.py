nome = str(input('Digite seu nome completo: ')).strip()

maiusc = nome.upper()
minusc = nome.lower()
tot_nome = len(nome)
primeiro_nome = nome[0:nome.find(' ')] 

print('Seu nome completo em maiúsculas é: {}'.format(maiusc))
print('Seu nome completo em minúsculas é: {}'.format(minusc))
print('Seu nome ao todo possui {} letras'.format(tot_nome - nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(primeiro_nome, nome.find(' ')))
