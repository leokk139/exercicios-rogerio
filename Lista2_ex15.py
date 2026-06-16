'''
15. Faça um algoritmo que receba três notas de um aluno, calcule e mostre a média 
aritmética e a mensagem que segue a tabela abaixo. Para alunos de exame, 
calcule e mostre a nota mínima a ser tirada no exame para que o aluno obtenha 
aprovação, considerando que a média no exame é 6,0.

Média Ponderada          |          Conceito
0,0 |⎯ 3,0                            Reprovado
3,0 |⎯ 7,0                            Exame
7,0 |⎯| 10,0                          Aprovado
'''

try:
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    nota3 = float(input('Digite a nota 3: '))

    media = (nota1 + nota2 + nota3) / 3

except ValueError:
    print('\n> Digite uma nota válida.\n')

else:
    if nota1 < 0 or nota2 < 0 or nota3 < 0:
        print('\n> Digite uma nota entre 0 a 10.\n')
    
    elif nota1 > 10 or nota2 > 10 or nota3 > 10:
        print('\n> Digite uma nota entre 0 a 10.\n')

    elif 0 <= media < 3:
        print('\n> Reprovado.\n')

    elif 3 <= media < 7:
        print('\n> Exame.\n')

    else:
        print('\n> Aprovado.\n')