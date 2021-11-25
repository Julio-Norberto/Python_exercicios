maioridade = 0
menoridade = 0
for c in range(1, 8):
    ano = int(input('Informe o ano de nascimento da pessoa {}: '.format(c)))
    if 2021 - ano < 18:
        menoridade += 1
    else:
        maioridade += 1
print('Dessas pessoas {} são maiores de idade e {} são menores de idade'.format(maioridade, menoridade))