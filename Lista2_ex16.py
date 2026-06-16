'''
16. Fazer um algoritmo para ajudar a bilheteria do metrô.  O operador deve informar 
o tipo do bilhete (unitário, duplo ou 10 viagens) e o valor pago pelo passageiro.  
O sistema deve mostrar, então, a quantidade de bilhetes possíveis e o troco que o 
passageiro deve receber. 
Considere a seguinte tabela de preço: 

Bilhete unitário  ..................................... 1,30 
Bilhete duplo  ........................................ 2,60 
Bilhete de 10 viagens  ......................... 12,00
'''

# 4 variáveis: tipo do bilhete, valor pago, quantidade de bilhete e troco

try:
    tipo_bilhete = input('---\nDigite o tipo do bilhete (unitário, duplo ou 10 viagens): ').lower()
    valor_pago = float(input('Digite o valor pago pelo passageiro (use "." caso tenha centavos): '))

except ValueError:
    print('\n> Digite um valor válido.\n')

else:
    match tipo_bilhete:
        case 'unitário':
            preco_bilhete = 1.30
        case 'duplo':
            preco_bilhete = 2.60
        case '10 viagens':
            preco_bilhete = 12.00
        case _:
            print('\n> Tipo inválido.\n')
            exit()

    quantidade_bilhete = int(valor_pago / preco_bilhete)
    troco = valor_pago - (quantidade_bilhete * preco_bilhete)

    print(f'\n> Quantidade de bilhetes: {quantidade_bilhete}\n> Troco: R${troco:.2f}\n---')