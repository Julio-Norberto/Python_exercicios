mediafinal = 0
mediaidade = 0
maioridade = 0
homemvelho = str
totmulhermenos20 = 0
for c in range (1, 5):
    nome = str(input('Informe seu nome: '))
    idade = int(input('Informe sua idade: '))
    sexo = int(input('Informe seu sexo (1 - para masculino | 2 - para feminino): '))
    mediaidade += idade
    if sexo == 1 and idade > maioridade:
        maioridade = idade
        homemvelho = nome
    elif sexo == 2 and idade < 20:
        totmulhermenos20 += 1

mediafinal = mediaidade / 4
print('E média de idade do grupo é de: {}'.format(mediafinal))
print('O nome do homem mais velho é: {}'.format(homemvelho))
print('A quantidade de mulheres com menos de 20 anos é de: {}'.format(totmulhermenos20))
