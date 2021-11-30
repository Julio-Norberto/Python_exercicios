soma = 0
tot_num = 0
n = 0
while n != 999:
    n = int(input('Digite um número: '))
    tot_num += 1
    if n != 999:
        soma = soma + n
print('Você digitou {} número(s) e a soma de todos eles é de: {}'.format(tot_num - 1, soma))