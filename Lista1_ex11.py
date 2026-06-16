'''
11. Elabore um algoritmo para fazer a conversão de graus fahrenheit  (º F) para 
graus celsius (º C). A fórmula para conversão é: c = 5/9 * (f-32)
'''

f = int(input('Digite a temperatura em graus Fahrenheint: '))
c = 5/9 * (f-32)

print(f'A conversão de {f} ºF para graus Celsius é de {int(c)} ºC.')