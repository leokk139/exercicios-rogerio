'''
3. Faça uma função que recebe um valor inteiro e verifica se o valor é 
positivo ou negativo. A função deve retornar um valor inteiro.  
'''

def positivo_negativo(n):
    if n > 0:
        return 'positivo'
    else:
        return 'negativo' #menos o zero

n = int(input('Digite um número: '))
print(positivo_negativo(n))