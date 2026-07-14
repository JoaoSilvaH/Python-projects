n1=float(input("Digite um numero para ser analisado: "))

calc_par = n1 % 2

if n1.is_integer:
    print(" ")
    
else: 
    print("Numeros decimais não são permitidos!! Por favor digite um numero Inteiro!")
    
    
if calc_par == 0:
    print(f"O numero {n1:.1f} é um numero par")
    
else:
    print(f"O numero {n1:.1f} é impar")
    
    
    