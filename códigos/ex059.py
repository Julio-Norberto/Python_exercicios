resp = 0
while resp != 5:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite mais um: '))
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior')
    print('[4] - Novos números')
    print('[5] - Sair do programa')
    resp = int(input('Sua opção: '))
    if resp == 1:
        soma = num1 + num2
        print('A soma dos números é de: {}'.format(soma))
        resp = 5
    elif resp == 2:
        mult = num1 * num2
        print('A multiplicação entre os números é igual a: {}'.format(mult))
        resp = 5
    elif resp == 3:
        if num1 > num2:
            print('O {} é maior'.format(num1))
            resp = 5
        else:
            print('O {} é maior'.format(num2))
            resp = 5
print('O programa terminou!')

# o enunciado não dizia para o programa encerrar assim que fosse feita uma das opções, mas eu acreditei que faria mais sentido dessa forma. Para que o programa encerre apenas quando o número 5 for digitado basta tirar o resp = 5 de cada condição.