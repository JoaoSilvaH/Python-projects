
formatacao = ''

print("=" * 30)

print(f'{' BEM VINDO A CALCULADORA DE DESCONTOS ' + formatacao:-^50}\n\n')

print(f'{' AQUI VOCE PODE CALCULAR O VALOR QUE SEU PRODUTO TERA COM O DESCONTO. ' + formatacao:-^85}')

val_product = float(input('\n\nDigite o valor do produto: R$'))

discount = val_product * 0.05

after_discount = val_product - discount

print(f'O valor do seu produto que é de R${val_product:.2f} pós-desconto: R${after_discount:.2f}')


print('=' * 30)