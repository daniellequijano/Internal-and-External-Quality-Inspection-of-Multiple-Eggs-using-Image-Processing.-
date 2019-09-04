# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from OtherWindow import Ui_OtherWindow
from gtts import gTTS
from pygame import mixer


import sys
mixer.init()
mixer.music.load("trainedvoice_dataset/opening.mp3")
mixer.music.play()


def db():
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
    c.execute("create table if not exists users(name TEXT NOT NULL,age INT NOT NULL,username TEXT NOT NULL,password TEXT NOT NULL, gender TEXT NOT NULL)")
    db.commit()
    c.close()
    db.close()
    
db()


class Ui_MainWindow(object):


        
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 512)
        MainWindow.setMinimumSize(QtCore.QSize(622, 512))
        MainWindow.setMaximumSize(QtCore.QSize(622, 512))
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(50, 10, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK SC")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(0, 0, 128);")
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget.setGeometry(QtCore.QRect(0, 80, 621, 431))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.accTab = QtWidgets.QWidget()
        self.accTab.setObjectName("accTab")
        self.label_2 = QtWidgets.QLabel(self.accTab)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK SC")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.firstname = QtWidgets.QLineEdit(self.accTab)
        self.firstname.setGeometry(QtCore.QRect(100, 70, 201, 41))
        self.firstname.setStyleSheet("font: 14pt \".SF NS Text\";\n"
"")
        self.firstname.setObjectName("firstname")
        self.lastname = QtWidgets.QLineEdit(self.accTab)
        self.lastname.setGeometry(QtCore.QRect(320, 70, 191, 41))
        self.lastname.setStyleSheet("\n"
"border-color: rgb(25, 25, 25);")
        self.lastname.setObjectName("lastname")
        self.cr_username = QtWidgets.QLineEdit(self.accTab)
        self.cr_username.setGeometry(QtCore.QRect(100, 130, 351, 41))
        self.cr_username.setObjectName("cr_username")
        self.cr_password = QtWidgets.QLineEdit(self.accTab)
        self.cr_password.setGeometry(QtCore.QRect(100, 180, 351, 41))
        self.cr_password.setText("")
        self.cr_password.setObjectName("cr_password")
        self.cr_age = QtWidgets.QLineEdit(self.accTab)
        #self.cr_age.setGeometry(QtCore.QRect(100, 240, 101, 31))
        self.cr_age.setGeometry(QtCore.QRect(0, 0, 0, 0))

        self.cr_age.setMaxLength(2)
        self.cr_age.setObjectName("cr_age")
        self.male_radio = QtWidgets.QRadioButton(self.accTab)
        #self.male_radio.setGeometry(QtCore.QRect(310, 240, 115, 31))
        self.male_radio.setGeometry(QtCore.QRect(0, 0, 0, 0))

        self.male_radio.setObjectName("male_radio")
        self.female_radio = QtWidgets.QRadioButton(self.accTab)
       # self.female_radio.setGeometry(QtCore.QRect(410, 240, 115, 31))
        self.female_radio.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.female_radio.setObjectName("female_radio")
        self.label_4 = QtWidgets.QLabel(self.accTab)
        self.label_4.setGeometry(QtCore.QRect(220, 240, 81, 31))
        self.label_4.setObjectName("label_4")
        self.createAccount = QtWidgets.QPushButton(self.accTab)
        self.createAccount.setGeometry(QtCore.QRect(100, 300, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.createAccount.setFont(font)
        self.createAccount.setObjectName("createAccount")
        self.cr_clear = QtWidgets.QPushButton(self.accTab)
        self.cr_clear.setGeometry(QtCore.QRect(350, 300, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.cr_clear.setFont(font)
        self.cr_clear.setObjectName("cr_clear")
        self.label_3 = QtWidgets.QLabel(self.accTab)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 571, 371))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix/dozen-white-eggs-wallpaper-3.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label_2.raise_()
        self.firstname.raise_()
        self.lastname.raise_()
        self.cr_username.raise_()
        self.cr_password.raise_()
        self.cr_age.raise_()
        self.male_radio.raise_()
        self.female_radio.raise_()
        self.label_4.raise_()
        self.createAccount.raise_()
        self.cr_clear.raise_()
        self.tabWidget.addTab(self.accTab, "")
        self.log = QtWidgets.QWidget()
        self.log.setObjectName("log")
        self.log_username = QtWidgets.QLineEdit(self.log)
        self.log_username.setGeometry(QtCore.QRect(110, 190, 401, 51))
        self.log_username.setObjectName("log_username")
        self.log_password = QtWidgets.QLineEdit(self.log)
        self.log_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.log_password.setGeometry(QtCore.QRect(110, 260, 401, 51))
        self.log_password.setObjectName("log_password")
        self.log_in = QtWidgets.QPushButton(self.log)
        self.log_in.setGeometry(QtCore.QRect(80, 330, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.log_in.setFont(font)
        self.log_in.setObjectName("log_in")
        self.log_clear = QtWidgets.QPushButton(self.log)
        self.log_clear.setGeometry(QtCore.QRect(340, 330, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.log_clear.setFont(font)
        self.log_clear.setObjectName("log_clear")
        self.icon = QtWidgets.QLabel(self.log)
        self.icon.setGeometry(QtCore.QRect(210, 0, 191, 181))
        self.icon.setStyleSheet("image: url(:/newPrefix/logo.jpg);")
        self.icon.setText("")
        self.icon.setObjectName("icon")
        self.label_5 = QtWidgets.QLabel(self.log)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 571, 371))
        self.label_5.setStyleSheet("background-image: url(:/newPrefix/dozen-white-eggs-wallpaper-3.jpg);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.log_username.raise_()
        self.log_password.raise_()
        self.log_in.raise_()
        self.log_clear.raise_()
        self.icon.raise_()
        self.tabWidget.addTab(self.log, "")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login and Register Form - EggIE(2019ver1.0) Created by: Danielle Mark O. Quijano"))
        self.label.setText(_translate("MainWindow", "Internal and External Egg Detection System"))
        self.label_2.setText(_translate("MainWindow", "Create Account "))
        self.firstname.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.lastname.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.cr_username.setPlaceholderText(_translate("MainWindow", "Type a username..."))
        self.cr_password.setPlaceholderText(_translate("MainWindow", "Type a password..."))
       # self.cr_age.setPlaceholderText(_translate("MainWindow", "Age...."))
       # self.male_radio.setText(_translate("MainWindow", "Male"))
        #self.female_radio.setText(_translate("MainWindow", "Female"))
        #self.label_4.setText(_translate("MainWindow", "Gender: "))
        self.createAccount.setText(_translate("MainWindow", "Create Account"))
        self.cr_clear.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.accTab), _translate("MainWindow", "Create Account"))
        self.log_username.setPlaceholderText(_translate("MainWindow", "Type username here ...."))
        self.log_password.setPlaceholderText(_translate("MainWindow", "Type password here ...."))
        self.log_in.setText(_translate("MainWindow", "Log In"))
        self.log_clear.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log), _translate("MainWindow", "Log In"))
        ##########CLICKING#############
        self.cr_clear.clicked.connect(self.clear1)
        self.log_clear.clicked.connect(self.clear2)
        self.createAccount.clicked.connect(self.create_account)
        self.log_in.clicked.connect(self.login)
        ################################


    def clear1(self):
        self.firstname.setText('')
        self.lastname.setText('')
        self.cr_username.setText('')
        self.cr_password.setText('')
        self.cr_age.setText('')
        mixer.init()
        mixer.music.load("trainedvoice_dataset/Clear.mp3")
        mixer.music.play()

    def clear2(self):
        self.log_username.setText('')
        self.log_password.setText('')
        mixer.init()
        mixer.music.load("trainedvoice_dataset/Clearlog.mp3")
        mixer.music.play()

    def login(self):
        
        with sqlite3.connect('users.db') as db:
            c = db.cursor()
            
        username = str(self.log_username.text())
        password = str(self.log_password.text())

        c.execute('SELECT * FROM users WHERE username = ? and password = ?',(username,password))
        data = c.fetchone()
        db.commit()
        if data != None:
            info = '''
                Name = %s ,

                Age = %s,

                Gender = %s,

                Username = %s,
                
                You are Loged In.
                
                    '''  %(data[0],str(data[1]),data[4],data[2])
            
            mixer.init()
            mixer.music.load("trainedvoice_dataset/login.mp3")
            mixer.music.play()
            QMessageBox.information(MainWindow,"Loged In",info)
            #sys.exit()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_OtherWindow()
            self.ui.setupUi(self.window)
            MainWindow.hide()
            self.window.show()
            mixer.init()
            mixer.music.load("trainedvoice_dataset/welcome.mp3")
            mixer.music.play()
        else:

            mixer.init()
            mixer.music.load("trainedvoice_dataset/invalidaccount.mp3")
            mixer.music.play()
            QMessageBox.critical(MainWindow,"Error", 'No Account With That Username And Password')



    def create_account(self):
        try:
            gender = None
            name = str(self.firstname.text()+' '+self.lastname.text())
            age = int(self.cr_age.text())
            username = str(self.cr_username.text())
            password = str(self.cr_password.text())
        
            if self.male_radio.isChecked():
                gender = 'Male'
            if self.female_radio.isChecked():
                gender = 'Female'
            
            with sqlite3.connect('users.db') as db:
                c = db.cursor()
            c.execute('INSERT INTO users VALUES(?,?,?,?,?)',(name,age,username,password,gender))
            db.commit()
            c.execute('SELECT * FROM users')
            db.commit()
            c.close()
            db.close()
            mixer.init()
            mixer.music.load("trainedvoice_dataset/Register.mp3")
            mixer.music.play()
            QMessageBox.information(MainWindow,"Success!!", 'Account Created Successfully.')

            self.clear1()

            
        except:
            
            mixer.init()
            mixer.music.load("trainedvoice_dataset/error_reg.mp3")
            mixer.music.play()
            QMessageBox.critical(MainWindow,"Error",'Error !!! Check Entries Again .Make Sure No Filed Is Empty.' )
            pass
        










import src1


if __name__ == "__main__":
    import sys
    from OtherWindow import Ui_OtherWindow

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



