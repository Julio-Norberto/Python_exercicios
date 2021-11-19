import math

valor = float(input('Informe um valor que possua ponto flutuante: '))
valor_int = math.trunc(valor)

print('A porção inteira do valor informado é: {}'.format(valor_int))
