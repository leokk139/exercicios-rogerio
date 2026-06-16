'''
14. Faça um algoritmo que receba três notas, calcule e mostre a média e o conceito 
que segue a tabela abaixo: 

Média Ponderada          |          Conceito
8,0 |⎯| 10,0                           A
7,0 |⎯ 8,0                             B
6,0 |⎯ 7,0                             C
5,0 |⎯ 6,0                             D
0,0 |⎯ 5,0                             E
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

    elif 8 <= media <= 10:
        print('\n> Nota A\n')

    elif 7 <= media < 8:
        print('\n> Nota B\n')

    elif 6 <= media < 7:
        print('\n> Nota C\n')

    elif 5 <= media < 6:
        print('\n> Nota D\n')

    else:
        print('\n> Nota E\n')