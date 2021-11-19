import random

#coletando os nomes
aluno1 = input('Informe o nome do primeiro aluno: ')
aluno2 = input('Informe o nome do segundo: ')
aluno3 = input('Informe o nome do terceiro: ')
aluno4 = input('Informe o nome do quarto: ')

#Criando uma lista com os nomes de todos os alunos
lista = [aluno1, aluno2, aluno3, aluno4]

#criando uma ordem aleatória dos nomes
random.shuffle(lista)

#exibindo o resultado final
print('A ordem de apresentação do trabalho será: {}'.format(lista))