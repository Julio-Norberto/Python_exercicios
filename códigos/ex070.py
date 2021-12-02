mais_de_mil = 0
mais_barato = 99999
produto_barato = 'a'
soma = 0
resp = 1
while True:
    if resp == 1:
        produto = str(input('Insira o nome do produto: '))
        preco = float(input('Informe o preço do produto R$: '))
        soma += preco
        if preco > 1000:
            mais_de_mil += 1
        if preco < mais_barato:
            mais_barato = preco
            produto_barato = produto
        resp = int(input('Quer continuar? [1 - SIM | 0 - NÃO] '))
    else:
        break    
print(f'O total de preço dos produtos foi de: R$ {soma}')
print(f'Os total de produtos que custam mais de mil reais é: {mais_de_mil}')
print(f'E o produto mais barato é: {produto_barato}')