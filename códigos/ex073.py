times = 'flamengo', 'palmeiras', 'chapecoense', 'são paulo', 'gremio', 'fluminense', 'sporte', 'santa cruz'

print('O três primeiros colocados são: ')
for c in range (0, 3):
    print(times[c])
print('\n')
print('Os dois ultimos colocados são: ')
for c in range (6, 8):
    print(times[c])
print('\n')
print('Lista dos times em ordem alfabetica: ')
print(sorted(times))
print('\n')
print('O time chapecoense está na posição')
print(times.index('chapecoense') + 1)