'''
4. Dado uma lista A de tamanho 8 e do tipo inteiro faça um programa em Python que, 
utilizando um laço de repetição, receba os valores de entrada e, utilizando outro laço 
de repetição, verifique qual o maior valor da lista e apresente esse valor. 
'''

lista = []
maior = 0

for _ in range(8):
    valor = int(input('Digite um valor para adicionar à lista: '))
    lista.append(valor)

print(f'Lista = {lista}')

for item in lista:
    if item > maior:
        maior = item
        
print(f'Maior valor = {maior}')