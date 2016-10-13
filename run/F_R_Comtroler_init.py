# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from F_R_Comtroler import *

ctrl = F_R_Controler()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        Dialog.setAutoFillBackground(False)
        self.btBegin = QtWidgets.QPushButton(Dialog)
        self.btBegin.setGeometry(QtCore.QRect(0, 0, 250, 250))
        self.btBegin.setObjectName("btBegin")
        self.btBegin.clicked.connect(self.comecar)

        self.btMarcar = QtWidgets.QPushButton(Dialog)
        self.btMarcar.setGeometry(QtCore.QRect(250, 0, 250, 250))
        self.btMarcar.setObjectName("btMarcar")
        self.btMarcar.clicked.connect(self.marcar)


        self.btDesmarcar = QtWidgets.QPushButton(Dialog)
        self.btDesmarcar.setGeometry(QtCore.QRect(250, 250, 250, 250))
        self.btDesmarcar.setObjectName("btDesmarcar")
        self.btDesmarcar.clicked.connect(self.desmarcar)
        
        self.btStop = QtWidgets.QPushButton(Dialog)
        self.btStop.setGeometry(QtCore.QRect(0, 250, 250, 250))
        self.btStop.setObjectName("btStop")
        self.btStop.clicked.connect(self.fechar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "F.R.Controler"))
        self.btBegin.setText(_translate("Dialog", "Começar"))
        self.btStop.setText(_translate("Dialog", "Parar"))
        self.btMarcar.setText(_translate("Dialog", "Marcar"))
        self.btDesmarcar.setText(_translate("Dialog", "Desmarcar"))

    def fechar(self):
        sys.exit(app.closeAllWindows())
    def comecar(self):
        ctrl.main()
    def marcar(self):
        ctrl.comecar()
    def desmarcar(self):
        ctrl.parar()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

