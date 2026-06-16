'''
8. Faça um algoritmo que leia o nome, salário e número de filhos de 
100 pessoas, e calcule: 
a. O salário médio das pessoas que possuam 2 filhos 
b. O salário médio das que não possuem filhos 
c. Qual a média salarial maior, entre os que têm um e dois filhos 
d. O salário médio geral
'''

soma_geral = 0
soma_2filhos = 0
qtd_2filhos = 0
soma_0filhos = 0
qtd_0filhos = 0
soma_1filho = 0
qtd_1filho = 0

for i in range(100):
    nome = input('Digite seu nome: ')
    salario = float(input('Digite seu salário: '))
    filhos = int(input('Digite a quantidade de filhos: '))

    soma_geral += salario
    
    if filhos == 0:
        soma_0filhos += salario
        qtd_0filhos += 1
    if filhos == 1:
        soma_1filho == salario
        qtd_1filho += 1
    if filhos == 2:
        soma_2filhos += salario
        qtd_2filhos += 1

media_geral = soma_geral / 100
media_2filhos = soma_2filhos / qtd_2filhos
media_0filhos = soma_0filhos / qtd_0filhos
media_1filho = soma_1filho / qtd_1filho

print(f'Média com 2 filhos: {media_2filhos}')
print(f'Média sem filhos: {media_0filhos}')

if media_1filho > media_2filhos:
    print(f'Maior média: 1 filho = {media_1filho}')
else:
    print(f'Maior média: 2 filhos = {media_2filhos}')

print(f'Média geral: {media_geral}')