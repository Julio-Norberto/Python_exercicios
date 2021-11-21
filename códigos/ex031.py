dist = float(input('Informe a distância (km) da viagem: '))

if dist <= 200:
    print('Sua viagem irá custar: {}R$'.format(dist * 0.50))
else:
    print('Sua viagem irá custar: {}R$'.format(dist * 0.45))
