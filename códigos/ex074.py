from random import randint
n = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print(n)
print(f'O maior valor sorteado foi: {max(n)}')
print(f'O menor valor sorteado foi: {min(n)}')