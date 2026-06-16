'''
8. Faça um algoritmo que leia o ano de nascimento de uma pessoa e imprima a 
idade dela. Assuma que a pessoa já tenha feito aniversário esse ano.
'''

ano_nasc = int(input('Digite o ano que você nasceu: '))
ano_atual = 2026

idade = 2026 - ano_nasc

print(f'Se você nasceu em {ano_nasc}, então você tem {idade} anos de idade.')