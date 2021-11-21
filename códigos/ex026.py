frase = str(input('Digite uma frase: ')).lower()

print('A quantidade de letras (a) nessa frase é {}'.format(frase.count('a')))
print('A primeira letra (a) aparece na posição: {}'.format(frase.find('a') + 1))
print('A última posição em que a letra (a) aparece é: {}'.format(frase.rfind('a') + 1))
