vel = float(input('Informe a velocidade do carro(km): '))

if vel > 80:
    print('Você foi multado!')
    multa = (vel - 80) * 7
    print('Sua multa foi de {} R$'.format(multa))
else:
    print('Você estava dentro do limite de velocidade, dirija com cuidado!')
