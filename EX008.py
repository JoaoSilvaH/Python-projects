valor_m = float(input("Digite o valor em metros: "))

convert_cm = valor_m * 100

convert_mm = convert_cm * 10

convert_dm =  valor_m * 10

convert_dam = valor_m/10

convert_hec = convert_dam/10

convert_km  = convert_hec/10




resultados = f'O valor de {valor_m:.1f}m convertido para Centimetros eh de {convert_cm:.1f}cm \n\nO Valor convertido de {valor_m:.1f}m para Milimetros eh de {convert_mm:.1f}mm \n\nO valor convertido de {valor_m:.1f}m para Decimetros eh {convert_dm}dm \n\nO valor convertido de {valor_m:.1f}m para Hectometros eh de {convert_hec:.1f}hec \n\nO valor convertido de {valor_m:.1f}m para Kilometros eh {convert_km:.1f}km'

print(resultados)