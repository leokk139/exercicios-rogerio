'''
2. Desenvolva um programa que simule as operações básicas de um 
caixa eletrônico. O cliente começa com um saldo de R$ 0,00. O 
programa deve exibir um menu contínuo com as seguintes regras: 
• O menu deve ter 4 opções: Ver Saldo, Depositar, Sacar e Sair. 
• Crie uma função para o depósito e outra para o saque. Ambas 
devem receber o saldo atual e o valor da operação. Obs: 
devem retornar o saldo atualizado. 
• A função de saque não pode permitir que o usuário saque um 
valor maior do que ele tem na conta (deve exibir uma 
mensagem de erro). 
• Valores de depósito e saque não podem ser negativos 
'''

def depositar(saldo, valor):
    if valor <= 0:
        print('Valor inválido.')
    saldo += valor
    return saldo

def sacar(saldo, valor):
    if valor <= 0:
        print('Valor inválido.')
    if valor > saldo:
        print('Saldo insuficiente.')
    saldo -= valor
    return saldo

saldo = 0

while True:
    print('1 - Ver saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Sair')
    opcao = int(input('Digite uma opção: '))
    match opcao:
        case 1:
            print(f'Saldo: R${saldo}')
        case 2:
            valor = float(input('Digite o valor a depositar (somente numeros): '))
            saldo = depositar(saldo, valor)
        case 3:
            valor = float(input('Digite o valor pra sacar: '))
            saldo = sacar(saldo, valor)
        case 4:
            break
        case _:
            print('Opção inválida.')