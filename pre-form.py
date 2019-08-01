# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pre-form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime, date, timedelta
from survey import Ui_surveyWindow
import re
import os
import json


class Ui_loginWindow(object):
        def openQuestionWindow(self, user_data):
                self.Window = QtWidgets.QMainWindow()
                self.pass_data = user_data
                self.ui = Ui_surveyWindow(self.pass_data)
                self.ui.setupUi(self.Window)
                loginWindow.hide()
                self.Window.show()

        def openRegisterWindow(self):
                self.Window = QtWidgets.QMainWindow()
                self.ui = Ui_RegisterWindow()
                self.ui.setupUi(self.Window)
                loginWindow.hide()
                self.Window.show()

        def messagebox(self,title, message):
                mess = QtWidgets.QMessageBox()
                mess.setWindowTitle(title)
                mess.setStyleSheet("QLabel{ color: blue}")
                mess.setText(message)
                mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
                mess.exec_()

        def warning(self,title, message):
                mess = QtWidgets.QMessageBox()
                mess.setWindowTitle(title)
                mess.setStyleSheet("QLabel{ color: red}")
                for i in range(len(message)):
                        mess.setText(message[i])
                mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
                mess.exec_()

        def cleanLoginInput(self):
                error = []
                user_id = ""
                email2 = self.usernameField.text()
                database = "db/users.json"
                em_check = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email2)
                password2 = self.passwordField.text()

                if(email2 == "" or password2 == ""):
                        error.append("email and password field Required")
                if em_check == None:
                        error.append("incorrect entry for email")
                if os.stat(database).st_size == 0:
                        error.append("Please Register First!!")
                else:
                        data = json.loads(open(database).read())
                        for i in range(len(data)):
                                j = i + 1
                                y = str(j)
                                if data[i][y]["email"] == email2 and data[i][y]["password"] == password2:
                                        user_id = str(data[i][y]["id"])
                                        self.frame.hide()
                                        # print(user_id)
                                        break
                        if(user_id == ""):
                                error.append("User has not registered")

                if len(error) == 0:
                        self.messagebox("congrats", "YOU HAVE REGISTERED AND NOW ARE LOGGED IN")
                        self.openQuestionWindow(user_id)
                #         self.getUserData(id, name, dob, age, country, occupation, email, number, password)
                else:
                        self.warning("alert", error)



        def setupUi(self, loginWindow):
                loginWindow.setObjectName("loginWindow")
                loginWindow.resize(823, 438)
                loginWindow.setMaximumSize(QtCore.QSize(823, 438))
                loginWindow.setStyleSheet("*{\n"
        "    background-color: white;\n"
        "    \n"
        "}")
                self.centralwidget = QtWidgets.QWidget(loginWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.gridLayout = QtWidgets.QGridLayout()
                self.gridLayout.setObjectName("gridLayout")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setStyleSheet("*{\n"
        "    background-color: white;\n"
        "    font-style: Times New Roman;\n"
        "}")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.label = QtWidgets.QLabel(self.frame)
                self.label.setGeometry(QtCore.QRect(320, 10, 161, 61))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.frame)
                self.label_2.setGeometry(QtCore.QRect(80, 115, 141, 41))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                self.label_2.setFont(font)
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.frame)
                self.label_3.setGeometry(QtCore.QRect(80, 180, 121, 41))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                self.label_3.setFont(font)
                self.label_3.setObjectName("label_3")
                self.usernameField = QtWidgets.QLineEdit(self.frame)
                self.usernameField.setGeometry(QtCore.QRect(240, 111, 431, 41))
                self.usernameField.setStyleSheet("*{\n"
        "    border: none;\n"
        "    border-bottom: 2px solid rgb(0, 0, 0);\n"
        "    font-size: 16px;\n"
        "}")
                self.usernameField.setObjectName("usernameField")
                self.passwordField = QtWidgets.QLineEdit(self.frame)
                self.passwordField.setGeometry(QtCore.QRect(240, 180, 431, 41))
                self.passwordField.setStyleSheet("*{\n"
        "    border: none;\n"
        "    border-bottom: 2px solid rgb(0, 0, 0);\n"
        "    font-size: 19px;\n"
        "}")
                self.passwordField.setObjectName("passwordField")
                self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
                self.loginBtn = QtWidgets.QPushButton(self.frame)
                self.loginBtn.setGeometry(QtCore.QRect(310, 250, 101, 61))
                self.loginBtn.setStyleSheet("*{\n"
        "    color: white;\n"
        "    background-color: rgb(8, 177, 255);\n"
        "    border: none;\n"
        "    font-size: 19px;\n"
        "    font-style: Times New Roman\n"
        "}")
                self.loginBtn.setObjectName("loginBtn")
                self.loginBtn.clicked.connect(self.cleanLoginInput)
                self.registerBtn = QtWidgets.QCommandLinkButton(self.frame)
                self.registerBtn.setGeometry(QtCore.QRect(440, 260, 222, 48))
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(True)
                font.setWeight(50)
                self.registerBtn.setFont(font)
                self.registerBtn.setObjectName("registerBtn")
                self.registerBtn.clicked.connect(self.openRegisterWindow)
                self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
                self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
                loginWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(loginWindow)
                QtCore.QMetaObject.connectSlotsByName(loginWindow)

        def retranslateUi(self, loginWindow):
                _translate = QtCore.QCoreApplication.translate
                loginWindow.setWindowTitle(_translate("loginWindow", "Login"))
                self.label.setText(_translate("loginWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Login</span></p></body></html>"))
                self.label_2.setText(_translate("loginWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Email :</span></p></body></html>"))
                self.label_3.setText(_translate("loginWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Password :</span></p></body></html>"))
                self.loginBtn.setText(_translate("loginWindow", "LOGIN"))
                self.registerBtn.setText(_translate("loginWindow", "Register"))


class Ui_RegisterWindow(object):
        def openQuestionWindow(self, user_data):
                self.Window = QtWidgets.QMainWindow()
                self.pass_data = user_data
                self.ui = Ui_surveyWindow(self.pass_data)
                self.ui.setupUi(self.Window)
                loginWindow.hide()
                self.Window.show()

        # def openLoginWindow(self):
        #         # sys.exit(app.exec_())
        #         self.Window = QtWidgets.QMainWindow()
        #         self.ui = Ui_loginWindow()
        #         self.ui.setupUi(self.Window)
        #         registerWindow = QtWidgets.QMainWindow()
        #         ui = Ui_RegisterWindow()
        #         ui.setupUi(loginWindow)
        #         # ui.destroy()
        #                         # self.Window.show()

        def messagebox(self,title, message):
                mess = QtWidgets.QMessageBox()
                mess.setWindowTitle(title)
                mess.setStyleSheet("QLabel{ color: blue}")
                mess.setText(message)
                mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
                mess.exec_()

        def warning(self,title, message):
                mess = QtWidgets.QMessageBox()
                mess.setWindowTitle(title)
                mess.setStyleSheet("QLabel{ color: red}")
                for i in range(len(message)):
                        mess.setText(message[i])
                mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
                mess.exec_()

        def cleanInput(self):
                message = []
                fname = self.fnameField.text()
                lname = self.lnameField.text()
                name = fname + " " + lname
                name_check = re.findall('[A-Za-z]{2,25}\s[A-Za-z]{2,25}', name)
                tad = self.bdayField.text()
                dob = "{2}-{1}-{0}".format(*tad.split('/'))
                age = str(self.calculate_age(tad))
                country = self.countryField.text()
                country_check = re.findall('[A-Za-z]{2,25}\s[A-Za-z]{2,25}', country)
                occupation = self.occupationField.text()
                occupation_check = re.findall('[A-Za-z]{2,25}\s[A-Za-z]{2,25}', occupation)
                email = self.emailField.text()
                em_check = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
                number = self.numberField.text()
                password = self.passwordField.text()
                num_check = re.match('^[0-9]+$', number)

                if(fname == "" or lname == ""):
                        message.append("first name and last name Fields are required")
                if(name_check  == None):
                        message.append("incorrect entry for first name or last name Field")
                if(country_check == None):
                        message.append("incorrect entry for country Field")
                if(occupation_check == None):
                        message.append("incorrect entry for occupation Field")
                if em_check == None:
                        message.append("incorrect entry for email")
                if num_check == None:
                        message.append("incorrect entry for number")

                if len(message) == 0:
                        name = name.capitalize()
                        country = country.capitalize()
                        occupation = occupation.capitalize()
                        filename = "db/counter.json"
                        with open(filename, 'r') as f:
                                f = json.load(f)
                                print(f)
                                id = f['id']
                                lew = id + 1
                        counter = {}
                        counter['id'] = lew                        
                        with open(filename, 'w') as f:
                                json.dump(counter, f)
                        self.messagebox("congrats", "YOU HAVE REGISTERED AND NOW ARE LOGGED IN")
                        self.getUserData(id, name, dob, age, country, occupation, email, number, password)
                else:
                        self.warning("alert", message)



        def getUserData(self, id, name, dob, age, country, occupation, email, number, password):
                filename = "db/users.json"
                resc ={id : {'id' : id, 'name' : name, 'dob' : dob, 'age' : age, 'country' : country, 'occupation' : occupation, 'email' : email, 'number' : number, 'password' : password}}
                if os.stat(filename).st_size == 0:
                        users = []
                        users.append(resc)
                        with open(filename, 'w+') as f:
                                json.dump(users, f)
                else:
                        with open(filename, 'r') as f:
                                u = json.load(f)
                                u.append(resc)
                        with open(filename, 'w') as f:
                                json.dump(u, f)


                self.openQuestionWindow(str(id))




        
        def calculate_age(self, birth):
                today = date.today()
                chan = str(birth)
                ray = chan.split("/")
                bornYear = int(ray[2])
                return today.year - bornYear

        def setupUi(self, RegisterWindow):
                RegisterWindow.setObjectName("RegisterWindow")
                RegisterWindow.resize(1237, 791)
                RegisterWindow.setMaximumSize(QtCore.QSize(1237, 791))
                RegisterWindow.setStyleSheet("*{\n"
        "    background-color: white;\n"
        "    font-style: Times New Roman;\n"
        "}\n"
        "")
                self.centralwidget = QtWidgets.QWidget(RegisterWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.gridLayout = QtWidgets.QGridLayout()
                self.gridLayout.setObjectName("gridLayout")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setStyleSheet("*{\n"
        "    background-color: white;\n"
        "    font-style: Times New Roman;\n"
        "}")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.label_2 = QtWidgets.QLabel(self.frame)
                self.label_2.setGeometry(QtCore.QRect(60, 180, 141, 41))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                self.label_2.setFont(font)
                self.label_2.setObjectName("label_2")
                self.label = QtWidgets.QLabel(self.frame)
                self.label.setGeometry(QtCore.QRect(450, 70, 591, 61))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.fnameField = QtWidgets.QLineEdit(self.frame)
                self.fnameField.setGeometry(QtCore.QRect(210, 170, 351, 41))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(18)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.fnameField.setFont(font)
                self.fnameField.setStyleSheet("*{\n"
        "    border: none;\n"
        "    border-bottom: 2px solid rgb(0, 0, 0);\n"
        "    font-size: 16px;\n"
        "    font: 75 18pt \"Times New Roman\";\n"
        "}")
                self.fnameField.setObjectName("fnameField")
                self.label_3 = QtWidgets.QLabel(self.frame)
                self.label_3.setGeometry(QtCore.QRect(230, 40, 171, 121))
                self.label_3.setStyleSheet("image: url(:/newPrefix/register-image.png);")
                self.label_3.setObjectName("label_3")
                self.lnameField = QtWidgets.QLineEdit(self.frame)
                self.lnameField.setGeometry(QtCore.QRect(760, 170, 411, 41))
                self.lnameField.setStyleSheet("*{\n"
        "    border: none;\n"
        "    border-bottom: 2px solid rgb(0, 0, 0);\n"
        "    font-size: 16px;\n"
        "    font: 75 18pt \"Times New Roman\";\n"
        "}")
                self.lnameField.setObjectName("lnameField")
                self.label_4 = QtWidgets.QLabel(self.frame)
                self.label_4.setGeometry(QtCore.QRect(600, 180, 141, 41))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                self.label_4.setFont(font)
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.frame)
                self.label_5.setGeometry(QtCore.QRect(70, 270, 121, 41))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                self.label_5.setFont(font)
                self.label_5.setObjectName("label_5")
                self.bdayField = QtWidgets.QDateEdit(self.frame)
                self.bdayField.setGeometry(QtCore.QRect(210, 260, 361, 51))
                self.bdayField.setStyleSheet("*{\n"
        "    border: none;\n"
        "    border-bottom: 2px solid rgb(0, 0, 0);\n"
        "    font: 75 18pt \"Times New Roman\";\n"
        "}")
                self.bdayField.setObjectName("bdayField")
                self.countryField = QtWidgets.QLineEdit(self.frame)
                self.countryField.setGeometry(QtCore.QRect(230, 340, 351, 41))
                self.countryField.setStyleSheet("*{\n"
        "    border: none;\n"
        "    border-bottom: 2px solid rgb(0, 0, 0);\n"
        "    font: 75 18pt \"Times New Roman\";\n"
        "}")
                self.countryField.setObjectName("countryField")
                self.label_6 = QtWidgets.QLabel(self.frame)
                self.label_6.setGeometry(QtCore.QRect(70, 350, 151, 41))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                self.label_6.setFont(font)
                self.label_6.setObjectName("label_6")
                self.occupationField = QtWidgets.QLineEdit(self.frame)
                self.occupationField.setGeometry(QtCore.QRect(760, 340, 411, 41))
                self.occupationField.setStyleSheet("*{\n"
        "    border: none;\n"
        "    border-bottom: 2px solid rgb(0, 0, 0);\n"
        "    font-size: 16px;\n"
        "    font: 75 14pt \"Times New Roman\";\n"
        "}")
                self.occupationField.setObjectName("occupationField")
                self.label_13 = QtWidgets.QLabel(self.frame)
                self.label_13.setGeometry(QtCore.QRect(590, 350, 151, 41))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                self.label_13.setFont(font)
                self.label_13.setObjectName("label_13")
                self.label_14 = QtWidgets.QLabel(self.frame)
                self.label_14.setGeometry(QtCore.QRect(590, 270, 121, 41))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                self.label_14.setFont(font)
                self.label_14.setObjectName("label_14")
                self.ageField = QtWidgets.QLabel(self.frame)
                self.ageField.setGeometry(QtCore.QRect(730, 260, 371, 61))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(18)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.ageField.setFont(font)
                self.ageField.setStyleSheet("*{\n"
        "    font: 75 18pt \"Times New Roman\";\n"
        "}")
                self.ageField.setObjectName("ageField")
                self.label_16 = QtWidgets.QLabel(self.frame)
                self.label_16.setGeometry(QtCore.QRect(590, 430, 201, 41))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                self.label_16.setFont(font)
                self.label_16.setObjectName("label_16")
                self.numberField = QtWidgets.QLineEdit(self.frame)
                self.numberField.setGeometry(QtCore.QRect(800, 420, 371, 41))
                self.numberField.setStyleSheet("*{\n"
        "    border: none;\n"
        "    border-bottom: 2px solid rgb(0, 0, 0);\n"
        "    font-size: 16px;\n"
        "    font: 75 14pt \"Times New Roman\";\n"
        "}")
                self.numberField.setObjectName("numberField")
                self.emailField = QtWidgets.QLineEdit(self.frame)
                self.emailField.setGeometry(QtCore.QRect(230, 420, 351, 41))
                self.emailField.setStyleSheet("*{\n"
        "    border: none;\n"
        "    border-bottom: 2px solid rgb(0, 0, 0);\n"
        "    font-size: 16px;\n"
        "    font: 75 14pt \"Times New Roman\";\n"
        "}")
                self.emailField.setObjectName("emailField")
                self.label_17 = QtWidgets.QLabel(self.frame)
                self.label_17.setGeometry(QtCore.QRect(40, 430, 181, 41))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                self.label_17.setFont(font)
                self.label_17.setObjectName("label_17")
                self.registerBtn = QtWidgets.QPushButton(self.frame)
                self.registerBtn.setGeometry(QtCore.QRect(510, 600, 201, 81))
                self.registerBtn.setStyleSheet("*{\n"
        "    color: white;\n"
        "    background-color: rgb(8, 177, 255);\n"
        "    border: none;\n"
        "    font-size: 19px;\n"
        "    font-style: Times New Roman\n"
        "}")
                self.registerBtn.setObjectName("registerBtn")
                self.registerBtn.clicked.connect(self.cleanInput)
                self.goBackBtn = QtWidgets.QPushButton(self.frame)
                self.goBackBtn.setGeometry(QtCore.QRect(0, 0, 71, 61))
                self.goBackBtn.setStyleSheet("image: url(:/newPrefix/go-back.png);")
                self.goBackBtn.setText("")
                self.goBackBtn.setObjectName("goBackBtn")
                # self.goBackBtn.clicked.connect(self.openLoginWindow)
                self.label_18 = QtWidgets.QLabel(self.frame)
                self.label_18.setGeometry(QtCore.QRect(90, 0, 121, 41))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                self.label_18.setFont(font)
                self.label_18.setObjectName("label_18")
                self.label_19 = QtWidgets.QLabel(self.frame)
                self.label_19.setGeometry(QtCore.QRect(40, 500, 171, 41))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                self.label_19.setFont(font)
                self.label_19.setObjectName("label_19")
                self.passwordField = QtWidgets.QLineEdit(self.frame)
                self.passwordField.setGeometry(QtCore.QRect(230, 490, 351, 41))
                self.passwordField.setStyleSheet("*{\n"
        "    border: none;\n"
        "    border-bottom: 2px solid rgb(0, 0, 0);\n"
        "    font-size: 16px;\n"
        "    font: 75 14pt \"Times New Roman\";\n"
        "}")
                self.passwordField.setObjectName("passwordField")
                self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
                self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
                self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
                RegisterWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(RegisterWindow)
                QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

        def retranslateUi(self, RegisterWindow):
                _translate = QtCore.QCoreApplication.translate
                RegisterWindow.setWindowTitle(_translate("RegisterWindow", "Register Form"))
                self.label_2.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">First Name: </span></p></body></html>"))
                self.label.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">Let us Know A little About You</span></p></body></html>"))
                self.label_3.setText(_translate("RegisterWindow", "<html><head/><body><p><br/></p></body></html>"))
                self.label_4.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Last Name: </span></p></body></html>"))
                self.label_5.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">BirthDay: </span></p></body></html>"))
                self.label_6.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Country :</span></p></body></html>"))
                self.label_13.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Occupation:</span></p></body></html>"))
                self.label_14.setText(_translate("RegisterWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Age :</span></p></body></html>"))
                self.ageField.setText(_translate("RegisterWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">0</span></p></body></html>"))
                self.label_16.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Phone Number:</span></p></body></html>"))
                self.label_17.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Email Address :</span></p></body></html>"))
                self.registerBtn.setText(_translate("RegisterWindow", "REGISTER"))
                self.label_18.setText(_translate("RegisterWindow", "<html><head/><body><p>Go Back</p></body></html>"))
                self.label_19.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Password :</span></p></body></html>"))


                        

from images import source



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    filename = "db/counter.json"
    if os.stat(filename).st_size == 0:
            counter = {}
            counter['id'] = 1
            users = {}
            with open(filename, 'w+') as f:
                    json.dump(counter, f)

    loginWindow = QtWidgets.QMainWindow()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())

