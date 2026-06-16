'''
4. Faça uma função que recebe um valor inteiro e verifica se o valor é 
par ou ímpar. A função deve retornar um valor inteiro. 
'''

def par_impar(n):
    if n % 2 == 0:
        return 'par'
    else:
        return '´impar'

n = int(input('Digite um número: '))
print(par_impar(n))