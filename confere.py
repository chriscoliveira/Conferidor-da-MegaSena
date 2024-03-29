from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

class Loteria:
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
        print(resultados)
        # exibe os resultados
        for i in resultados:
            if jogo:
                if jogo.lower() in i.lower():
                    resultado = i,resultados[i]['numeros'],resultados[i]['acumulado'],resultados[i]['descricao']
                
        return resultado

    def conferente_resultados(planilha,resultados):
        
        mensagem = f'Numeros sorteados : {resultados}\n'
        
        # capura os numeros jogados
        planilha = pd.read_excel(planilha).replace(np.nan, '', regex=True)
        # print(planilha)
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
            # mensagem += f'Jogo {i[0]} - acertos {contador}\n'

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

        num_sen ,num_quin, num_quadr, num_tern='','','',''
        # try:
        # num_sen ,num_quin, num_quadr, num_tern='\n\t','\n\t','\n\t','\n\t'
        for y in num_sena.values():
            for xx in y:
                if not xx == '':
                    num_sen += f'{xx} '
            num_sen += '\n\t'
        for y in num_quina.values():
            for xx in y:
                if not xx == '':
                    num_quin += f'{xx} '
            num_quin += '\n\t'
        for y in num_quadra.values():
            for xx in y:
                if not xx == '\n':
                    num_quadr += f'{xx} '
            num_quadr += '\n\t'
        for y in num_terno.values():
            for xx in y:
                if not xx == '':
                    num_tern += f'{xx} '
            num_tern += '\n\t'
        # except Exception as e:
        #     mensagem = f'Erro ao processar planilha: {e}'    
        mensagem += f'\n\nNumeros Finais em {qtde_jogos} jogos' \
                f'\nSena: {sena}x {num_sen}\n' \
                f'Quina: {quina}x {num_quin}\n' \
                f'Quadra: {quadra}x {num_quadr}\n' \
                f'Terno: {terno}x {num_tern}\n' \
                f'Duque: {duque}x \n'
        
        return mensagem

# jogo,numeros,acumulado,descricao = procura_resultados('mega-sena')
# numeros = ['05', '15', '28', '32', '38', '54']
# conferente_resultados('jogos.xlsx',resultados=numeros)

