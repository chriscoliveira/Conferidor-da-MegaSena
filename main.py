 
import sys
from threading import Thread

from PyQt5.QtWidgets import QMainWindow, QApplication
from confere import Loteria
from design import *

class Funcao(Thread):
    # declarar as variaveis que terão interação da funcao com a interface UI
    def __init__(self, label,edit):
        # variaveis que herdam os componentes
        self.status = label
        self.numeros = edit
        super().__init__()

    def run(self):
        numeros_sorteados = self.numeros.text().split(',')
        numeros_sorteados = [int(i) for i in numeros_sorteados]
        print(numeros_sorteados)
        retorno = Loteria.conferente_resultados('jogos.xlsx',numeros_sorteados)
        self.status.setPlainText(retorno)
        # print(retorno)


# classe que trabalha diretamente com o design UI do pyqt
class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        btn = self.bt_confere.clicked.connect(self.executar)
        atz = self.bt_baixar.clicked.connect(self.atz)

    def executar(self):
        t = Funcao(label=self.ed_status, edit=self.ed_numeros)
        retorno = t.start()
    
    def atz(self):
        numeros = Loteria.procura_resultados('mega-sena')
        self.ed_numeros.setText(numeros)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    novo.ed_numeros.setText('5,15,28,32,38,54')
    qt.exec_()
