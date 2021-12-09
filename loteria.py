from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


def remove_tags(text):
    try:
        text = text.replace('\n', '')
        text = text.replace('\t', '')
        text = text.replace('\r', '')
    except Exception as e :
        #print('Erro ao remover tags',e)
        pass

    return text

def procura_resultados(jogo=None):

    URL = 'http://www.loterias.caixa.gov.br/wps/portal/loterias'

    headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    r = requests.get(URL, headers=headers).text
    soup = BeautifulSoup(r, 'html.parser')
    loterias = soup.find_all('div', {'class': 'products'})
    tipos = soup.find_all('div', {'class': 'product'})

    resultados = {}

    for tipo in tipos:
        try:
            nome = tipo.find('h3', class_='nome-loteria').text
            acumulado = tipo.find('h3', class_='zeta').text
            descricao = tipo.find('p', class_='description').text
            numeros = tipo.find('ul')
            num_list = []
            for numero in numeros:
                if not numero == '\n':
                    num_list.append(remove_tags(numero.text))
            acumulado = remove_tags(acumulado)
            descricao = remove_tags(descricao)
            resultados[nome] = {'acumulado': acumulado, 'descricao': descricao, 'numeros': num_list}
            
        except Exception as e:
            pass

    # exibe os resultados
    for i in resultados:
        if jogo:
            if jogo.lower() in i.lower():
                resultado = i,resultados[i]['numeros'],resultados[i]['acumulado'],resultados[i]['descricao']
            
    return resultado

def conferente_resultados(planilha,resultados):
    print(f'Numeros sorteados : {resultados}')
    
    # capura os numeros jogados
    planilha = pd.read_excel(planilha).notna()
    print(planilha)
    planilha = planilha.values.tolist()
    qtde_jogos = len(planilha)
    duque, quina, quadra, terno, sena = 0, 0, 0, 0, 0
    num_duque, num_quina, num_quadra, num_terno, num_sena = {}, {}, {}, {}, {}
    # cria um array com os numeros jogados
    for i in planilha:
        contador = 0
        # verifica se o numero esta na lista de numeros sorteados
        for x in range(len(resultados)):
            if int(resultados[x]) in i:
                contador += 1
        print(f'Jogo {i[0]} - acertos {contador}')

        if contador == 6:
            sena += 1
            num_sena[sena] = i
        elif contador == 5:
            quina += 1
            num_quina[quina] = i
        elif contador == 4:
            quadra += 1
            num_quadra[quadra] = i
        elif contador == 3:
            terno += 1
            num_terno[terno] = i
        elif contador == 2:
            duque += 1


    print(f'\n{"*"*20}\nNumeros Finais em {qtde_jogos} jogos' \
            f'\nSena: {sena}x {num_sena}\n' \
            f'Quina: {quina}x {num_quina}\n' \
            f'Quadra: {quadra}x {num_quadra}\n' \
            f'Terno: {terno}x {num_terno}\n' \
            f'Duque: {duque}x \n')


jogo,numeros,acumulado,descricao = procura_resultados('mega-sena')

conferente_resultados('jogos.xlsx',resultados=numeros)