from math import radians, cos, sin, tan

valor_angulo = float(input('Digite o angulo que deseja saber seu seno, cosseno e tangente: '))

seno        = sin(radians(valor_angulo))
cosseno     = cos(radians(valor_angulo))
tangente    = tan(radians(valor_angulo))


print(f'Seno de {valor_angulo:.1f} = {seno:.2f}')
print('\n\n')
print('=' * 30)
print(f'Cosseno de {valor_angulo:.1f} = {cosseno:.2f}')
print('\n\n')
print('=' * 30)
print(f'Tangente de {valor_angulo:.1f} = {tangente:.2f}')
print('=' * 30)