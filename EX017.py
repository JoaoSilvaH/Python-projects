import math


cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))

cateto_adjacente = float(input('\n\nDigite o comprimento do cateto adjacente: '))

calc_hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print('=' * 30)

print(f'De acordo com os dados fornecidos, cateto oposto = {cateto_oposto}, cateto adjacente = {cateto_adjacente} \n\n O resultado do valor da Hipotenusa é = {calc_hipotenusa:.2f}')

print('=' * 30)