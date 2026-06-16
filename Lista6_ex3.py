'''
3. Uma escola deseja saber se existem alunos cursando, simultaneamente, as disciplinas 
Lógica e Linguagem de Programação. Coloque os números das matrículas dos alunos 
que cursam Lógica em uma lista, no máximo 10 alunos. Coloque os números das 
matrículas dos alunos que cursam Linguagem de Programação em outra lista, no 
máximo 8 alunos. Mostre o número de matrícula que aparece nas duas listas. 
'''

logica = ['01', '04', '06', '12', '13', '15', '20', '21', '25', '27']
ling_program = ['01', '02', '03', '06', '07', '13', '17', '24']
ambas = []

for item in logica:
    if item in logica and item in ling_program:
        ambas.append(item)

print(f'Matéria de Lógica: {logica}\nMatéria de Linguagem de Programação: {ling_program}')
print(f'Alunos que cursam ambas matérias: {ambas}')