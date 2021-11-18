print('=' * 20)
print('ALUGUEL DE CARROS')
print('=' * 20)
#coletando dados
dias = int(input('Informe quantos dias você ficou com o carro: '))
km = float(input('Informe quantos km rodados: '))
#fazendo o cácluco do total dos valores a serem pagos
preco_dias = dias * 60
preco_km = km * 0.15
tot_preco = preco_km + preco_dias
#exibindo resultado final
print('O valor que você deve pagar é: R$ {}'.format(tot_preco))
