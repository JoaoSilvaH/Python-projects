print("=" * 30)

print('Vamos analisar as medidas da sua parede \n\n')

print("=" * 30) 
altura =    float(input('Digite o valor da altura da parede (nao eh necessario dizer que esta em metros): ' "\n\n"))
largura =   float(input('Agora digite o valor da largura da parede: ' "\n\n"))


a_parede = largura * altura

qtd_litros = a_parede / 2

print(f'A quantidade em litros de tinta para pintar a sua parede que possui uma área de {a_parede:.2f}m² \n\n Seria de: {qtd_litros:.2f}L \n\n')


print("=" * 30)