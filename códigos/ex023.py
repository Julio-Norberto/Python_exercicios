num = int(input('Informe um número: '))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

print('O milhar é {} a centena é {} a dezena {} e a unidade {}'.format(m, c, d, u))
