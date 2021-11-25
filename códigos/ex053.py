frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
palavrasjuntas = ''.join(palavras)
contrario = ''

for c in range (len(palavrasjuntas) - 1, -1, -1):
    contrario += palavrasjuntas[c]
if contrario == palavrasjuntas:
    print('A frase é um palíndromo')
else: 
    print('A frase não é um palíndromo')