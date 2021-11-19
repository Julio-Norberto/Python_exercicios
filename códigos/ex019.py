import random

#coletando os nomes dos alunos
aluno1 = input('Informe o nome do primeiro aluno: ')
aluno2 = input('Informe o nome do segundo: ')
aluno3 = input('Informe o nome do terceiro: ')
aluno4 = input('Informe o nome do quarto: ')

#jogando todos os nomes dentro de uma única variável
lista = [aluno1, aluno2, aluno3, aluno4]

#fazendo a escolha aleatoria usando o módulor random
sorteado = random.choice(lista)

#exibindo resultado final
print('O aluno sorteado foi: {}'.format(sorteado))
