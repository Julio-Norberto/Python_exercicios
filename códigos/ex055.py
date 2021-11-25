maiorpeso = 0
menorpeso = 9999
for c in range (1, 6):
    peso = float(input('Informe seu peso: '))
    if peso > maiorpeso:
        maiorpeso = peso
    if peso < menorpeso:
        menorpeso = peso
print('O maior peso da lista é: {} e o menor peso é: {}'.format(maiorpeso, menorpeso))
