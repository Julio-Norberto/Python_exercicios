print('=' * 26)
print('\033[35mAPROVAÇÃO DE EMPRESTIMO\033[m')
print('=' * 26)

val_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salário: '))
anos = int(input('Em quantos anos você pretende pagar? '))

mes = anos * 12
parcela = val_casa / mes
trinta_porc = salario * 30 / 100

if parcela > trinta_porc:
    print('\033[31mDesculpe, não foi possível aprovar o seu emprestimo no momento!\033[m')
else:
    print('\033[32mParabéns! o seu emprestimo foi aprovado.\033[m')