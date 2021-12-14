palavras = 'tela', 'computador', 'janela', 'programcao', 'estudar', 'python', 'azul', 'lilas'

for c in palavras:
    print(f'\n na palavra {c} temos', end=' ')
    for letra in c:
        if letra in 'aeiou':
            print(letra, end=' ')