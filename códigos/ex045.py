from time import sleep
import random

pedra = ('pedra')
papel = ('papel')
tesoura = ('tesoura')

print('=' * 24)
print('\033[34mPEDRA, PAPEL OU TESOURA \033[m')
print('=' * 24)
print('Escolha sua opção: ')
print('\033[32m 1 - PEDRA \033[m')
print('\033[31m 2 - PAPEL \033[m')
print('\033[37m 3 - TESOURA \033[m')
escolha = int(input())

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO \n')

lista = [pedra, papel, tesoura]

jogada = random.choice(lista)

print('=' * 9)
print('RESULTADO')
print('=' * 9)
if jogada == 'pedra' and escolha == 1:
    print('\033[34m EMPATE')
elif jogada == pedra and escolha == 2:
    print('\033[35m VOCÊ GANHOU! eu escolhi pedra')
elif jogada == 'pedra' and escolha == 3:
    print('\033[32m EU GANHEI! minha escolha foi pedra')
elif jogada == 'papel' and escolha == 1:
    print('\033[31m EU GANHEI! minha escolha foi papel')
elif jogada == 'papel' and escolha == 2:
    print('\033[36m EMPATE!')
elif jogada == 'papel' and escolha == 3:
    print('\033[33m VOCÊ GANHOU! minha escolha foi papel')
elif jogada == 'tesoura' and escolha == 1:
    print('\033[32m VOCÊ GANHOU! minha escolha foi tesoura')
elif jogada == 'tesoura' and escolha == 2:
    print('\033[31m EU GANHEI! minha escolha foi tesoura')
else:
    print('\033[35m EMPATE!')