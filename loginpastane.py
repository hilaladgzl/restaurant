# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpastane.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from kayit import Ui_kayit
from menupstane import Ui_menu



class Ui_login(object):

    def loginchek(self):
        kullaniciadi = self.textEdit.toPlainText()
        sifre = self.textEdit_2.toPlainText()

        conn = sqlite3.connect('Our_data.db')
        result = conn.execute(''' SELECT * FROM kullanicilar WHERE kullanıcıAdı=? AND sifre=?''', (kullaniciadi, sifre))

        if (len(result.fetchall()) > 0):
            print('user found')

            self.menu = QtWidgets.QMainWindow()
            self.ui = Ui_menu()
            self.ui.setupUi(self.menu)
            self.menu.show()
        else:
            result2 = QMessageBox.warning(login, 'Message', 'user not found')
            login.show()
            print('user not found')


    def kayitcheck(self):
        self.kayit = QtWidgets.QMainWindow()
        self.ui = Ui_kayit()
        self.ui.setupUi(self.kayit)
        self.kayit.show()

    def menucheck(self):
        self.menu = QtWidgets.QMainWindow()
        self.ui = Ui_menu()
        self.ui.setupUi(self.menu)
        self.menu.show()

    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(1255, 1024)
        login.setStyleSheet("\n"
"background-image: url(waffle.jpg);")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(110, 190, 301, 41))
        self.label.setStyleSheet("QLabel{\n"
"    font: 20pt \"Lucida Handwriting\";\n"
"}")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(login)
        self.textEdit.setGeometry(QtCore.QRect(440, 190, 291, 51))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"background-color :white; color rgb(180, 167, 255); border:3px solid black;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(login)
        self.textEdit_2.setGeometry(QtCore.QRect(440, 290, 291, 51))
        self.textEdit_2.setStyleSheet("QTextEdit{background-color :white; color rgb(180, 167, 255); border:3px solid black;\n"
"}")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(120, 300, 211, 41))
        self.label_2.setStyleSheet("QLabel{\n"
"    font: 20pt \"Lucida Handwriting\";\n"
"}")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(login)
        self.pushButton.setGeometry(QtCore.QRect(580, 400, 121, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"font: 75 11pt \"Segoe Print\";\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"\n"
"background: #ffffff;\n"
"padding: 10px;\n"
"border: 4px solid #494949 !important;\n"
"display: inline-block;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"QPushButton:hover {\n"
"color: #ffffff !important;\n"
"background-color:rgb(255, 97, 49);\n"
"border-color: #f6b93b !important;\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(login)
        self.pushButton.clicked.connect(self.loginchek)  # buton action
        self.pushButton_2.clicked.connect(self.kayitcheck)
        self.pushButton_2.setGeometry(QtCore.QRect(760, 400, 121, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"font: 75 11pt \"Segoe Print\";\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"\n"
"background: #ffffff;\n"
"padding: 10px;\n"
"border: 4px solid #494949 !important;\n"
"display: inline-block;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"QPushButton:hover {\n"
"color: #ffffff !important;\n"
"background-color:rgb(255, 97, 49);\n"
"border-color: #f6b93b !important;\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(login)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 240, 201, 51))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background:rgb(157, 206, 205);\n"
"font: 75 11pt \"Segoe Print\";\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"padding: 10px;\n"
"border: 4px solid #494949 !important;\n"
"display: inline-block;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"QPushButton:hover {\n"
"color: #ffffff !important;\n"
"background-color: rgb(66, 127, 145);\n"
"border-color: rgb(66, 86, 103);\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"\n"
"")


        self.textEdit.setPlaceholderText('Please enter your username')



        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.menucheck)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.label.setText(_translate("login", "Kullanıcı Adı :"))
        self.textEdit.setHtml(_translate("login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("login", "Şifre :"))
        self.pushButton.setText(_translate("login", "LOGIN"))
        self.pushButton_2.setText(_translate("login", "KAYIT"))
        self.pushButton_3.setText(_translate("login", "Menü"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
