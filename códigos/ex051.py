t = int(input('Informe o primeiro termo da PA: '))
r = int(input('Agora informe a razão: '))
c = 0
print(t)
for c in range(1, 10):
    t = t + r
    print(t)
print('Esses são os 10 primeiros termos dessa PA')