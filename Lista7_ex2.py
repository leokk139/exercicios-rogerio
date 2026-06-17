'''
2 - Um pequeno comércio quer analisar as movimentações do dia. Crie um programa 
que receba várias entradas financeiras e armazene-as em uma única lista chamada 
movimentações.  
Valores positivos representam vendas (receitas) e valores negativos representam 
pagamentos (despesas). Pare de registrar quando o usuário digitar 0. 
Cálculos exigidos: Percorra a lista para calcular o total arrecadado (soma dos 
positivos), o total gasto (soma dos negativos) e o saldo final do dia (receitas + 
despesas). 
Saída: Imprima um relatório financeiro simples mostrando esses três valores. Mostre 
também uma mensagem de "Lucro" se o saldo for positivo, ou "Prejuízo" se for 
negativo.
'''

movimentacoes = []
soma_vendas = 0
soma_despesas = 0

while True:
    valor_financeiro = float(input('Digite um valor financeiro (Digite 0 para parar o registro): R$'))
    if valor_financeiro == 0:
        print('Registro fechado.')
        break
    else:
        movimentacoes.append(valor_financeiro)

for item in movimentacoes:
    if item > 0:
        soma_vendas += item
    if item < 0:
        soma_despesas += item

saldo_final = soma_vendas + soma_despesas
print(f'Total Vendas = {soma_vendas} | Total Despesas = {soma_despesas} | Saldo Final = {saldo_final}')

if saldo_final > 0:
    print('Lucro.')

elif saldo_final < 0:
    print('Prejuízo.')

else:
    print('Neutro.')