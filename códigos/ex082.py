valores = list()
valores_par = list()
valores_impar = list()
for c in range (0, 7):
    valores.append(int(input('Digite um valor: ')))
    if valores[c] % 2 == 0:
        valores_par.append(valores[c])
    else:
        valores_impar.append(valores[c])
print(f'A lista original digitada é: {valores}')
print(f'A lista contendo apenas números pares é: {valores_par}')
print(f'A lista contendo apenas números impares é? {valores_impar}')
