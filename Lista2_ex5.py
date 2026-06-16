'''
5. Faça um algoritmo que leia 5 números e imprima quantos números maiores que 
100 foram digitados.
'''

try:
    contador = 0

    n1 = float(input('Digite o primeiro número: '))
    if n1 > 100:
        contador += 1

    n2 = float(input('Digite o segundo número: '))
    if n2 > 100:
        contador += 1

    n3 = float(input('Digite o terceiro número: '))
    if n3 > 100:
        contador += 1

    n4 = float(input('Digite o quarto número: '))
    if n4 > 100:
        contador += 1

    n5 = float(input('Digite o quinto número: '))
    if n5 > 100:
        contador += 1

except ValueError:
    print('\n> Preencha somente com números.\n')

else:
    print(f'\n> {contador} número(s) são maiores que 100.\n')