'''
7. Escreva um algoritmo para ler um valor e escrever a mensagem “É PAR!” se o 
valor lido for par, ou escrever “É ÍMPAR!” caso contrário. 
'''

try:
    n = int(input('Digite um valor inteiro: '))

except ValueError:
    print('\n> Digite somente números inteiros.\n')

else:
    if n % 2 == 0:
        print('\n> É par!\n')

    else:
        print('\n> É ímpar!\n')