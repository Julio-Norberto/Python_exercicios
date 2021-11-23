print('\nSeu produto custa R$ 40, os meios de pagamento disponíveis são: \n')

print('\033[32m 1 - Dinheiro/Cheque (10 porcento de desconto)\033[m')
print('\033[33m 2 - à vista no cartão (5 porcento de desconto)\033[m')
print('\033[34m 3 - em 2x no cartão (preço normal)\033[m')
print('\033[35m 4 - em 3x ou mais (com 20 porcento de juros)\033[m \n')
escolha = int(input('Escolha o método de pagamento: '))

if escolha == 1:
    desconto = 40 * 10 / 100
    preco_final = 40 - desconto
    print('\n Você ganhou 10 porcento de desconto!')
    print('\033[32m O valor final do produto é de: R$ {} \033[m'.format(preco_final))
elif escolha == 2:
    preco2 = 40 - (40 * 5 / 100)
    print('Você ganhou 5 porcento de desconto!')
    print('O preço final do produto ficou: R$ {}'.format(preco2))
elif escolha == 3:
    print('Parabéns pela compra!')
else: 
    preco3 = 40 + (40 * 20 / 100)
    print('Com a opção 4 o valor da sua compra ganha um adicional de 20 porcento')
    print('O preço final do produto sai por: R$ {}'.format(preco3))