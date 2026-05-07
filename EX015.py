dias_percorridos = int(input('Digite a quantidade de dias que voce utilizou o carro: '))

km_rodados =  float(input('\n\nDigite a quantidade de km rodados com o carro: '))

print("=" * 30)

calc_dias = (dias_percorridos * 60)

calc_km_rodados = (km_rodados * 0.15)

calc_valor_final = calc_dias + calc_km_rodados

resultado =  print(f'De acordo com os dados passados voce dirigiu por {dias_percorridos} dias e rodou por {km_rodados:.2f}km \n\n O valor final a ser pago é de: R${calc_valor_final:.2f}')

print('=' * 30)

print(resultado)

