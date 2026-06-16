'''
8. Dados n e uma sequência de n números inteiros positivos, determinar a soma dos 
números pares, dos ímpares e as respectivas quantidades de cada um dos 
subconjuntos.
'''

n = int(input('Digite quantas vezes quer rodar o laço de repetição: '))
qtd_par = 0
qtd_impar = 0
soma_par = 0
soma_impar = 0

for _ in range(n):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        qtd_par += 1
        soma_par += num
        print(f'Par = {num} | Soma dos pares = {soma_par}')
    else:
        qtd_impar += 1
        soma_impar += num
        print(f'Ímpar = {num} | Soma dos ímpares = {soma_impar}')

print(f'Quantidade de pares = {qtd_par} | Soma dos pares = {soma_par}')
print(f'Quantidade de ímpares = {qtd_impar} | Soma dos ímpares = {soma_impar}')