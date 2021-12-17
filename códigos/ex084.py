maior = 0
menor = 9999999
tot_pessoas = 0
dados = list()
pessoas = list()
pesadas = list()
leves = list()
while True:
    nome = str(input('Informe o seu nome: '))
    peso = float(input('Informe seu peso: '))
    tot_pessoas += 1
    if peso >= maior:
        maior = peso
        pesadas.append(nome)
    elif peso <= menor:
        leves.append(nome)
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? (S / N)'))
    if resp in 'Nn':
        break
print(f'O total de pessoas cadastradas foi de: {tot_pessoas}')
print(f'As pessoas mais leves são: {leves}')
print(f'As pessoas mais pesadas são: {pesadas}')
