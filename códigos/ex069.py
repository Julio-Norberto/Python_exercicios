maioridade = 0
tot_homens = 0
tot_mulher_menos_de_20 = 0
resposta = 1

while True:
    if resposta == 1:
        sexo = str(input('Informe o sexo [M / F]: ')).lower()
        idade = int(input('Informe a idade: '))
        if idade > 18:
            maioridade += 1
        if sexo == 'm':
            tot_homens += 1
        if sexo == 'f' and idade < 20:
            tot_mulher_menos_de_20 += 1
        resposta = int(input('Quer continuar? [1 - sim / 0 - não] '))
    else:
        break
print(f'A quantidade de pessoas com mais de 18 anos é de {maioridade} pessoa(s)')
print(f'A quantidade de homens cadastrados é de: {tot_homens}')
print(f'A quantidade de mulher com menos de 20 anos é de: {tot_mulher_menos_de_20}')