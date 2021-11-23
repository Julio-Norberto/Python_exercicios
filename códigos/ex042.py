reta1 = float(input('Informe o comprimento da reta 1: '))
reta2 = float(input('Informe o comprimento da reta 2: '))
reta3 = float(input('Informe o comprimento da reta 3: '))

if reta2 - reta3 < reta1 and reta1 < reta2 + reta3:
    print('Essas retas podem formar um triângulo!')
    if reta1 == reta2 == reta3:
        print('Este triângulo é do tipo: EQUILATERO')
    elif reta1 != reta2 and reta2 != reta3:
        print('Este triângulo é do tipo: ESCALENO')
    else:
        print('Este triângulo é do tipo: ISÓSCELES')
