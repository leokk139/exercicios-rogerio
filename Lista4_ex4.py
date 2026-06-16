'''
4. Faça um procedimento que recebe por parâmetro os valores necessários para o 
cálculo da fórmula de báskara e imprima as suas raízes, caso seja possível calcular.
'''

# tem que saber a fórmula

def baskara(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print('Não tem raíz')
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print(f'x1 = {x1} | x2 = {x2}')

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

baskara(a, b, c)