from random import randint
tentativa = 0
print('Estou pensando em um número de 0 à 10, tente adivinhar! ')
#conlhendo valor da variável num
num = int(input('Seu chute: '))
#colocando um número aleatório dentro de num2
num2 = randint(0, 10)
#fazendo as condições
while num != num2:
    num = int(input('Você errou, tente novamente: '))
    tentativa += 1
print('Parabéns, você acertou!')
print('Você fez {} tentativa(s)'.format(tentativa))