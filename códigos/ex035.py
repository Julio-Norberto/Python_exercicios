reta1 = float(input('Informe o comprimento da reta 1: '))
reta2 = float(input('Informe o comprimento da reta 2: '))
reta3 = float(input('Informe o comprimento da reta 3: '))

if reta2 - reta3 < reta1 and reta1 < reta2 + reta3:
    print('Essas retas podem formar um triângulo!')
else:
    print('Esse Não podem formar um triângulo')