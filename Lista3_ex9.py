'''
9. Dado um inteiro positivo n, determinar o fatorial de n, que denotamos por n!.  
'''

n = int(input('Digite o número para o fatorial: '))
multi = 1

for i in range(1, n + 1):
    multi *= i

print(f'{n}! = {multi}')