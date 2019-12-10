from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from pythonproje.kayit import Ui_kayit
from pythonproje.menupstane import Ui_menu


class Ui_admin(object):
    def menucheck(self):
        self.menu = QtWidgets.QMainWindow()
        self.ui = Ui_menu()
        self.ui.setupUi(self.menu)
        self.menu.show()

    def uyelist(self):
        self.connection = sqlite3.connect("Our_data.db")
        query = "SELECT * FROM kullanicilar"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()


    def pastalist(self):
        self.connection = sqlite3.connect("Our_data.db")
        query = "SELECT * FROM pastalar"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()


    def serbetlist(self):
            self.connection = sqlite3.connect("Our_data.db")
            query = "SELECT * FROM serbetliler"
            result = self.connection.execute(query)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.connection.close()

    def sutlulist(self):
            self.connection = sqlite3.connect("Our_data.db")
            query = "SELECT * FROM sutluler"
            result = self.connection.execute(query)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.connection.close()

    def iceceklist(self):
            self.connection = sqlite3.connect("Our_data.db")
            query = "SELECT * FROM icecekler"
            result = self.connection.execute(query)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.connection.close()

    def delete(self):
        conn = sqlite3.connect('Our_data.db')
        curs = conn.cursor()
        content = 'SELECT *FROM kullanicilar'
        res = curs.execute(content)
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                id = data[0]
                email = data[1]
                curs.execute('''DELETE FROM kullanicilar WHERE id=? AND email=?''', (id, email,))
                conn.commit()
        result = QMessageBox.warning(admin, 'Message', 'Deleted User!')


    def kayit(self):
        self.kayit = QtWidgets.QMainWindow()
        self.ui = Ui_kayit()
        self.ui.setupUi(self.kayit)
        self.kayit.show()


    def setupUi(self, admin):
        admin.setObjectName("admin")
        admin.setEnabled(True)
        admin.resize(928, 769)
        #admin.setStyleSheet("background-image: url(arka.jpg);")
        self.pushButton = QtWidgets.QPushButton(admin)
        self.pushButton.clicked.connect(self.uyelist)
        self.pushButton.setGeometry(QtCore.QRect(30, 100, 161, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"font: 75 10pt \"OCR A Extended\";\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"\n"
"background: #ffffff;\n"
"padding: 10px;\n"
"border: 2px solid #494949 !important;\n"
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
        self.pushButton_3 = QtWidgets.QPushButton(admin)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 100, 161, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"font: 75 10pt \"OCR A Extended\";\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"\n"
"background: #ffffff;\n"
"padding: 10px;\n"
"border: 2px solid #494949 !important;\n"
"display: inline-block;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"QPushButton:hover {\n"
"color: #ffffff !important;\n"
"background: #663366;\n"
"border-color: #D0D0D0 !important;\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(admin)
        self.pushButton_4.clicked.connect(self.menucheck)
        self.pushButton_4.setGeometry(QtCore.QRect(710, 100, 161, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"font: 75 10pt \"OCR A Extended\";\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"\n"
"background: #ffffff;\n"
"padding: 10px;\n"
"border: 2px solid #494949 !important;\n"
"display: inline-block;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"QPushButton:hover {\n"
"color: #ffffff !important;\n"
"background: #663366;\n"
"border-color: #D0D0D0 !important;\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(admin)
        self.pushButton_5.clicked.connect(self.delete)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 100, 161, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"font: 75 10pt \"OCR A Extended\";\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"\n"
"background: #ffffff;\n"
"padding: 7px;\n"
"border: 2px solid #494949 !important;\n"
"display: inline-block;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"QPushButton:hover {\n"
"color: #ffffff !important;\n"
"background: #663366;\n"
"border-color: #D0D0D0 !important;\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(admin)
        self.pushButton_2.clicked.connect(self.kayit)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 100, 161, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"font: 75 10pt \"OCR A Extended\";\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"\n"
"background: #ffffff;\n"
"padding: 7px;\n"
"border: 2px solid #494949 !important;\n"
"display: inline-block;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"QPushButton:hover {\n"
"color: #ffffff !important;\n"
"background: #663366;\n"
"border-color: #D0D0D0 !important;\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(admin)
        self.pushButton_6.clicked.connect(self.sutlulist)
        self.pushButton_6.setGeometry(QtCore.QRect(510, 160, 91, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"font: 75 9pt \"OCR A Extended\";\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"\n"
"background: #ffffff;\n"
"padding: 7px;\n"
"border: 2px solid #494949 !important;\n"
"display: inline-block;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"QPushButton:hover {\n"
"color: #ffffff !important;\n"
"background: #663366;\n"
"border-color: #D0D0D0 !important;\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(admin)
        self.pushButton_7.clicked.connect(self.serbetlist)
        self.pushButton_7.setGeometry(QtCore.QRect(620, 160, 111, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"font: 75 9pt \"OCR A Extended\";\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"\n"
"background: #ffffff;\n"
"padding: 6px;\n"
"border: 2px solid #494949 !important;\n"
"display: inline-block;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"QPushButton:hover {\n"
"color: #ffffff !important;\n"
"background: #663366;\n"
"border-color: #D0D0D0 !important;\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(admin)
        self.pushButton_8.clicked.connect(self.iceceklist)
        self.pushButton_8.setGeometry(QtCore.QRect(740, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"font: 75 9pt \"OCR A Extended\";\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"\n"
"background: #ffffff;\n"
"padding: 7px;\n"
"border: 2px solid #494949 !important;\n"
"display: inline-block;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"QPushButton:hover {\n"
"color: #ffffff !important;\n"
"background: #663366;\n"
"border-color: #D0D0D0 !important;\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(admin)
        self.pushButton_9.clicked.connect(self.pastalist)
        self.pushButton_9.setGeometry(QtCore.QRect(400, 160, 91, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"font: 75 9pt \"OCR A Extended\";\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"\n"
"background: #ffffff;\n"
"padding: 7px;\n"
"border: 2px solid #494949 !important;\n"
"display: inline-block;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"QPushButton:hover {\n"
"color: #ffffff !important;\n"
"background: #663366;\n"
"border-color: #D0D0D0 !important;\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.tableWidget = QtWidgets.QTableWidget(admin)
        self.tableWidget.setGeometry(QtCore.QRect(50, 250, 811, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item=QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0,item)
        item=QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1,item)
        item=QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.retranslateUi(admin)
        QtCore.QMetaObject.connectSlotsByName(admin)

    def retranslateUi(self, admin):
        _translate = QtCore.QCoreApplication.translate
        admin.setWindowTitle(_translate("admin", "Form"))
        self.pushButton.setText(_translate("admin", "Admin Listele"))
        self.pushButton_3.setText(_translate("admin", "Spariş Listele"))
        self.pushButton_4.setText(_translate("admin", "Menüyü Gör"))
        self.pushButton_5.setText(_translate("admin", "Admin Sil"))
        self.pushButton_2.setText(_translate("admin", "Admin Ekle"))
        self.pushButton_6.setText(_translate("admin", "Sütlüler"))
        self.pushButton_7.setText(_translate("admin", "Şerbetliler"))
        self.pushButton_8.setText(_translate("admin", "içecekler"))
        self.pushButton_9.setText(_translate("admin", "Pastalar"))

        self.tableWidget.doubleClicked.connect(self.tiklanmisSatir)

        item=self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("admin","id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("admin", "email"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("admin", "isim"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("admin", "soyisim"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("admin", "telefon"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("admin", "kullanıcıAdı"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("admin", "sifre"))


    def tiklanmisSatir(self):
        print("Table clicked")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin = QtWidgets.QWidget()
    ui = Ui_admin()
    ui.setupUi(admin)
    admin.show()
    sys.exit(app.exec_())
