from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# from confere import Loteria



def conferente_resultados(planilha,resultados):
    mensagem = f'Numeros sorteados : {resultados}\n'
    
    # capura os numeros jogados
    planilha = pd.read_excel(planilha).replace(np.nan, '', regex=True)
    # print(planilha)
    planilha = planilha.values.tolist()
    resultados = resultados.replace('-',',').replace(' ',',').replace('.',',').split(',')
    
    qtde_jogos = len(planilha)
    um, duque, quina, quadra, terno, sena = 0, 0, 0, 0, 0, 0
    num_um, num_duque, num_quina, num_quadra, num_terno, num_sena = {}, {}, {}, {}, {}, {}
    # cria um array com os numeros jogados
    for i in planilha:
        contador = 0
        # verifica se o numero esta na lista de numeros sorteados
        for x in range(len(resultados)):
            if int(resultados[x]) in i:
                contador += 1
        # print(f'Jogo {i[0]} - acertos {contador}\n')

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
        elif contador == 1:
            um += 1

    num_sen ,num_quin, num_quadr, num_tern='\n\t','\n\t','\n\t','\n\t'
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
    mensagem += f'\n{"#"*60}\n\nNumeros Finais em {qtde_jogos} jogos' \
            f'\nSena: {sena}x {num_sen}\n' \
            f'Quina: {quina}x {num_quin}\n' \
            f'Quadra: {quadra}x {num_quadr}\n' \
            f'Terno: {terno}x {num_tern}\n' \
            f'2 acertos: {duque}x \n' \
            f'1 acerto: {um}x \n'

    if len(resultados) >= 3:
        print(mensagem)
        pass

sorteado = []


for x in range(6):
    numeros = input('Digite o numero sorteado ')
    sorteado.append(numeros)
    print(f'Numeros sorteados: {sorteado}')
    for y in range(len(sorteado)):
        pass
        #print(' '.join(sorteado))
    if len(sorteado) > 1:
        conferente_resultados('jogos.xlsx',' '.join(sorteado))
    
    if x == 5:
        continu = input('Pressione Qualquer tecla para sair')