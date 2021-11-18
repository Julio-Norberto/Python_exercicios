preco = float(input('Informe o preço do produto: '))

desc = preco * 5 / 100
novo_val = preco - desc

print('Você acaba de ganhar 5% de desconto, o novo valor é de {}R$'.format(novo_val))