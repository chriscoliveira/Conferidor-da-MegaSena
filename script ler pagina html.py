#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

meus_numeros=[]
numeros=0
while numeros < 6:
    numeros +=1
    meus_numeros.append(int(input('Digite o '+str(numeros)+' jogado: ')))
print(meus_numeros)
print('\n\nAguarde enquanto procuro o ultimo resultado...\n\n')

response = requests.get('https://www.sorteonline.com.br/mega-sena/resultados')
soup = BeautifulSoup(response.text, 'html.parser')
print ("\n======[ RESULTADO MEGA SENA: ]======")


for div in soup.find_all(class_='result result-default center'):
    lista = div.text.replace('<li class=bg>',',')

valores = []
ul = soup.find_all('li',{'class': 'bg'})
for indice, li in enumerate(ul):
    if indice < 6:
        numero=str(li)
        numero = numero.replace('<li class="bg">','')
        numero = numero.replace('</li>','')
        valores.append(int(numero))


print('Numeros sorteados '+str(valores)+'\n\n')
for valor in valores:
    texto=str(valor)
    texto = texto.replace('<li class="bg">','')
    texto = texto.replace('</li>','')



final = [x for x in valores if x not in meus_numeros]
acertos=6-len(final)
print('Voce acertou '+str(acertos)+' numeros')

if acertos == 6:
    print('Parabens você ganhou a Mega Sena!')
elif acertos == 5:
    print('Parabens você ganhou a Quina!')
elif acertos == 4:
    print('Parabens você ganhou a Quadra!')
else:
    print('Dessa vez nao deu... :(')