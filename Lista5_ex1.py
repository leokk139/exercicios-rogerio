'''
1. Crie um programa que exiba um menu interativo para o usuário com 
opções de conversão de medidas.  
O programa deve rodar continuamente até que o usuário escolha a 
opção de sair. 
O menu deve ter 3 opções: Converter Celsius para Fahrenheit, 
Converter Metros para Centímetros e Sair. 
Crie uma função específica para cada cálculo de conversão. 
Se o usuário digitar uma opção que não existe, o programa deve 
avisar que a opção é inválida e mostrar o menu novamente. 
'''

def celsius_fahrenheit(c):
    return c * 9/5 + 32

def metros_cm(m):
    return m * 100

while True:
    print('1 - Celsius pra Fahrenheit')
    print('2 - Metros pra Centímetros')
    print('3 - Sair')
    opcao = int(input('Escolha uma opção: '))
    match opcao: #match pra escolhas tipo cardapio
        case 1:
            c = float(input('Digite a temperatura em Celsius: '))
            print(f'{c}°C = {celsius_fahrenheit(c)}°F')
        case 2:
            m = float(input('Digite o valor em metros: '))
            print(f'{m}m = {metros_cm(m)}cm')
        case 3:
            print('Saindo.')
            break
        case _:
            print('Opção inválida.')