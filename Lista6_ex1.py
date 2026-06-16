'''
1. Faça um programa que carregue uma lista de seis elementos numéricos inteiros e 
mostre:

a. A quantidade de números pares; 
b. Quais são os números pares; 
c. A quantidade de números ímpares; 
d. Quais são os números ímpares. 
'''

lista = [0, 1, 2, 3, 4, 5]
pares = []
impares = []

for item in lista:
    if item == 0:
        pass
    if item % 2 == 0: #como não contar o 0 como par
        pares.append(item)
        # quantidade_pares += 1
    else:
        impares.append(item)

# for item in range(len(lista)):
#     if item % 2 == 0: #como não contar o 0 como par
#         pares.append(lista[item])
#     else:
#         impares.append(lista[item])

print(f'{len(pares)} pares na lista Pares.\nPares = {pares}')
print('---')
print(f'{len(impares)} ímpares na lista Ímpares.\nÍmpares = {impares}')