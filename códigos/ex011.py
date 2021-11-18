comp = float(input('Informe o comprimento da parede em metros: '))
alt = float(input('Informe a altura da parede em metros: '))

base = comp * alt
tot_litro = base / 2

print('Para que a parede seja completamente pintada será necessário(s) {} litro(s) de tinta'.format(tot_litro))