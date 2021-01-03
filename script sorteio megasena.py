#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import csv
from bs4 import BeautifulSoup

'''
le o arquivo jogos.txt e cria uma lista para conferencia
'''
meus_numeros = []
numeros = 0

jogos = []

with open('jogos.txt', 'r') as arquivo:
    reader = csv.reader(arquivo)
    for linha in reader:
        jogos.append(linha)

#print(jogos)
quantidade_jogos = len(jogos)

'''
procura os numeros do ultimo sorteio da mega sena  
'''
print('\n\nAguarde enquanto procuro o ultimo resultado...\n\n')

response = requests.get('https://www.sorteonline.com.br/mega-sena/resultados')
soup = BeautifulSoup(response.text, 'html.parser')
print("\n======[ RESULTADO MEGA SENA: ]======")

for div in soup.find_all(class_='result result-default center'):
    lista = div.text.replace('<li class=bg>', ',')

valores = []
ul = soup.find_all('li', {'class': 'bg'})
for indice, li in enumerate(ul):
    if indice < 6:
        numero = str(li)
        numero = numero.replace('<li class="bg">', '')
        numero = numero.replace('</li>', '')
        valores.append(numero)

print('Numeros sorteados ' + str(valores) + '\n\n')
for valor in valores:
    texto = str(valor)
    texto = texto.replace('<li class="bg">', '')
    texto = texto.replace('</li>', '')


'''
confere se houve acerto e notifica
'''
J, sena ,quina,quadra,terno,duque,uno,zero =0,0,0,0,0,0,0,0
while J < quantidade_jogos:
    final = [x for x in valores if x not in jogos[J]]
    acertos = 6 - len(final)
    # print('Voce acertou '+str(acertos)+' numeros')
    if acertos == 6:
        print('Parabens você ganhou a Mega Sena!\n\n')
        sena=sena+1
    elif acertos == 5:
        print('Parabens você ganhou a Quina!\n\n')
        quina=quina+1
    elif acertos == 4:
        print('Parabens você ganhou a Quadra!\n\n')
        quadra=quadra+1
    elif acertos == 3:
        terno=terno+1
    elif acertos == 2:
        duque=duque+1
    elif acertos == 1:
        uno=uno+1
    elif acertos == 0:
        zero=zero+1
    J = J + 1

print(f'Total de jogos feitos {quantidade_jogos}\n'
      f'jogos com 6 acertos: {sena}\n'
      f'jogos com 5 acertos: {quina}\n'
      f'jogos com 4 acertos: {quadra}\n'
      f'jogos com 3 acertos: {terno}\n'
      f'jogos com 2 acertos: {duque}\n'
      f'jogos com 1 acertos: {uno}\n'
      f'jogos com 0 acertos: {zero}')