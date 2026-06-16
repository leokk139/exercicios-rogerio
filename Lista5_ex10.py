'''
10. Suponha que serão digitados 100 números inteiros via teclado, faça 
um algoritmo para: 
a. Somar os números positivos 
b. Contar os números negativos. 
c. A média dos números negativos e a média dos números 
positivos. 
d. A diferença entre o total de números positivos e negativos.
'''

soma_pos = 0
soma_neg = 0
qtd_pos = 0
qtd_neg = 0

for i in range(100):
    num = int(input('Digite um número: '))
    if num > 0:
        soma_pos += num
        qtd_pos += 1
    if num < 0:
        soma_neg += num
        qtd_neg += 1
    if num == 0:
        print('0 é neutro')

media_pos = soma_pos / qtd_pos
media_neg = soma_neg / qtd_neg
diferenca = qtd_pos - qtd_neg

print(f'Soma positivos: {soma_pos}')
print(f'Quantidade negativos: {qtd_neg}')
print(f'Média positivos: {media_pos}')
print(f'Média negativos: {media_neg}')
print(f'Diferença: {diferenca}')