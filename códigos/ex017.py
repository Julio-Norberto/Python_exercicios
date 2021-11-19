#importando bibliotecas
import math
from math import hypot

#solicitando valores
print('==========================')
print('CALCULADORA DE HIPOTENUSA')
print('==========================')
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))

#Realizando o cálculo da hipotenusa atráves da função hypot
hipotenusa = math.hypot(co, ca)

#Exibindo resultado final
print('O valor da hipotenusa deste triângulo retângulo é de: {:.2f}'.format(hipotenusa))
