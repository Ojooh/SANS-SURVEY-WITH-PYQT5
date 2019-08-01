# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'survey.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime, date, timedelta
import re
import os
import json
gee = []
user_answer = []

class Ui_surveyWindow(object):
        def __init__(self, user_data):
                self.user_id = user_data
                self.fname = ""
                self.tag = ""
                database = "db/users.json"
                ret = json.loads(open(database).read())
                for i in range(len(ret)):
                        j = i + 1
                        y = str(j)
                        rip = ret[i][y]["id"]
                        if str(rip) == self.user_id:
                                self.user_name = str(ret[i][y]["name"])
                                user_names = self.user_name.split()
                                self.fname = user_names[0]
                                break

        def get_answer(self):
                op1 = self.option1.isChecked()
                op2 = self.option2.isChecked()
                op3 = self.option3.isChecked()
                if(op1):
                        return 0
                elif(op2):
                        return 1
                elif(op3):
                        return 2
                else:
                        return -1

        def start(self):
                self.welcomeFrame.hide()
                filequestion = "db/questions.json"
                fileoption = "db/options.json"
                free = json.loads(open(filequestion).read())
                multi = json.loads(open(fileoption).read())
                self.questionLabel_2.setText("1. " + free["1."])
                self.option1.setText(multi[0][0])
                self.option2.setText(multi[0][1])
                self.option3.setText(multi[0][2])
                

        def nextQuestion(self):
                ans = self.get_answer()
                user_answer.append(ans)
                d = 2
                file1 = "db/questions.json"
                file2 = "db/options.json"
                free = json.loads(open(file1).read())
                multi = json.loads(open(file2).read())

                if len(gee) == 0:
                        gee.append(d)
                        y = str(gee[0]) + "."
                        index = gee[0] - 1
                        self.questionLabel_2.setText(y + free[y])
                        self.option1.setText(multi[index][0])
                        self.option2.setText(multi[index][1])
                        self.option3.setText(multi[index][2])
                else:
                        if gee[0] == len(free):
                                lindex = len(multi) - 1
                                correct = multi[lindex]
                                uanswer = user_answer
                                self.calc(correct, uanswer)

                        else:
                                yi = gee[0] + 1
                                gee[0] = yi
                                y = str(gee[0]) + "."
                                index = gee[0] - 1
                                self.questionLabel_2.setText(y + free[y])
                                self.option1.setText(multi[index][0])
                                self.option2.setText(multi[index][1])
                                self.option3.setText(multi[index][2])


        def calc(self, correct, ua):
                x = 0
                score = 0
                for i in range(len(correct)):
                        if ua[x] == correct[i]:
                                score = score + 5
                        x += 1
                print(score)
                with open("db/users.json") as f:
                        wily = json.loads(f.read())
                        for i in range(len(wily)):
                                j = i + 1
                                y = str(j)
                                if wily[i][y]["id"] == int(self.user_id):
                                        wily[i][y]["score"] = score
                                        with open("db/users.json", 'w') as v:
                                                json.dump(wily, v)
                                        break
                entry = []
                rac ={int(self.user_id) : {'id' : int(self.user_id), 'name' : self.user_name}}
                entry.append(rac)
                cordx = len(ua)
                print(entry)
                for p in range(cordx):
                        df = p + 1
                        tey = "Q"+ str(df)
                        entry[0][int(self.user_id)][tey] = ua[p]

                with open("db/responses.json", 'a+') as e:
                        json.dump(entry, e)
                self.showresult(score)

        def showresult(self, score):
                self.startPageFrame.hide()
                self.scoreLabel.setText("<html><head/><body><p align=\"center\">"+ str(score) + "</p><p align=\"center\">0</p></body></html>")
                if score >= 20:
                        self.commentLabel.setText("<html><head/><body><p align=\"center\">You have a high level of Cyber user security awareness!!</p></body></html>")
                        self.emojiLabel.setStyleSheet("image: url(:/emojis/master.jpg);")
                elif (score >= 10 and score < 20):
                        self.commentLabel.setText("<html><head/><body><p align=\"center\">You Can Be Better with a Cyber user security awareness revision!!</p></body></html>")
                        self.emojiLabel.setStyleSheet("image: url(:/emojis/intermediate.png);")
                else:
                        self.commentLabel.setText("<html><head/><body><p align=\"center\">You Can Be Better with a Cyber user security awareness training!!</p></body></html>")



        def setupUi(self, surveyWindow):
                surveyWindow.setObjectName("surveyWindow")
                surveyWindow.resize(1655, 1006)
                surveyWindow.setStyleSheet("*{\n"
        "    background-color: white;\n"
        "}\n"
        "")
                self.centralwidget = QtWidgets.QWidget(surveyWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.gridLayout = QtWidgets.QGridLayout()
                self.gridLayout.setObjectName("gridLayout")
                self.finishFrame = QtWidgets.QFrame(self.centralwidget)
                self.finishFrame.setStyleSheet("*{\n"
        "        font: 75 18pt \"Comic Sans MS\";\n"
        "}")
                self.finishFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.finishFrame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.finishFrame.setObjectName("finishFrame")
                self.emojiLabel = QtWidgets.QLabel(self.finishFrame)
                self.emojiLabel.setGeometry(QtCore.QRect(50, 50, 241, 231))
                self.emojiLabel.setStyleSheet("image: url(:/emojis/master.jpg);\n"
        "image: url(:/emojis/intermediate.png);\n"
        "image: url(:/emojis/leveler.png);")
                self.emojiLabel.setObjectName("emojiLabel")
                self.label_2 = QtWidgets.QLabel(self.finishFrame)
                self.label_2.setGeometry(QtCore.QRect(350, 90, 1271, 91))
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.finishFrame)
                self.label_3.setGeometry(QtCore.QRect(350, 190, 1001, 91))
                self.label_3.setObjectName("label_3")
                self.scoreLabel = QtWidgets.QLabel(self.finishFrame)
                self.scoreLabel.setGeometry(QtCore.QRect(350, 300, 1001, 171))
                self.scoreLabel.setStyleSheet("font: 75 72pt \"Comic Sans MS\";")
                self.scoreLabel.setObjectName("scoreLabel")
                self.commentLabel = QtWidgets.QLabel(self.finishFrame)
                self.commentLabel.setGeometry(QtCore.QRect(240, 510, 1401, 121))
                self.commentLabel.setObjectName("commentLabel")
                self.startPageFrame = QtWidgets.QFrame(self.finishFrame)
                self.startPageFrame.setGeometry(QtCore.QRect(0, 0, 1631, 982))
                self.startPageFrame.setStyleSheet("*{\n"
        "    \n"
        "    background-color: rgb(255, 255, 255);\n"
        "    \n"
        "    font: 75 italic 18pt \"Comic Sans MS\";\n"
        "}")
                self.startPageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.startPageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.startPageFrame.setObjectName("startPageFrame")
                self.option3_2 = QtWidgets.QRadioButton(self.startPageFrame)
                self.option3_2.setGeometry(QtCore.QRect(816, 1060, 1211, 91))
                self.option3_2.setObjectName("option3_2")
                self.option1 = QtWidgets.QRadioButton(self.startPageFrame)
                self.option1.setGeometry(QtCore.QRect(190, 240, 1211, 81))
                self.option1.setObjectName("option1")
                self.questionLabel_2 = QtWidgets.QLabel(self.startPageFrame)
                self.questionLabel_2.setGeometry(QtCore.QRect(130, 110, 1451, 121))
                self.questionLabel_2.setObjectName("questionLabel_2")
                self.option2 = QtWidgets.QRadioButton(self.startPageFrame)
                self.option2.setGeometry(QtCore.QRect(190, 330, 1211, 81))
                self.option2.setObjectName("option2")
                self.pushButton = QtWidgets.QPushButton(self.startPageFrame)
                self.pushButton.setGeometry(QtCore.QRect(1146, 1180, 361, 141))
                self.pushButton.setStyleSheet("*{\n"
        "    border-radius: 40%;\n"
        "    background-image: url(:/images/nextt.png);\n"
        "}")
                self.pushButton.setText("")
                self.pushButton.setObjectName("pushButton")
                self.option3 = QtWidgets.QRadioButton(self.startPageFrame)
                self.option3.setGeometry(QtCore.QRect(190, 420, 1211, 81))
                self.option3.setObjectName("option3")
                self.nextBtn = QtWidgets.QPushButton(self.startPageFrame)
                self.nextBtn.setGeometry(QtCore.QRect(640, 620, 361, 141))
                self.nextBtn.setStyleSheet("background-image: url(:/images/nextt.png);")
                self.nextBtn.setText("")
                self.nextBtn.setObjectName("nextBtn")
                self.nextBtn.clicked.connect(self.nextQuestion)
                self.welcomeFrame = QtWidgets.QFrame(self.startPageFrame)
                self.welcomeFrame.setGeometry(QtCore.QRect(0, 0, 1631, 951))
                self.welcomeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.welcomeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.welcomeFrame.setObjectName("welcomeFrame")
                self.welcomeIcon = QtWidgets.QLabel(self.welcomeFrame)
                self.welcomeIcon.setGeometry(QtCore.QRect(24, 40, 261, 781))
                self.welcomeIcon.setStyleSheet("background-image: url(:/images/welcome.jpg);")
                self.welcomeIcon.setObjectName("welcomeIcon")
                self.welcomeLabel = QtWidgets.QLabel(self.welcomeFrame)
                self.welcomeLabel.setGeometry(QtCore.QRect(290, 0, 1321, 101))
                self.welcomeLabel.setObjectName("welcomeLabel")
                self.logoIcon = QtWidgets.QLabel(self.welcomeFrame)
                self.logoIcon.setGeometry(QtCore.QRect(310, 100, 1281, 631))
                self.logoIcon.setStyleSheet("\n"
        "background-image: url(:/images/user_awareness1.png);")
                self.logoIcon.setObjectName("logoIcon")
                self.startbtn = QtWidgets.QPushButton(self.welcomeFrame)
                self.startbtn.setGeometry(QtCore.QRect(800, 740, 221, 201))
                self.startbtn.setStyleSheet("*{\n"
        "    border-radius: 40%;\n"
        "    \n"
        "    background-image: url(:/images/start.png);\n"
        "}")
                self.startbtn.setText("")
                self.startbtn.setObjectName("startbtn")
                self.startbtn.clicked.connect(self.start)
                self.gridLayout.addWidget(self.finishFrame, 0, 1, 1, 1)
                self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
                surveyWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(surveyWindow)
                QtCore.QMetaObject.connectSlotsByName(surveyWindow)

        def retranslateUi(self, surveyWindow):
                _translate = QtCore.QCoreApplication.translate
                surveyWindow.setWindowTitle(_translate("surveyWindow", "SANS Survey Window"))
                self.emojiLabel.setText(_translate("surveyWindow", "<html><head/><body><p><br/></p></body></html>"))
                self.label_2.setText(_translate("surveyWindow", "<html><head/><body><p>Thank You " + self.fname+ " for Taking your Time to fill this survey, do have a Lovely Day!!</p></body></html>"))
                self.label_3.setText(_translate("surveyWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Your Score :</span></p></body></html>"))
                self.scoreLabel.setText(_translate("surveyWindow", "<html><head/><body><p align=\"center\">0</p><p align=\"center\">0</p></body></html>"))
                self.commentLabel.setText(_translate("surveyWindow", "<html><head/><body><p align=\"center\">You Can Be Better with a Cyber user security awareness training!!</p></body></html>"))
                self.option3_2.setText(_translate("surveyWindow", "no"))
                self.option1.setText(_translate("surveyWindow", "yes"))
                self.questionLabel_2.setText(_translate("surveyWindow", "<html><head/><body><p>&quot;1.    What is your position within the company?&quot;,</p></body></html>"))
                self.option2.setText(_translate("surveyWindow", "yes"))
                self.option3.setText(_translate("surveyWindow", "yes"))
                self.welcomeIcon.setText(_translate("surveyWindow", "<html><head/><body><p><br/></p></body></html>"))
                self.welcomeLabel.setText(_translate("surveyWindow", "<html><head/><body><p>Welcome <span style=\" font-size:12pt;\">" + self.fname+ "</span>!, Thank you for offering to participate in this test. CLick start to begin.</p></body></html>"))
                self.logoIcon.setText(_translate("surveyWindow", "TextLabel"))

from images import emoji, resource, source

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    surveyWindow = QtWidgets.QMainWindow()
    ui = Ui_surveyWindow()
    ui.setupUi(surveyWindow)
    surveyWindow.show()
    sys.exit(app.exec_())

