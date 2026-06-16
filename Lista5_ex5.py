'''
5. Faça uma função que receba 3 valores inteiros por parâmetro e 
imprima-os ordenados em ordem crescente. 
'''

def ordenar(a, b, c):
    if a <= b <= c:
        print(a, b, c)
    elif a <= c <= b:
        print(a, c, b)
    elif b <= a <= c:
        print(b, a, c)
    elif b <= c <= a:
        print(b, c, a)
    elif c <= a <= b:
        print(c, a, b)
    else:
        print(c, b, a)#3 números só tem 6 ordens possíveis

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o primeiro número: '))
c = int(input('Digite o primeiro número: '))

ordenar(a, b, c)