# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\FracktalWorks\Julia2018ExtendedTouchUI\octoprint_Julia2018ExtendedTouchUI\Keyboard.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(480, 320)
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 288, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(_fromUtf8("background-color:  rgb(40, 40, 40);\n"
"font-color: white;\n"
"color: rgb(255, 255, 255);"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 80, 480, 250))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.pageAlphaU = QtGui.QWidget()
        self.pageAlphaU.setObjectName(_fromUtf8("pageAlphaU"))
        self.ButtonLowercase = QtGui.QPushButton(self.pageAlphaU)
        self.ButtonLowercase.setGeometry(QtCore.QRect(0, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.ButtonLowercase.setFont(font)
        self.ButtonLowercase.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonLowercase.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/caps-lock-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonLowercase.setIcon(icon)
        self.ButtonLowercase.setObjectName(_fromUtf8("ButtonLowercase"))
        self.Button1 = QtGui.QPushButton(self.pageAlphaU)
        self.Button1.setGeometry(QtCore.QRect(0, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button1.setFont(font)
        self.Button1.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button1.setObjectName(_fromUtf8("Button1"))
        self.Button11 = QtGui.QPushButton(self.pageAlphaU)
        self.Button11.setGeometry(QtCore.QRect(0, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button11.setFont(font)
        self.Button11.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button11.setObjectName(_fromUtf8("Button11"))
        self.Button2 = QtGui.QPushButton(self.pageAlphaU)
        self.Button2.setGeometry(QtCore.QRect(48, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button2.setFont(font)
        self.Button2.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button2.setObjectName(_fromUtf8("Button2"))
        self.Button12 = QtGui.QPushButton(self.pageAlphaU)
        self.Button12.setGeometry(QtCore.QRect(48, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button12.setFont(font)
        self.Button12.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button12.setObjectName(_fromUtf8("Button12"))
        self.Button20 = QtGui.QPushButton(self.pageAlphaU)
        self.Button20.setGeometry(QtCore.QRect(48, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button20.setFont(font)
        self.Button20.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button20.setObjectName(_fromUtf8("Button20"))
        self.Button3 = QtGui.QPushButton(self.pageAlphaU)
        self.Button3.setGeometry(QtCore.QRect(96, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button3.setFont(font)
        self.Button3.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button3.setObjectName(_fromUtf8("Button3"))
        self.Button13 = QtGui.QPushButton(self.pageAlphaU)
        self.Button13.setGeometry(QtCore.QRect(96, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button13.setFont(font)
        self.Button13.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button13.setObjectName(_fromUtf8("Button13"))
        self.Button21 = QtGui.QPushButton(self.pageAlphaU)
        self.Button21.setGeometry(QtCore.QRect(96, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button21.setFont(font)
        self.Button21.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button21.setObjectName(_fromUtf8("Button21"))
        self.Button4 = QtGui.QPushButton(self.pageAlphaU)
        self.Button4.setGeometry(QtCore.QRect(144, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button4.setFont(font)
        self.Button4.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button4.setObjectName(_fromUtf8("Button4"))
        self.Button14 = QtGui.QPushButton(self.pageAlphaU)
        self.Button14.setGeometry(QtCore.QRect(144, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button14.setFont(font)
        self.Button14.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button14.setObjectName(_fromUtf8("Button14"))
        self.Button22 = QtGui.QPushButton(self.pageAlphaU)
        self.Button22.setGeometry(QtCore.QRect(144, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button22.setFont(font)
        self.Button22.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button22.setObjectName(_fromUtf8("Button22"))
        self.Button5 = QtGui.QPushButton(self.pageAlphaU)
        self.Button5.setGeometry(QtCore.QRect(192, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button5.setFont(font)
        self.Button5.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button5.setObjectName(_fromUtf8("Button5"))
        self.Button15 = QtGui.QPushButton(self.pageAlphaU)
        self.Button15.setGeometry(QtCore.QRect(192, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button15.setFont(font)
        self.Button15.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button15.setObjectName(_fromUtf8("Button15"))
        self.Button23 = QtGui.QPushButton(self.pageAlphaU)
        self.Button23.setGeometry(QtCore.QRect(192, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button23.setFont(font)
        self.Button23.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button23.setObjectName(_fromUtf8("Button23"))
        self.Button6 = QtGui.QPushButton(self.pageAlphaU)
        self.Button6.setGeometry(QtCore.QRect(240, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button6.setFont(font)
        self.Button6.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button6.setObjectName(_fromUtf8("Button6"))
        self.Button16 = QtGui.QPushButton(self.pageAlphaU)
        self.Button16.setGeometry(QtCore.QRect(240, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button16.setFont(font)
        self.Button16.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button16.setObjectName(_fromUtf8("Button16"))
        self.Button24 = QtGui.QPushButton(self.pageAlphaU)
        self.Button24.setGeometry(QtCore.QRect(240, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button24.setFont(font)
        self.Button24.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button24.setObjectName(_fromUtf8("Button24"))
        self.Button7 = QtGui.QPushButton(self.pageAlphaU)
        self.Button7.setGeometry(QtCore.QRect(288, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button7.setFont(font)
        self.Button7.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button7.setObjectName(_fromUtf8("Button7"))
        self.Button17 = QtGui.QPushButton(self.pageAlphaU)
        self.Button17.setGeometry(QtCore.QRect(288, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button17.setFont(font)
        self.Button17.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button17.setObjectName(_fromUtf8("Button17"))
        self.Button25 = QtGui.QPushButton(self.pageAlphaU)
        self.Button25.setGeometry(QtCore.QRect(288, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button25.setFont(font)
        self.Button25.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button25.setObjectName(_fromUtf8("Button25"))
        self.Button8 = QtGui.QPushButton(self.pageAlphaU)
        self.Button8.setGeometry(QtCore.QRect(336, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button8.setFont(font)
        self.Button8.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button8.setObjectName(_fromUtf8("Button8"))
        self.Button18 = QtGui.QPushButton(self.pageAlphaU)
        self.Button18.setGeometry(QtCore.QRect(336, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button18.setFont(font)
        self.Button18.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button18.setObjectName(_fromUtf8("Button18"))
        self.Button26 = QtGui.QPushButton(self.pageAlphaU)
        self.Button26.setGeometry(QtCore.QRect(336, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button26.setFont(font)
        self.Button26.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button26.setObjectName(_fromUtf8("Button26"))
        self.Button9 = QtGui.QPushButton(self.pageAlphaU)
        self.Button9.setGeometry(QtCore.QRect(384, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button9.setFont(font)
        self.Button9.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button9.setObjectName(_fromUtf8("Button9"))
        self.Button19 = QtGui.QPushButton(self.pageAlphaU)
        self.Button19.setGeometry(QtCore.QRect(384, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button19.setFont(font)
        self.Button19.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button19.setObjectName(_fromUtf8("Button19"))
        self.Button27 = QtGui.QPushButton(self.pageAlphaU)
        self.Button27.setGeometry(QtCore.QRect(384, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button27.setFont(font)
        self.Button27.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button27.setObjectName(_fromUtf8("Button27"))
        self.ButtonBackspaceAlphaU = QtGui.QPushButton(self.pageAlphaU)
        self.ButtonBackspaceAlphaU.setGeometry(QtCore.QRect(432, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.ButtonBackspaceAlphaU.setFont(font)
        self.ButtonBackspaceAlphaU.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonBackspaceAlphaU.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/backspace-arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonBackspaceAlphaU.setIcon(icon1)
        self.ButtonBackspaceAlphaU.setIconSize(QtCore.QSize(25, 25))
        self.ButtonBackspaceAlphaU.setObjectName(_fromUtf8("ButtonBackspaceAlphaU"))
        self.Button10 = QtGui.QPushButton(self.pageAlphaU)
        self.Button10.setGeometry(QtCore.QRect(432, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button10.setFont(font)
        self.Button10.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button10.setObjectName(_fromUtf8("Button10"))
        self.Button28 = QtGui.QPushButton(self.pageAlphaU)
        self.Button28.setGeometry(QtCore.QRect(432, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button28.setFont(font)
        self.Button28.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button28.setObjectName(_fromUtf8("Button28"))
        self.ButtonSpecialAlphaU = QtGui.QPushButton(self.pageAlphaU)
        self.ButtonSpecialAlphaU.setGeometry(QtCore.QRect(96, 180, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonSpecialAlphaU.setFont(font)
        self.ButtonSpecialAlphaU.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonSpecialAlphaU.setObjectName(_fromUtf8("ButtonSpecialAlphaU"))
        self.ButtonSpaceAlphaU = QtGui.QPushButton(self.pageAlphaU)
        self.ButtonSpaceAlphaU.setGeometry(QtCore.QRect(192, 180, 192, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonSpaceAlphaU.setFont(font)
        self.ButtonSpaceAlphaU.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonSpaceAlphaU.setObjectName(_fromUtf8("ButtonSpaceAlphaU"))
        self.ButtonNumericAlphaU = QtGui.QPushButton(self.pageAlphaU)
        self.ButtonNumericAlphaU.setGeometry(QtCore.QRect(0, 180, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonNumericAlphaU.setFont(font)
        self.ButtonNumericAlphaU.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonNumericAlphaU.setObjectName(_fromUtf8("ButtonNumericAlphaU"))
        self.ButtonSubmitAlphaU = QtGui.QPushButton(self.pageAlphaU)
        self.ButtonSubmitAlphaU.setGeometry(QtCore.QRect(384, 180, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonSubmitAlphaU.setFont(font)
        self.ButtonSubmitAlphaU.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonSubmitAlphaU.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/verification-mark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonSubmitAlphaU.setIcon(icon2)
        self.ButtonSubmitAlphaU.setIconSize(QtCore.QSize(35, 35))
        self.ButtonSubmitAlphaU.setObjectName(_fromUtf8("ButtonSubmitAlphaU"))
        self.stackedWidget.addWidget(self.pageAlphaU)
        self.pageAlpha = QtGui.QWidget()
        self.pageAlpha.setObjectName(_fromUtf8("pageAlpha"))
        self.Button48 = QtGui.QPushButton(self.pageAlpha)
        self.Button48.setGeometry(QtCore.QRect(48, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button48.setFont(font)
        self.Button48.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button48.setObjectName(_fromUtf8("Button48"))
        self.Button52 = QtGui.QPushButton(self.pageAlpha)
        self.Button52.setGeometry(QtCore.QRect(240, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button52.setFont(font)
        self.Button52.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button52.setObjectName(_fromUtf8("Button52"))
        self.Button42 = QtGui.QPushButton(self.pageAlpha)
        self.Button42.setGeometry(QtCore.QRect(144, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button42.setFont(font)
        self.Button42.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button42.setObjectName(_fromUtf8("Button42"))
        self.Button54 = QtGui.QPushButton(self.pageAlpha)
        self.Button54.setGeometry(QtCore.QRect(336, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button54.setFont(font)
        self.Button54.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button54.setObjectName(_fromUtf8("Button54"))
        self.Button35 = QtGui.QPushButton(self.pageAlpha)
        self.Button35.setGeometry(QtCore.QRect(288, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button35.setFont(font)
        self.Button35.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button35.setObjectName(_fromUtf8("Button35"))
        self.Button45 = QtGui.QPushButton(self.pageAlpha)
        self.Button45.setGeometry(QtCore.QRect(288, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button45.setFont(font)
        self.Button45.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button45.setObjectName(_fromUtf8("Button45"))
        self.Button53 = QtGui.QPushButton(self.pageAlpha)
        self.Button53.setGeometry(QtCore.QRect(288, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button53.setFont(font)
        self.Button53.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button53.setObjectName(_fromUtf8("Button53"))
        self.Button33 = QtGui.QPushButton(self.pageAlpha)
        self.Button33.setGeometry(QtCore.QRect(192, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button33.setFont(font)
        self.Button33.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button33.setObjectName(_fromUtf8("Button33"))
        self.Button43 = QtGui.QPushButton(self.pageAlpha)
        self.Button43.setGeometry(QtCore.QRect(192, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button43.setFont(font)
        self.Button43.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button43.setObjectName(_fromUtf8("Button43"))
        self.Button40 = QtGui.QPushButton(self.pageAlpha)
        self.Button40.setGeometry(QtCore.QRect(48, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button40.setFont(font)
        self.Button40.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button40.setObjectName(_fromUtf8("Button40"))
        self.Button29 = QtGui.QPushButton(self.pageAlpha)
        self.Button29.setGeometry(QtCore.QRect(0, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button29.setFont(font)
        self.Button29.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button29.setObjectName(_fromUtf8("Button29"))
        self.Button30 = QtGui.QPushButton(self.pageAlpha)
        self.Button30.setGeometry(QtCore.QRect(48, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button30.setFont(font)
        self.Button30.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button30.setObjectName(_fromUtf8("Button30"))
        self.Button38 = QtGui.QPushButton(self.pageAlpha)
        self.Button38.setGeometry(QtCore.QRect(432, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button38.setFont(font)
        self.Button38.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button38.setObjectName(_fromUtf8("Button38"))
        self.ButtonUppercase = QtGui.QPushButton(self.pageAlpha)
        self.ButtonUppercase.setGeometry(QtCore.QRect(0, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonUppercase.setFont(font)
        self.ButtonUppercase.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonUppercase.setText(_fromUtf8(""))
        self.ButtonUppercase.setIcon(icon)
        self.ButtonUppercase.setObjectName(_fromUtf8("ButtonUppercase"))
        self.Button49 = QtGui.QPushButton(self.pageAlpha)
        self.Button49.setGeometry(QtCore.QRect(96, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button49.setFont(font)
        self.Button49.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button49.setObjectName(_fromUtf8("Button49"))
        self.Button31 = QtGui.QPushButton(self.pageAlpha)
        self.Button31.setGeometry(QtCore.QRect(96, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button31.setFont(font)
        self.Button31.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button31.setObjectName(_fromUtf8("Button31"))
        self.Button32 = QtGui.QPushButton(self.pageAlpha)
        self.Button32.setGeometry(QtCore.QRect(144, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button32.setFont(font)
        self.Button32.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button32.setObjectName(_fromUtf8("Button32"))
        self.Button44 = QtGui.QPushButton(self.pageAlpha)
        self.Button44.setGeometry(QtCore.QRect(240, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button44.setFont(font)
        self.Button44.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button44.setObjectName(_fromUtf8("Button44"))
        self.Button37 = QtGui.QPushButton(self.pageAlpha)
        self.Button37.setGeometry(QtCore.QRect(384, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button37.setFont(font)
        self.Button37.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button37.setObjectName(_fromUtf8("Button37"))
        self.Button46 = QtGui.QPushButton(self.pageAlpha)
        self.Button46.setGeometry(QtCore.QRect(336, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button46.setFont(font)
        self.Button46.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button46.setObjectName(_fromUtf8("Button46"))
        self.Button55 = QtGui.QPushButton(self.pageAlpha)
        self.Button55.setGeometry(QtCore.QRect(384, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button55.setFont(font)
        self.Button55.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button55.setObjectName(_fromUtf8("Button55"))
        self.Button41 = QtGui.QPushButton(self.pageAlpha)
        self.Button41.setGeometry(QtCore.QRect(96, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button41.setFont(font)
        self.Button41.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button41.setObjectName(_fromUtf8("Button41"))
        self.Button51 = QtGui.QPushButton(self.pageAlpha)
        self.Button51.setGeometry(QtCore.QRect(192, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button51.setFont(font)
        self.Button51.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button51.setObjectName(_fromUtf8("Button51"))
        self.Button36 = QtGui.QPushButton(self.pageAlpha)
        self.Button36.setGeometry(QtCore.QRect(336, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button36.setFont(font)
        self.Button36.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button36.setObjectName(_fromUtf8("Button36"))
        self.Button39 = QtGui.QPushButton(self.pageAlpha)
        self.Button39.setGeometry(QtCore.QRect(0, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button39.setFont(font)
        self.Button39.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button39.setObjectName(_fromUtf8("Button39"))
        self.Button50 = QtGui.QPushButton(self.pageAlpha)
        self.Button50.setGeometry(QtCore.QRect(144, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button50.setFont(font)
        self.Button50.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button50.setObjectName(_fromUtf8("Button50"))
        self.ButtonBackspaceAlpha = QtGui.QPushButton(self.pageAlpha)
        self.ButtonBackspaceAlpha.setGeometry(QtCore.QRect(432, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonBackspaceAlpha.setFont(font)
        self.ButtonBackspaceAlpha.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonBackspaceAlpha.setText(_fromUtf8(""))
        self.ButtonBackspaceAlpha.setIcon(icon1)
        self.ButtonBackspaceAlpha.setIconSize(QtCore.QSize(25, 25))
        self.ButtonBackspaceAlpha.setObjectName(_fromUtf8("ButtonBackspaceAlpha"))
        self.Button34 = QtGui.QPushButton(self.pageAlpha)
        self.Button34.setGeometry(QtCore.QRect(240, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button34.setFont(font)
        self.Button34.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button34.setObjectName(_fromUtf8("Button34"))
        self.Button47 = QtGui.QPushButton(self.pageAlpha)
        self.Button47.setGeometry(QtCore.QRect(384, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button47.setFont(font)
        self.Button47.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button47.setObjectName(_fromUtf8("Button47"))
        self.Button56 = QtGui.QPushButton(self.pageAlpha)
        self.Button56.setGeometry(QtCore.QRect(432, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button56.setFont(font)
        self.Button56.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button56.setObjectName(_fromUtf8("Button56"))
        self.ButtonSpaceAlpha = QtGui.QPushButton(self.pageAlpha)
        self.ButtonSpaceAlpha.setGeometry(QtCore.QRect(192, 180, 192, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonSpaceAlpha.setFont(font)
        self.ButtonSpaceAlpha.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonSpaceAlpha.setObjectName(_fromUtf8("ButtonSpaceAlpha"))
        self.ButtonNumericAlpha = QtGui.QPushButton(self.pageAlpha)
        self.ButtonNumericAlpha.setGeometry(QtCore.QRect(0, 180, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonNumericAlpha.setFont(font)
        self.ButtonNumericAlpha.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonNumericAlpha.setObjectName(_fromUtf8("ButtonNumericAlpha"))
        self.ButtonSubmitAlpha = QtGui.QPushButton(self.pageAlpha)
        self.ButtonSubmitAlpha.setGeometry(QtCore.QRect(384, 180, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonSubmitAlpha.setFont(font)
        self.ButtonSubmitAlpha.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonSubmitAlpha.setText(_fromUtf8(""))
        self.ButtonSubmitAlpha.setIcon(icon2)
        self.ButtonSubmitAlpha.setIconSize(QtCore.QSize(35, 35))
        self.ButtonSubmitAlpha.setObjectName(_fromUtf8("ButtonSubmitAlpha"))
        self.ButtonSpecialAlpha = QtGui.QPushButton(self.pageAlpha)
        self.ButtonSpecialAlpha.setGeometry(QtCore.QRect(96, 180, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonSpecialAlpha.setFont(font)
        self.ButtonSpecialAlpha.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonSpecialAlpha.setObjectName(_fromUtf8("ButtonSpecialAlpha"))
        self.stackedWidget.addWidget(self.pageAlpha)
        self.pageSpecial = QtGui.QWidget()
        self.pageSpecial.setObjectName(_fromUtf8("pageSpecial"))
        self.Button78 = QtGui.QPushButton(self.pageSpecial)
        self.Button78.setGeometry(QtCore.QRect(48, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button78.setFont(font)
        self.Button78.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button78.setObjectName(_fromUtf8("Button78"))
        self.Button82 = QtGui.QPushButton(self.pageSpecial)
        self.Button82.setGeometry(QtCore.QRect(240, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button82.setFont(font)
        self.Button82.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button82.setObjectName(_fromUtf8("Button82"))
        self.Button70 = QtGui.QPushButton(self.pageSpecial)
        self.Button70.setGeometry(QtCore.QRect(144, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button70.setFont(font)
        self.Button70.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button70.setObjectName(_fromUtf8("Button70"))
        self.Button84 = QtGui.QPushButton(self.pageSpecial)
        self.Button84.setGeometry(QtCore.QRect(192, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button84.setFont(font)
        self.Button84.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button84.setObjectName(_fromUtf8("Button84"))
        self.Button73 = QtGui.QPushButton(self.pageSpecial)
        self.Button73.setGeometry(QtCore.QRect(288, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button73.setFont(font)
        self.Button73.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button73.setObjectName(_fromUtf8("Button73"))
        self.Button83 = QtGui.QPushButton(self.pageSpecial)
        self.Button83.setGeometry(QtCore.QRect(288, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button83.setFont(font)
        self.Button83.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button83.setObjectName(_fromUtf8("Button83"))
        self.Button71 = QtGui.QPushButton(self.pageSpecial)
        self.Button71.setGeometry(QtCore.QRect(336, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button71.setFont(font)
        self.Button71.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button71.setObjectName(_fromUtf8("Button71"))
        self.Button68 = QtGui.QPushButton(self.pageSpecial)
        self.Button68.setGeometry(QtCore.QRect(48, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button68.setFont(font)
        self.Button68.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button68.setObjectName(_fromUtf8("Button68"))
        self.Button77 = QtGui.QPushButton(self.pageSpecial)
        self.Button77.setGeometry(QtCore.QRect(0, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button77.setFont(font)
        self.Button77.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button77.setObjectName(_fromUtf8("Button77"))
        self.Button79 = QtGui.QPushButton(self.pageSpecial)
        self.Button79.setGeometry(QtCore.QRect(96, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button79.setFont(font)
        self.Button79.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button79.setObjectName(_fromUtf8("Button79"))
        self.Button72 = QtGui.QPushButton(self.pageSpecial)
        self.Button72.setGeometry(QtCore.QRect(384, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button72.setFont(font)
        self.Button72.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button72.setObjectName(_fromUtf8("Button72"))
        self.Button74 = QtGui.QPushButton(self.pageSpecial)
        self.Button74.setGeometry(QtCore.QRect(336, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button74.setFont(font)
        self.Button74.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button74.setObjectName(_fromUtf8("Button74"))
        self.Button85 = QtGui.QPushButton(self.pageSpecial)
        self.Button85.setGeometry(QtCore.QRect(240, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button85.setFont(font)
        self.Button85.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button85.setObjectName(_fromUtf8("Button85"))
        self.Button69 = QtGui.QPushButton(self.pageSpecial)
        self.Button69.setGeometry(QtCore.QRect(96, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button69.setFont(font)
        self.Button69.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button69.setObjectName(_fromUtf8("Button69"))
        self.Button81 = QtGui.QPushButton(self.pageSpecial)
        self.Button81.setGeometry(QtCore.QRect(192, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button81.setFont(font)
        self.Button81.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button81.setObjectName(_fromUtf8("Button81"))
        self.Button67 = QtGui.QPushButton(self.pageSpecial)
        self.Button67.setGeometry(QtCore.QRect(0, 60, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button67.setFont(font)
        self.Button67.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button67.setObjectName(_fromUtf8("Button67"))
        self.Button80 = QtGui.QPushButton(self.pageSpecial)
        self.Button80.setGeometry(QtCore.QRect(144, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button80.setFont(font)
        self.Button80.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button80.setObjectName(_fromUtf8("Button80"))
        self.Button76 = QtGui.QPushButton(self.pageSpecial)
        self.Button76.setGeometry(QtCore.QRect(240, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button76.setFont(font)
        self.Button76.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button76.setObjectName(_fromUtf8("Button76"))
        self.Button75 = QtGui.QPushButton(self.pageSpecial)
        self.Button75.setGeometry(QtCore.QRect(192, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button75.setFont(font)
        self.Button75.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button75.setObjectName(_fromUtf8("Button75"))
        self.Button86 = QtGui.QPushButton(self.pageSpecial)
        self.Button86.setGeometry(QtCore.QRect(432, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button86.setFont(font)
        self.Button86.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button86.setObjectName(_fromUtf8("Button86"))
        self.Button90 = QtGui.QPushButton(self.pageSpecial)
        self.Button90.setGeometry(QtCore.QRect(384, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button90.setFont(font)
        self.Button90.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button90.setObjectName(_fromUtf8("Button90"))
        self.Button91 = QtGui.QPushButton(self.pageSpecial)
        self.Button91.setGeometry(QtCore.QRect(192, 180, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button91.setFont(font)
        self.Button91.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button91.setObjectName(_fromUtf8("Button91"))
        self.Button92 = QtGui.QPushButton(self.pageSpecial)
        self.Button92.setGeometry(QtCore.QRect(240, 180, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button92.setFont(font)
        self.Button92.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button92.setObjectName(_fromUtf8("Button92"))
        self.Button93 = QtGui.QPushButton(self.pageSpecial)
        self.Button93.setGeometry(QtCore.QRect(0, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button93.setFont(font)
        self.Button93.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button93.setObjectName(_fromUtf8("Button93"))
        self.Button87 = QtGui.QPushButton(self.pageSpecial)
        self.Button87.setGeometry(QtCore.QRect(96, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button87.setFont(font)
        self.Button87.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button87.setObjectName(_fromUtf8("Button87"))
        self.Button88 = QtGui.QPushButton(self.pageSpecial)
        self.Button88.setGeometry(QtCore.QRect(144, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button88.setFont(font)
        self.Button88.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button88.setObjectName(_fromUtf8("Button88"))
        self.Button89 = QtGui.QPushButton(self.pageSpecial)
        self.Button89.setGeometry(QtCore.QRect(432, 120, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button89.setFont(font)
        self.Button89.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button89.setObjectName(_fromUtf8("Button89"))
        self.Button94 = QtGui.QPushButton(self.pageSpecial)
        self.Button94.setGeometry(QtCore.QRect(48, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button94.setFont(font)
        self.Button94.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button94.setObjectName(_fromUtf8("Button94"))
        self.ButtonBackSpecial = QtGui.QPushButton(self.pageSpecial)
        self.ButtonBackSpecial.setGeometry(QtCore.QRect(0, 180, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonBackSpecial.setFont(font)
        self.ButtonBackSpecial.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonBackSpecial.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/back-arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonBackSpecial.setIcon(icon3)
        self.ButtonBackSpecial.setIconSize(QtCore.QSize(35, 35))
        self.ButtonBackSpecial.setObjectName(_fromUtf8("ButtonBackSpecial"))
        self.Button27_3 = QtGui.QPushButton(self.pageSpecial)
        self.Button27_3.setGeometry(QtCore.QRect(288, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button27_3.setFont(font)
        self.Button27_3.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top:none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button27_3.setObjectName(_fromUtf8("Button27_3"))
        self.ButtonBackspaceSpecial = QtGui.QPushButton(self.pageSpecial)
        self.ButtonBackspaceSpecial.setGeometry(QtCore.QRect(384, 60, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.ButtonBackspaceSpecial.setFont(font)
        self.ButtonBackspaceSpecial.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonBackspaceSpecial.setText(_fromUtf8(""))
        self.ButtonBackspaceSpecial.setIcon(icon1)
        self.ButtonBackspaceSpecial.setIconSize(QtCore.QSize(25, 25))
        self.ButtonBackspaceSpecial.setObjectName(_fromUtf8("ButtonBackspaceSpecial"))
        self.ButtonNumericSpecial = QtGui.QPushButton(self.pageSpecial)
        self.ButtonNumericSpecial.setGeometry(QtCore.QRect(96, 180, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonNumericSpecial.setFont(font)
        self.ButtonNumericSpecial.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonNumericSpecial.setObjectName(_fromUtf8("ButtonNumericSpecial"))
        self.ButtonSpaceSpecial = QtGui.QPushButton(self.pageSpecial)
        self.ButtonSpaceSpecial.setGeometry(QtCore.QRect(288, 180, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonSpaceSpecial.setFont(font)
        self.ButtonSpaceSpecial.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonSpaceSpecial.setObjectName(_fromUtf8("ButtonSpaceSpecial"))
        self.Button56_3 = QtGui.QPushButton(self.pageSpecial)
        self.Button56_3.setGeometry(QtCore.QRect(336, 0, 48, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button56_3.setFont(font)
        self.Button56_3.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button56_3.setObjectName(_fromUtf8("Button56_3"))
        self.ButtonSubmitSpecial = QtGui.QPushButton(self.pageSpecial)
        self.ButtonSubmitSpecial.setGeometry(QtCore.QRect(384, 180, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonSubmitSpecial.setFont(font)
        self.ButtonSubmitSpecial.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonSubmitSpecial.setText(_fromUtf8(""))
        self.ButtonSubmitSpecial.setIcon(icon2)
        self.ButtonSubmitSpecial.setIconSize(QtCore.QSize(35, 35))
        self.ButtonSubmitSpecial.setObjectName(_fromUtf8("ButtonSubmitSpecial"))
        self.Button92.raise_()
        self.Button89.raise_()
        self.Button85.raise_()
        self.Button94.raise_()
        self.Button83.raise_()
        self.Button68.raise_()
        self.Button72.raise_()
        self.ButtonNumericSpecial.raise_()
        self.Button93.raise_()
        self.Button79.raise_()
        self.Button71.raise_()
        self.Button56_3.raise_()
        self.ButtonBackspaceSpecial.raise_()
        self.Button82.raise_()
        self.Button80.raise_()
        self.Button74.raise_()
        self.Button75.raise_()
        self.Button77.raise_()
        self.Button91.raise_()
        self.Button69.raise_()
        self.Button90.raise_()
        self.Button67.raise_()
        self.Button81.raise_()
        self.Button27_3.raise_()
        self.Button76.raise_()
        self.Button84.raise_()
        self.Button70.raise_()
        self.ButtonBackSpecial.raise_()
        self.ButtonSpaceSpecial.raise_()
        self.Button73.raise_()
        self.Button88.raise_()
        self.Button87.raise_()
        self.Button78.raise_()
        self.Button86.raise_()
        self.ButtonSubmitSpecial.raise_()
        self.stackedWidget.addWidget(self.pageSpecial)
        self.pageNumeric = QtGui.QWidget()
        self.pageNumeric.setObjectName(_fromUtf8("pageNumeric"))
        self.Button58 = QtGui.QPushButton(self.pageNumeric)
        self.Button58.setGeometry(QtCore.QRect(96, 0, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button58.setFont(font)
        self.Button58.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button58.setObjectName(_fromUtf8("Button58"))
        self.Button57 = QtGui.QPushButton(self.pageNumeric)
        self.Button57.setGeometry(QtCore.QRect(0, 0, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button57.setFont(font)
        self.Button57.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button57.setObjectName(_fromUtf8("Button57"))
        self.Button65 = QtGui.QPushButton(self.pageNumeric)
        self.Button65.setGeometry(QtCore.QRect(192, 120, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button65.setFont(font)
        self.Button65.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button65.setObjectName(_fromUtf8("Button65"))
        self.Button62 = QtGui.QPushButton(self.pageNumeric)
        self.Button62.setGeometry(QtCore.QRect(192, 60, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button62.setFont(font)
        self.Button62.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button62.setObjectName(_fromUtf8("Button62"))
        self.Button63 = QtGui.QPushButton(self.pageNumeric)
        self.Button63.setGeometry(QtCore.QRect(0, 120, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button63.setFont(font)
        self.Button63.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button63.setObjectName(_fromUtf8("Button63"))
        self.Button61 = QtGui.QPushButton(self.pageNumeric)
        self.Button61.setGeometry(QtCore.QRect(96, 60, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button61.setFont(font)
        self.Button61.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button61.setObjectName(_fromUtf8("Button61"))
        self.Button59 = QtGui.QPushButton(self.pageNumeric)
        self.Button59.setGeometry(QtCore.QRect(192, 0, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button59.setFont(font)
        self.Button59.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button59.setObjectName(_fromUtf8("Button59"))
        self.Button64 = QtGui.QPushButton(self.pageNumeric)
        self.Button64.setGeometry(QtCore.QRect(96, 120, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button64.setFont(font)
        self.Button64.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button64.setObjectName(_fromUtf8("Button64"))
        self.Button66 = QtGui.QPushButton(self.pageNumeric)
        self.Button66.setGeometry(QtCore.QRect(192, 180, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button66.setFont(font)
        self.Button66.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button66.setObjectName(_fromUtf8("Button66"))
        self.Button60 = QtGui.QPushButton(self.pageNumeric)
        self.Button60.setGeometry(QtCore.QRect(0, 60, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button60.setFont(font)
        self.Button60.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button60.setObjectName(_fromUtf8("Button60"))
        self.ButtonBackNumeric = QtGui.QPushButton(self.pageNumeric)
        self.ButtonBackNumeric.setGeometry(QtCore.QRect(0, 180, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonBackNumeric.setFont(font)
        self.ButtonBackNumeric.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonBackNumeric.setText(_fromUtf8(""))
        self.ButtonBackNumeric.setIcon(icon3)
        self.ButtonBackNumeric.setIconSize(QtCore.QSize(35, 35))
        self.ButtonBackNumeric.setObjectName(_fromUtf8("ButtonBackNumeric"))
        self.Button27_2 = QtGui.QPushButton(self.pageNumeric)
        self.Button27_2.setGeometry(QtCore.QRect(288, 0, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Button27_2.setFont(font)
        self.Button27_2.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button27_2.setObjectName(_fromUtf8("Button27_2"))
        self.ButtonSpecialNumeric = QtGui.QPushButton(self.pageNumeric)
        self.ButtonSpecialNumeric.setGeometry(QtCore.QRect(96, 180, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonSpecialNumeric.setFont(font)
        self.ButtonSpecialNumeric.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonSpecialNumeric.setObjectName(_fromUtf8("ButtonSpecialNumeric"))
        self.Button74_2 = QtGui.QPushButton(self.pageNumeric)
        self.Button74_2.setGeometry(QtCore.QRect(288, 60, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button74_2.setFont(font)
        self.Button74_2.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button74_2.setObjectName(_fromUtf8("Button74_2"))
        self.Button79_2 = QtGui.QPushButton(self.pageNumeric)
        self.Button79_2.setGeometry(QtCore.QRect(288, 120, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button79_2.setFont(font)
        self.Button79_2.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button79_2.setObjectName(_fromUtf8("Button79_2"))
        self.Button69_2 = QtGui.QPushButton(self.pageNumeric)
        self.Button69_2.setGeometry(QtCore.QRect(288, 180, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button69_2.setFont(font)
        self.Button69_2.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button69_2.setObjectName(_fromUtf8("Button69_2"))
        self.ButtonSubmitNumeric = QtGui.QPushButton(self.pageNumeric)
        self.ButtonSubmitNumeric.setGeometry(QtCore.QRect(384, 180, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonSubmitNumeric.setFont(font)
        self.ButtonSubmitNumeric.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonSubmitNumeric.setText(_fromUtf8(""))
        self.ButtonSubmitNumeric.setIcon(icon2)
        self.ButtonSubmitNumeric.setIconSize(QtCore.QSize(35, 35))
        self.ButtonSubmitNumeric.setObjectName(_fromUtf8("ButtonSubmitNumeric"))
        self.ButtonSpaceNumeric = QtGui.QPushButton(self.pageNumeric)
        self.ButtonSpaceNumeric.setGeometry(QtCore.QRect(384, 60, 96, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonSpaceNumeric.setFont(font)
        self.ButtonSpaceNumeric.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonSpaceNumeric.setObjectName(_fromUtf8("ButtonSpaceNumeric"))
        self.ButtonBackspaceNumeric = QtGui.QPushButton(self.pageNumeric)
        self.ButtonBackspaceNumeric.setGeometry(QtCore.QRect(384, 0, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonBackspaceNumeric.setFont(font)
        self.ButtonBackspaceNumeric.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonBackspaceNumeric.setText(_fromUtf8(""))
        self.ButtonBackspaceNumeric.setIcon(icon1)
        self.ButtonBackspaceNumeric.setIconSize(QtCore.QSize(35, 35))
        self.ButtonBackspaceNumeric.setObjectName(_fromUtf8("ButtonBackspaceNumeric"))
        self.Button56_2 = QtGui.QPushButton(self.pageNumeric)
        self.Button56_2.setGeometry(QtCore.QRect(384, 120, 96, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button56_2.setFont(font)
        self.Button56_2.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.Button56_2.setObjectName(_fromUtf8("Button56_2"))
        self.stackedWidget.addWidget(self.pageNumeric)
        self.ButtonCursorLeft = QtGui.QPushButton(Form)
        self.ButtonCursorLeft.setGeometry(QtCore.QRect(288, 0, 96, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonCursorLeft.setFont(font)
        self.ButtonCursorLeft.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonCursorLeft.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/arrows-4.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonCursorLeft.setIcon(icon4)
        self.ButtonCursorLeft.setIconSize(QtCore.QSize(45, 45))
        self.ButtonCursorLeft.setObjectName(_fromUtf8("ButtonCursorLeft"))
        self.ButtonCursorRight = QtGui.QPushButton(Form)
        self.ButtonCursorRight.setGeometry(QtCore.QRect(384, 0, 96, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonCursorRight.setFont(font)
        self.ButtonCursorRight.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.ButtonCursorRight.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/arrows-2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonCursorRight.setIcon(icon5)
        self.ButtonCursorRight.setIconSize(QtCore.QSize(45, 45))
        self.ButtonCursorRight.setObjectName(_fromUtf8("ButtonCursorRight"))

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gotham\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">ENTER TEXT ...</span></p></body></html>", None))
        self.Button1.setText(_translate("Form", "Q", None))
        self.Button11.setText(_translate("Form", "A", None))
        self.Button2.setText(_translate("Form", "W", None))
        self.Button12.setText(_translate("Form", "S", None))
        self.Button20.setText(_translate("Form", "Z", None))
        self.Button3.setText(_translate("Form", "E", None))
        self.Button13.setText(_translate("Form", "D", None))
        self.Button21.setText(_translate("Form", "X", None))
        self.Button4.setText(_translate("Form", "R", None))
        self.Button14.setText(_translate("Form", "F", None))
        self.Button22.setText(_translate("Form", "C", None))
        self.Button5.setText(_translate("Form", "T", None))
        self.Button15.setText(_translate("Form", "G", None))
        self.Button23.setText(_translate("Form", "V", None))
        self.Button6.setText(_translate("Form", "Y", None))
        self.Button16.setText(_translate("Form", "H", None))
        self.Button24.setText(_translate("Form", "B", None))
        self.Button7.setText(_translate("Form", "U", None))
        self.Button17.setText(_translate("Form", "J", None))
        self.Button25.setText(_translate("Form", "N", None))
        self.Button8.setText(_translate("Form", "I", None))
        self.Button18.setText(_translate("Form", "K", None))
        self.Button26.setText(_translate("Form", "M", None))
        self.Button9.setText(_translate("Form", "O", None))
        self.Button19.setText(_translate("Form", "L", None))
        self.Button27.setText(_translate("Form", ".", None))
        self.Button10.setText(_translate("Form", "P", None))
        self.Button28.setText(_translate("Form", ",", None))
        self.ButtonSpecialAlphaU.setText(_translate("Form", "@#!", None))
        self.ButtonSpaceAlphaU.setText(_translate("Form", "Space", None))
        self.ButtonNumericAlphaU.setText(_translate("Form", "123", None))
        self.Button48.setText(_translate("Form", "z", None))
        self.Button52.setText(_translate("Form", "b", None))
        self.Button42.setText(_translate("Form", "f", None))
        self.Button54.setText(_translate("Form", "m", None))
        self.Button35.setText(_translate("Form", "u", None))
        self.Button45.setText(_translate("Form", "j", None))
        self.Button53.setText(_translate("Form", "n", None))
        self.Button33.setText(_translate("Form", "t", None))
        self.Button43.setText(_translate("Form", "g", None))
        self.Button40.setText(_translate("Form", "s", None))
        self.Button29.setText(_translate("Form", "q", None))
        self.Button30.setText(_translate("Form", "w", None))
        self.Button38.setText(_translate("Form", "p", None))
        self.Button49.setText(_translate("Form", "x", None))
        self.Button31.setText(_translate("Form", "e", None))
        self.Button32.setText(_translate("Form", "r", None))
        self.Button44.setText(_translate("Form", "h", None))
        self.Button37.setText(_translate("Form", "o", None))
        self.Button46.setText(_translate("Form", "k", None))
        self.Button55.setText(_translate("Form", ".", None))
        self.Button41.setText(_translate("Form", "d", None))
        self.Button51.setText(_translate("Form", "v", None))
        self.Button36.setText(_translate("Form", "i", None))
        self.Button39.setText(_translate("Form", "a", None))
        self.Button50.setText(_translate("Form", "c", None))
        self.Button34.setText(_translate("Form", "y", None))
        self.Button47.setText(_translate("Form", "l", None))
        self.Button56.setText(_translate("Form", ",", None))
        self.ButtonSpaceAlpha.setText(_translate("Form", "Space", None))
        self.ButtonNumericAlpha.setText(_translate("Form", "123", None))
        self.ButtonSpecialAlpha.setText(_translate("Form", "@#!", None))
        self.Button78.setText(_translate("Form", "_", None))
        self.Button82.setText(_translate("Form", ">", None))
        self.Button70.setText(_translate("Form", "$", None))
        self.Button84.setText(_translate("Form", "{", None))
        self.Button73.setText(_translate("Form", "&&", None))
        self.Button83.setText(_translate("Form", "?", None))
        self.Button71.setText(_translate("Form", "%", None))
        self.Button68.setText(_translate("Form", "@", None))
        self.Button77.setText(_translate("Form", "-", None))
        self.Button79.setText(_translate("Form", "+", None))
        self.Button72.setText(_translate("Form", "^", None))
        self.Button74.setText(_translate("Form", "*", None))
        self.Button85.setText(_translate("Form", "}", None))
        self.Button69.setText(_translate("Form", "#", None))
        self.Button81.setText(_translate("Form", "<", None))
        self.Button67.setText(_translate("Form", "!", None))
        self.Button80.setText(_translate("Form", "=", None))
        self.Button76.setText(_translate("Form", ")", None))
        self.Button75.setText(_translate("Form", "(", None))
        self.Button86.setText(_translate("Form", "/", None))
        self.Button90.setText(_translate("Form", "\\", None))
        self.Button91.setText(_translate("Form", "[", None))
        self.Button92.setText(_translate("Form", "]", None))
        self.Button93.setText(_translate("Form", "\"", None))
        self.Button87.setText(_translate("Form", ";", None))
        self.Button88.setText(_translate("Form", ":", None))
        self.Button89.setText(_translate("Form", "|", None))
        self.Button94.setText(_translate("Form", "\'", None))
        self.Button27_3.setText(_translate("Form", ".", None))
        self.ButtonNumericSpecial.setText(_translate("Form", "123", None))
        self.ButtonSpaceSpecial.setText(_translate("Form", "Space", None))
        self.Button56_3.setText(_translate("Form", ",", None))
        self.Button58.setText(_translate("Form", "2", None))
        self.Button57.setText(_translate("Form", "1", None))
        self.Button65.setText(_translate("Form", "9", None))
        self.Button62.setText(_translate("Form", "6", None))
        self.Button63.setText(_translate("Form", "7", None))
        self.Button61.setText(_translate("Form", "5", None))
        self.Button59.setText(_translate("Form", "3", None))
        self.Button64.setText(_translate("Form", "8", None))
        self.Button66.setText(_translate("Form", "0", None))
        self.Button60.setText(_translate("Form", "4", None))
        self.Button27_2.setText(_translate("Form", ".", None))
        self.ButtonSpecialNumeric.setText(_translate("Form", "@#!", None))
        self.Button74_2.setText(_translate("Form", "*", None))
        self.Button79_2.setText(_translate("Form", "+", None))
        self.Button69_2.setText(_translate("Form", "#", None))
        self.ButtonSpaceNumeric.setText(_translate("Form", "Space", None))
        self.Button56_2.setText(_translate("Form", ",", None))

