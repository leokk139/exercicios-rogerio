'''
10. Encontre todos os números primos entre 2 e 20.000.
'''

for i in range(2, 20001):
    divisor = 0
    for j in range(2, i):
        if i % j == 0:
            divisor += 1
    if divisor == 0:
        print(i)