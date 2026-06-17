'''
3 - Dadas duas listas já preenchidas no código, uma com os nomes dos funcionários 
(funcionarios = ['Ana', 'Bruno', 'Carlos', 'Diana']) e outra com seus respectivos salários 
(salarios = [1500.0, 3200.0, 1800.0, 4500.0]).

Cálculos exigidos: A empresa dará um aumento. Quem ganha até R$ 2000,00 receberá 
15% de aumento. Quem ganha mais de R$ 2000,00 receberá 10%. Modifique os valores 
diretamente na lista salarios aplicando a regra matemática adequada.

Saída: Percorra as listas atualizadas e imprima um holerite simples no formato: "Nome: 
X - Novo Salário: R$ Y"
'''

funcionarios = ['Ana', 'Bruno', 'Carlos', 'Diana']
salarios = [1500.0, 3200.0, 1800.0, 4500.0]

for item in range(len(salarios)):
    if salarios[item] <= 2000:
        salarios[item] = salarios[item] * 1.15
    else:
        salarios[item] = salarios[item] * 1.10

for item in range(len(funcionarios)):
    print(f'Nome: {funcionarios[item]}| Novo Salário: R${salarios[item]:.2f}')