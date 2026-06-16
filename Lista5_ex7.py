'''
7. Faça um algoritmo para ler um número até que o usuário opte por 
terminar a entrada dos dados e, mostre na tela as seguintes 
informações: a média dos números, o maior e o menor número.
'''

soma = 0
qtd = 0
maior = 0
menor = 0

while True:
    num = float(input('Digite um número (0 pra sair): '))
    if num == 0:
        break
    soma += num
    qtd += 1
    if maior == 0 or num > maior:
        maior = num
    if menor == 0 or num < menor:
        menor = num

media = soma / qtd

print(f'Média: {media}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')