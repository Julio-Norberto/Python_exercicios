maior = 0
menor = 9999999
tot_pessoas = 0
dados = list()
pessoas = list()
pesadas = list()
leves = list()
for c in range(0, 6):
    nome = str(input('Informe o seu nome: '))
    peso = float(input('Informe seu peso: '))
    tot_pessoas += 1
    if peso > maior:
        maior = peso
        pesadas.append(nome)
    else:
        leves.append(nome)
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
print(f'O total de pessoas cadastradas foi de: {tot_pessoas}')
print(f'As pessoas mais leves são: {leves}')
print(f'As pessoas mais pesadas são: {pesadas}')
