'''
4 - Crie um programa onde o usuário vai digitando os preços dos produtos que está 
colocando no carrinho de supermercado. Armazene todos os preços em uma lista. O 
cadastro termina quando o usuário digitar um valor negativo. 
Cálculos exigidos: Calcule o valor total da compra. Se o cliente comprou mais de 10 
itens no total, ele ganha um desconto fixo de 5% sobre o valor bruto. 
Saída: Exiba a quantidade total de produtos comprados, o valor bruto, o valor do 
desconto calculado e o valor final a ser pago. 
'''

# precos = []
# qtd_produto = 0
# valor_total = 0
# desconto = 0

# while True:
#     preco_produto = float(input('Digite o preço do produto: '))
#     if preco_produto <= 0:
#         break
#     precos.append(preco_produto)
#     qtd_produto += 1
#     valor_total += preco_produto

# if qtd_produto > 10:
#     desconto = valor_total * 0.05
#     valor_total_desconto = valor_total * 0.95
#     print(f'Quantidade de produtos comprados = {qtd_produto}')
#     print(f'Valor bruto = {valor_total}')
#     print(f'Desconto = {desconto}')
#     print(f'Valor final = {valor_total_desconto}')

# else:
#     print(f'Quantidade de produtos comprados = {qtd_produto}')
#     print(f'Valor bruto = {valor_total}')
#     print(f'Desconto = Sem desconto')
#     print(f'Valor final = {valor_total}')

# ou

precos = []

while True:
    preco_produto = float(input('Digite o preço do produto: '))
    if preco_produto <= 0:
        break
    precos.append(preco_produto)

qtd_produto = len(precos)
valor_total = sum(precos)
desconto = 0

if qtd_produto > 10:
    desconto = valor_total * 0.05
    valor_total_desconto = valor_total * 0.95
    print(f'Quantidade de produtos comprados = {qtd_produto}')
    print(f'Valor bruto = {valor_total}')
    print(f'Desconto = {desconto}')
    print(f'Valor final = {valor_total_desconto}')

else:
    print(f'Quantidade de produtos comprados = {qtd_produto}')
    print(f'Valor bruto = {valor_total}')
    print(f'Desconto = Sem desconto')
    print(f'Valor final = {valor_total}')