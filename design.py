# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(542, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 521, 590))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.ed_numeros = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.ed_numeros.setObjectName("ed_numeros")
        self.horizontalLayout.addWidget(self.ed_numeros)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_baixar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_baixar.setObjectName("bt_baixar")
        self.horizontalLayout_2.addWidget(self.bt_baixar)
        self.bt_confere = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_confere.setObjectName("bt_confere")
        self.horizontalLayout_2.addWidget(self.bt_confere)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.ed_status = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.ed_status.setObjectName("ed_status")
        self.verticalLayout.addWidget(self.ed_status)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Confere Loteria"))
        self.label.setText(_translate("MainWindow", "Confere Jogos Loteria"))
        self.label_2.setText(_translate("MainWindow", "Digite os numeros sorteados\n"
"separados por vírgula"))
        self.bt_baixar.setText(_translate("MainWindow", "Baixar Resultado"))
        self.bt_confere.setText(_translate("MainWindow", "Conferir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
