while True:
    n = int(input('Informe um número: '))
    if n < 0:
        print('Fim do programa')
        break
    else:
        print('A tabuada deste número é: ')
        for c in range(1, 11):
            print(f'{n} x {c} = {n * c}')