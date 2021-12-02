from time import sleep
import random

pedra = ('pedra')
papel = ('papel')
tesoura = ('tesoura')
cont = 0

while True:
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
        print('\033[34m EMPATE \033[m')
    elif jogada == pedra and escolha == 2:
        print('\033[35m VOCÊ GANHOU! eu escolhi pedra \033[m')
        cont += 1
    elif jogada == 'pedra' and escolha == 3:
        print('\033[32m EU GANHEI! minha escolha foi pedra \033[m')
        break
    elif jogada == 'papel' and escolha == 1:
        print('\033[31m EU GANHEI! minha escolha foi papel \033[m')
        break
    elif jogada == 'papel' and escolha == 2:
        print('\033[36m EMPATE! \033[m')
    elif jogada == 'papel' and escolha == 3:
        print('\033[33m VOCÊ GANHOU! minha escolha foi papel \033[m')
        cont += 1
    elif jogada == 'tesoura' and escolha == 1:
        print('\033[32m VOCÊ GANHOU! minha escolha foi tesoura \033[m')
        cont += 1
    elif jogada == 'tesoura' and escolha == 2:
        print('\033[31m EU GANHEI! minha escolha foi tesoura \033[m')
        break
    else:
        print('\033[35m EMPATE! \033[m')
if cont == 1:
    print('Você ganhou apenas 1 vez')
else:
    print(f'Você ganhou um total de {cont} vezes seguidas')