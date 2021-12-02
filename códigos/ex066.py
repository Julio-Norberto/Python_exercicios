n = 0
soma = 0
tot = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    tot += 1
print(f'Você digitou {tot} números e a soma deles é {soma}')