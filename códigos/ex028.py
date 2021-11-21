#importando biblioteca
from random import randint

print('Estou pensando em um número de 0 a 5, teste adivinhar! ')
#conlhendo valor da variável num

num = int(input('Seu chute: '))
#colocando um número aleatório dentro de num2

num2 = randint(0, 5)
#fazendo as condições

if num == num2:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou!')
print('O número que pensei foi {}'.format(num2))
