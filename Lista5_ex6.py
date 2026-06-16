'''
6. Faça uma função que recebe por parâmetro o tempo de duração de 
uma fábrica expressa em segundos e imprima esse tempo em horas, 
minutos e segundos. 
'''

def tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    seg = (segundos % 3600) % 60
    print(f'{horas}:{minutos}:{seg}')

segundos = int(input('Digite o horário em segundos: '))
tempo(segundos)