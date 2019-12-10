from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from PyQt5.QtWidgets import QMessageBox


class Ui_kayit(object):
    def add(self,kayit):
        id=self.textEdit_7.toPlainText()
        isim = self.textEdit.toPlainText()
        soyisim = self.textEdit_2.toPlainText()
        telefon = self.textEdit_3.toPlainText()
        email = self.textEdit_4.toPlainText()
        kullaniciadi = self.textEdit_5.toPlainText()
        sifre = self.textEdit_6.toPlainText()
        conn = sqlite3.connect('Our_data.db')
        conn.execute('''INSERT INTO kullanicilar (id, isim,  soyisim, telefon, email, kullanıcıAdı, sifre) VALUES (?,?,?,?,?,?,?)''',
                     (id,isim, soyisim, telefon, email, kullaniciadi, sifre))
        result = QMessageBox.warning(kayit, 'Message', 'Added User!')
        kayit.show()
        conn.commit()


    def setupUi(self, kayit):
        kayit.setObjectName("kayit")
        kayit.resize(1142, 1027)
        kayit.setStyleSheet("background-image: url(waffle.jpg);")
        self.label = QtWidgets.QLabel(kayit)
        self.label.setGeometry(QtCore.QRect(140, 170, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(kayit)
        self.label_2.setGeometry(QtCore.QRect(140, 240, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(kayit)
        self.label_4.setGeometry(QtCore.QRect(140, 300, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(kayit)
        self.label_5.setGeometry(QtCore.QRect(140, 350, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(kayit)
        self.textEdit.setGeometry(QtCore.QRect(340, 160, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(kayit)
        self.textEdit_2.setGeometry(QtCore.QRect(340, 220, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(kayit)
        self.textEdit_3.setGeometry(QtCore.QRect(340, 280, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(kayit)
        self.textEdit_4.setGeometry(QtCore.QRect(340, 340, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton = QtWidgets.QPushButton(kayit)
        self.pushButton.clicked.connect(lambda : self.add(kayit))  # buton action
        self.pushButton.setGeometry(QtCore.QRect(620, 630, 151, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
"font: 75 11pt \"OCR A Extended\";\n"
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
"background: #663366;\n"
"border-color: #D0D0D0 !important;\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.textEdit_5 = QtWidgets.QTextEdit(kayit)
        self.textEdit_5.setGeometry(QtCore.QRect(340, 400, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_7 = QtWidgets.QLabel(kayit)
        self.label_7.setGeometry(QtCore.QRect(140, 410, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit_6 = QtWidgets.QTextEdit(kayit)
        self.textEdit_6.setGeometry(QtCore.QRect(340, 460, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_8 = QtWidgets.QLabel(kayit)
        self.label_8.setGeometry(QtCore.QRect(140, 470, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(kayit)
        self.label_3.setGeometry(QtCore.QRect(140, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_7 = QtWidgets.QTextEdit(kayit)
        self.textEdit_7.setGeometry(QtCore.QRect(340, 100, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_7.setFont(font)
        self.textEdit_7.setObjectName("textEdit_7")

        self.retranslateUi(kayit)
        QtCore.QMetaObject.connectSlotsByName(kayit)

    def retranslateUi(self, kayit):
        _translate = QtCore.QCoreApplication.translate
        kayit.setWindowTitle(_translate("kayit", "Form"))
        self.label.setText(_translate("kayit", "İsim:"))
        self.label_2.setText(_translate("kayit", "Soyisim:"))
        self.label_4.setText(_translate("kayit", "Telefon:"))
        self.label_5.setText(_translate("kayit", "E-mail:"))
        self.pushButton.setText(_translate("kayit", "Kayıt"))
        self.label_7.setText(_translate("kayit", "Kullanıcı Adı:"))
        self.label_8.setText(_translate("kayit", "Şifre:"))
        self.label_3.setText(_translate("kayit", "ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kayit = QtWidgets.QWidget()
    ui = Ui_kayit()
    ui.setupUi(kayit)
    kayit.show()
    sys.exit(app.exec_())
