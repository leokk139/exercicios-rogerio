'''
5. Dado as listas A e B de tamanho 6 e do tipo float faça um programa em Python que, 
utilizando um laço de repetição, e, utilizando outro laço, inicialize os valores de ambas 
as listas, some os valores posição por posição e guarde o novo valor na lista A.
'''

lista_a = []
lista_b = []

for _ in range(6):
    valor = float(input('Digite um valor para adicionar à lista A: '))
    lista_a.append(valor)

print('---')

for _ in range(6):
    valor = float(input('Digite um valor para adicionar à lista B: '))
    lista_b.append(valor)

print('---')