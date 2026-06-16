'''
2. Faça um programa que carregue uma lista com oito números inteiros e mostre: 

a. Os números múltiplos de dois; 
b. Os números múltiplos de três; 
'''

lista = [1, 2, 3, 4, 5, 6, 7, 8]
mult2 = []
mult3 = []

for item in lista:
    if item % 2 == 0:
        mult2.append(item)
    if item % 3 == 0:
        mult3.append(item)

print(f'Múltiplos de 2: {mult2}\nMúltiplos de 3: {mult3}')