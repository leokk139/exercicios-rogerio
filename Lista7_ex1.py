'''
1 - Crie duas listas vazias: nomes e medias. Escreva um programa que peça ao usuário 
para digitar o nome de 5 alunos e a média final de cada um. Guarde os nomes na 
primeira lista e as médias na segunda lista. 
Cálculos exigidos: Após o cadastro, o programa deve percorrer as listas e calcular a 
média geral da turma. 
Saída: Imprima o nome de cada aluno ao lado de sua nota e, ao final, informe quantos 
alunos ficaram acima da média geral da turma. 
'''

# nomes = []
# medias = []
# soma_medias = 0
# qtd_acima_da_media = 0

# for i in range(5):
#     nome_aluno = input('Digite o nome do aluno: ')
#     media_aluno = float(input('Digite a média desse aluno: '))
#     nomes.append(nome_aluno)
#     medias.append(media_aluno)

# for i in range(5):
#     print(f'{nomes[i]} - {medias[i]}')

# for item in medias:
#     soma_medias += item

# media_geral = soma_medias / 5

# for item in medias:
#     if item >= media_geral: #tem que ser maior ou igual pq se td mundo tirar 10, printa q ngm ta acima da media
#         qtd_acima_da_media += 1

# print(f'Média Geral = {media_geral}')
# print(f'Quantidade de alunos acima da média geral = {qtd_acima_da_media}')

# ou

nomes = []
medias = []
qtd_acima_da_media = 0

for i in range(5):
    nome_aluno = input('Digite o nome do aluno: ')
    media_aluno = float(input('Digite a média desse aluno: '))
    nomes.append(nome_aluno)
    medias.append(media_aluno)

for i in range(5):
    print(f'{nomes[item]} - {medias[item]}')

media_geral = sum(medias) / len(medias)

for item in medias:
    if item >= media_geral: #tem que ser maior ou igual pq se td mundo tirar 10, printa q ngm ta acima da media
        qtd_acima_da_media += 1

print(f'Média Geral = {media_geral}')
print(f'Quantidade de alunos acima da média = {qtd_acima_da_media}')