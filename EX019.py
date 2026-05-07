from random import choice

aluno1 = str(input('Digite o nome do primeiro aluno :'))
aluno2 = str(input('\nDigite o nome do segundo aluno :'))
aluno3 = str(input('\nDigite o nome do terceiro aluno :'))
aluno4 = str(input('\nDigite o nome do quarto aluno :'))

alunos = choice([aluno1,aluno2, aluno3, aluno4])

print(f'\n\n O aluno escolhido foi: {alunos}')