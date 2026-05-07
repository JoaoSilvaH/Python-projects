from random import shuffle, sample
print('=' * 30)
al1= str(input('Digite o nome do primeiro aluno: '))
al2= str(input('\nDigite o nome do segundo aluno:'))
al3= str(input('\nDigite o nome do terceiro aluno: '))
al4= str(input('\nDigite o nome do quarto aluno: '))
print('=' * 30)
alunos = sample([al1,al2,al3,al4], 4)

print(f'A ordem de escolha para o projeto é essa: {alunos}')

print('=' * 30)
