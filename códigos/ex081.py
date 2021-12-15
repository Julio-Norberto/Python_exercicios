valores = list()
for c in range(1, 7):
    valores.append(int(input('Digite um valor: ')))
valores.sort(reverse=True)
print(f'Foram digitados {len(valores)} valores')
print(f'A lista ordenada de forma decrescente fica da seguinte forma: {valores}')
if 5 in valores:
    print('E o valor 5 está presente na lista!')
else:
    print('E o valor 5 não está presente na lista!')