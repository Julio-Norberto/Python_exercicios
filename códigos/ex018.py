import math

#Coletando um angulo
angulo = int(input('Informe um ângulo: '))

#calculando o angulo com módulos
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

#exibindo o resultado final
print('O seno do ângulo informado é {:.2f} o cosseno é {:.2f} e a tangente é {:.2f}'.format(sen, cos, tan))
