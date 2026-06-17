'''
5 - Uma empresa fez uma pesquisa de satisfação onde as notas possíveis eram apenas 1 
(Ruim), 2 (Bom) e 3 (Excelente). Crie uma lista longa simulando as respostas de 20 
clientes (ex: votos = [1, 2, 3, 2, 2, 1, 3, ...]). 
Cálculos exigidos: Crie uma lógica para contar quantas vezes cada nota aparece na 
lista. Em seguida, calcule o percentual que cada categoria representa em relação ao total 
de 20 votos. 
Saída: Imprima um relatório gerencial informando a quantidade absoluta de votos e a 
porcentagem para "Ruim", "Bom" e "Excelente". Indique também qual foi a avaliação 
vencedora (a que teve mais votos).
'''

notas = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2]
ruim = notas.count(1)
bom = notas.count(2)
excelente = notas.count(3)

print(f'Ruim = {ruim} ({ruim / 10 * 100})%') #multiplicar por 100
print(f'Bom = {bom} {bom / 10 * 100}%')
print(f'Excelente = {excelente} ({excelente / 10 * 10})%')

if bom < ruim > excelente:
    print('Vencedor = Ruim')
elif ruim < bom > excelente:
    print('Vencedor = Bom')
else:
    print('Vencedor = Excelente')