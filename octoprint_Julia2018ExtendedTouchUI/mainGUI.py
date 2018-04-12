# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Test2.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(480, 320)
        MainWindow.setMinimumSize(QtCore.QSize(480, 320))
        MainWindow.setMaximumSize(QtCore.QSize(480, 320))
        MainWindow.setStyleSheet(_fromUtf8("QStatusBar {\n"
"    background-color: rgb(49, 49, 49);\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"}"))
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.mainApplication = QtGui.QWidget(MainWindow)
        self.mainApplication.setObjectName(_fromUtf8("mainApplication"))
        self.stackedWidget = QtGui.QStackedWidget(self.mainApplication)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.stackedWidget.setMinimumSize(QtCore.QSize(480, 320))
        self.stackedWidget.setMaximumSize(QtCore.QSize(480, 320))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.stackedWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(40, 40, 40);"))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.loadingPage = QtGui.QWidget()
        self.loadingPage.setObjectName(_fromUtf8("loadingPage"))
        self.LoadingLabel = QtGui.QLabel(self.loadingPage)
        self.LoadingLabel.setGeometry(QtCore.QRect(0, 0, 481, 321))
        self.LoadingLabel.setText(_fromUtf8(""))
        self.LoadingLabel.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/splash.png")))
        self.LoadingLabel.setObjectName(_fromUtf8("LoadingLabel"))
        self.loadingGif = QtGui.QLabel(self.loadingPage)
        self.loadingGif.setGeometry(QtCore.QRect(210, 210, 50, 50))
        self.loadingGif.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255,0);"))
        self.loadingGif.setText(_fromUtf8(""))
        self.loadingGif.setScaledContents(True)
        self.loadingGif.setObjectName(_fromUtf8("loadingGif"))
        self.stackedWidget.addWidget(self.loadingPage)
        self.homePage = QtGui.QWidget()
        self.homePage.setObjectName(_fromUtf8("homePage"))
        self.playPauseButton = QtGui.QPushButton(self.homePage)
        self.playPauseButton.setGeometry(QtCore.QRect(220, 240, 131, 61))
        self.playPauseButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        self.playPauseButton.setFont(font)
        self.playPauseButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
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
        self.playPauseButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/play-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/pause-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.playPauseButton.setIcon(icon)
        self.playPauseButton.setIconSize(QtCore.QSize(30, 30))
        self.playPauseButton.setCheckable(True)
        self.playPauseButton.setChecked(False)
        self.playPauseButton.setAutoDefault(False)
        self.playPauseButton.setDefault(False)
        self.playPauseButton.setFlat(False)
        self.playPauseButton.setObjectName(_fromUtf8("playPauseButton"))
        self.stopButton = QtGui.QPushButton(self.homePage)
        self.stopButton.setGeometry(QtCore.QRect(350, 240, 131, 61))
        self.stopButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.stopButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/video-player-stop-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setIconSize(QtCore.QSize(25, 25))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.line = QtGui.QFrame(self.homePage)
        self.line.setGeometry(QtCore.QRect(260, 90, 20, 111))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.tool0Label = QtGui.QLabel(self.homePage)
        self.tool0Label.setGeometry(QtCore.QRect(40, 98, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0Label.setFont(font)
        self.tool0Label.setStyleSheet(_fromUtf8("\n"
"   color:  white;"))
        self.tool0Label.setText(_fromUtf8(""))
        self.tool0Label.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Nozzle.png")))
        self.tool0Label.setScaledContents(True)
        self.tool0Label.setObjectName(_fromUtf8("tool0Label"))
        self.FileNameLabel = QtGui.QLabel(self.homePage)
        self.FileNameLabel.setGeometry(QtCore.QRect(0, 170, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.FileNameLabel.setFont(font)
        self.FileNameLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.FileNameLabel.setObjectName(_fromUtf8("FileNameLabel"))
        self.printTimeLabel = QtGui.QLabel(self.homePage)
        self.printTimeLabel.setGeometry(QtCore.QRect(0, 190, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.printTimeLabel.setFont(font)
        self.printTimeLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.printTimeLabel.setObjectName(_fromUtf8("printTimeLabel"))
        self.fileName = QtGui.QLabel(self.homePage)
        self.fileName.setGeometry(QtCore.QRect(40, 170, 211, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        self.fileName.setFont(font)
        self.fileName.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.fileName.setScaledContents(True)
        self.fileName.setWordWrap(False)
        self.fileName.setObjectName(_fromUtf8("fileName"))
        self.printTime = QtGui.QLabel(self.homePage)
        self.printTime.setGeometry(QtCore.QRect(100, 190, 181, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        self.printTime.setFont(font)
        self.printTime.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.printTime.setObjectName(_fromUtf8("printTime"))
        self.timeLeftLabel = QtGui.QLabel(self.homePage)
        self.timeLeftLabel.setGeometry(QtCore.QRect(0, 210, 181, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.timeLeftLabel.setFont(font)
        self.timeLeftLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.timeLeftLabel.setObjectName(_fromUtf8("timeLeftLabel"))
        self.tool0TargetTemperature = QtGui.QLabel(self.homePage)
        self.tool0TargetTemperature.setGeometry(QtCore.QRect(40, 70, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0TargetTemperature.setFont(font)
        self.tool0TargetTemperature.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.tool0TargetTemperature.setObjectName(_fromUtf8("tool0TargetTemperature"))
        self.tool0TempBar = QtGui.QProgressBar(self.homePage)
        self.tool0TempBar.setGeometry(QtCore.QRect(80, 80, 16, 71))
        self.tool0TempBar.setStyleSheet(_fromUtf8("QProgressBar::chunk {\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.522, y2:0, stop:0.0336134 rgba(74, 183, 255, 255), stop:1 rgba(53, 173, 242, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"}\n"
""))
        self.tool0TempBar.setMaximum(300)
        self.tool0TempBar.setProperty("value", 100)
        self.tool0TempBar.setAlignment(QtCore.Qt.AlignCenter)
        self.tool0TempBar.setTextVisible(False)
        self.tool0TempBar.setOrientation(QtCore.Qt.Vertical)
        self.tool0TempBar.setObjectName(_fromUtf8("tool0TempBar"))
        self.tool0ActualTemperature = QtGui.QLabel(self.homePage)
        self.tool0ActualTemperature.setGeometry(QtCore.QRect(35, 140, 71, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0ActualTemperature.setFont(font)
        self.tool0ActualTemperature.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(0, 0, 0, 0);"))
        self.tool0ActualTemperature.setObjectName(_fromUtf8("tool0ActualTemperature"))
        self.menuButton = QtGui.QPushButton(self.homePage)
        self.menuButton.setGeometry(QtCore.QRect(0, 240, 111, 61))
        self.menuButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(13)
        self.menuButton.setFont(font)
        self.menuButton.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.menuButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/menu.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton.setIcon(icon2)
        self.menuButton.setIconSize(QtCore.QSize(40, 40))
        self.menuButton.setCheckable(False)
        self.menuButton.setAutoDefault(False)
        self.menuButton.setDefault(False)
        self.menuButton.setFlat(False)
        self.menuButton.setObjectName(_fromUtf8("menuButton"))
        self.printPreviewMain = QtGui.QLabel(self.homePage)
        self.printPreviewMain.setGeometry(QtCore.QRect(280, 49, 191, 191))
        self.printPreviewMain.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.printPreviewMain.setText(_fromUtf8(""))
        self.printPreviewMain.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/thumbnail.png")))
        self.printPreviewMain.setScaledContents(True)
        self.printPreviewMain.setObjectName(_fromUtf8("printPreviewMain"))
        self.printProgressBar = QtGui.QProgressBar(self.homePage)
        self.printProgressBar.setGeometry(QtCore.QRect(0, 300, 481, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.printProgressBar.setFont(font)
        self.printProgressBar.setStyleSheet(_fromUtf8("QProgressBar::chunk {\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:0, y2:0.534, stop:0 rgba(130, 203, 117, 255), stop:1 rgba(66, 191, 85, 255));\n"
"border: 1px solid green;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
" /*  border-bottom-left-radius: 10px;\n"
" border-bottom-right-radius: 10px;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(180, 180, 180, 255));\n"
"}\n"
""))
        self.printProgressBar.setMaximum(100)
        self.printProgressBar.setProperty("value", 0)
        self.printProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.printProgressBar.setTextVisible(True)
        self.printProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.printProgressBar.setObjectName(_fromUtf8("printProgressBar"))
        self.timeLeft = QtGui.QLabel(self.homePage)
        self.timeLeft.setGeometry(QtCore.QRect(110, 210, 181, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        self.timeLeft.setFont(font)
        self.timeLeft.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.timeLeft.setWordWrap(False)
        self.timeLeft.setObjectName(_fromUtf8("timeLeft"))
        self.printerStatus = QtGui.QLabel(self.homePage)
        self.printerStatus.setGeometry(QtCore.QRect(40, 0, 441, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.printerStatus.setFont(font)
        self.printerStatus.setStyleSheet(_fromUtf8("\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.printerStatus.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.printerStatus.setWordWrap(True)
        self.printerStatus.setObjectName(_fromUtf8("printerStatus"))
        self.controlButton = QtGui.QPushButton(self.homePage)
        self.controlButton.setGeometry(QtCore.QRect(110, 240, 111, 61))
        self.controlButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(13)
        self.controlButton.setFont(font)
        self.controlButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.controlButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/settings-1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.controlButton.setIcon(icon3)
        self.controlButton.setIconSize(QtCore.QSize(40, 40))
        self.controlButton.setCheckable(False)
        self.controlButton.setAutoDefault(False)
        self.controlButton.setDefault(False)
        self.controlButton.setFlat(False)
        self.controlButton.setObjectName(_fromUtf8("controlButton"))
        self.printerStatusColour = QtGui.QLabel(self.homePage)
        self.printerStatusColour.setGeometry(QtCore.QRect(5, 6, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.printerStatusColour.setFont(font)
        self.printerStatusColour.setStyleSheet(_fromUtf8("     border: 1px solid rgb(87, 87, 87);\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:0, y2:0.534, stop:0 rgba(130, 203, 117, 255), stop:1 rgba(66, 191, 85, 255));"))
        self.printerStatusColour.setText(_fromUtf8(""))
        self.printerStatusColour.setAlignment(QtCore.Qt.AlignCenter)
        self.printerStatusColour.setObjectName(_fromUtf8("printerStatusColour"))
        self.celciusLabel = QtGui.QLabel(self.homePage)
        self.celciusLabel.setGeometry(QtCore.QRect(100, 70, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.celciusLabel.setFont(font)
        self.celciusLabel.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.celciusLabel.setObjectName(_fromUtf8("celciusLabel"))
        self.statusBar = QtGui.QLabel(self.homePage)
        self.statusBar.setGeometry(QtCore.QRect(0, 0, 481, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        self.statusBar.setFont(font)
        self.statusBar.setStyleSheet(_fromUtf8("     border-bottom: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.statusBar.setFrameShape(QtGui.QFrame.NoFrame)
        self.statusBar.setFrameShadow(QtGui.QFrame.Raised)
        self.statusBar.setText(_fromUtf8(""))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.celciusLabel_2 = QtGui.QLabel(self.homePage)
        self.celciusLabel_2.setGeometry(QtCore.QRect(220, 70, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.celciusLabel_2.setFont(font)
        self.celciusLabel_2.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.celciusLabel_2.setObjectName(_fromUtf8("celciusLabel_2"))
        self.bedTempBar = QtGui.QProgressBar(self.homePage)
        self.bedTempBar.setGeometry(QtCore.QRect(205, 80, 16, 71))
        self.bedTempBar.setStyleSheet(_fromUtf8("QProgressBar::chunk {\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.522, y2:0, stop:0.0336134 rgba(74, 183, 255, 255), stop:1 rgba(53, 173, 242, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"}\n"
""))
        self.bedTempBar.setMaximum(300)
        self.bedTempBar.setProperty("value", 10)
        self.bedTempBar.setAlignment(QtCore.Qt.AlignCenter)
        self.bedTempBar.setTextVisible(False)
        self.bedTempBar.setOrientation(QtCore.Qt.Vertical)
        self.bedTempBar.setObjectName(_fromUtf8("bedTempBar"))
        self.bedActualTemperatute = QtGui.QLabel(self.homePage)
        self.bedActualTemperatute.setGeometry(QtCore.QRect(155, 140, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.bedActualTemperatute.setFont(font)
        self.bedActualTemperatute.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(0, 0, 0, 0);"))
        self.bedActualTemperatute.setObjectName(_fromUtf8("bedActualTemperatute"))
        self.bedTargetTemperature = QtGui.QLabel(self.homePage)
        self.bedTargetTemperature.setGeometry(QtCore.QRect(155, 70, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.bedTargetTemperature.setFont(font)
        self.bedTargetTemperature.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.bedTargetTemperature.setObjectName(_fromUtf8("bedTargetTemperature"))
        self.bedLabel = QtGui.QLabel(self.homePage)
        self.bedLabel.setGeometry(QtCore.QRect(150, 95, 41, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.bedLabel.setFont(font)
        self.bedLabel.setStyleSheet(_fromUtf8("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.bedLabel.setText(_fromUtf8(""))
        self.bedLabel.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/bed.png")))
        self.bedLabel.setScaledContents(True)
        self.bedLabel.setObjectName(_fromUtf8("bedLabel"))
        self.line.raise_()
        self.printPreviewMain.raise_()
        self.statusBar.raise_()
        self.playPauseButton.raise_()
        self.stopButton.raise_()
        self.tool0Label.raise_()
        self.FileNameLabel.raise_()
        self.printTimeLabel.raise_()
        self.fileName.raise_()
        self.printTime.raise_()
        self.timeLeftLabel.raise_()
        self.tool0TempBar.raise_()
        self.tool0ActualTemperature.raise_()
        self.tool0TargetTemperature.raise_()
        self.menuButton.raise_()
        self.timeLeft.raise_()
        self.controlButton.raise_()
        self.printProgressBar.raise_()
        self.printerStatus.raise_()
        self.printerStatusColour.raise_()
        self.celciusLabel.raise_()
        self.celciusLabel_2.raise_()
        self.bedTempBar.raise_()
        self.bedActualTemperatute.raise_()
        self.bedTargetTemperature.raise_()
        self.bedLabel.raise_()
        self.stackedWidget.addWidget(self.homePage)
        self.MenuPage = QtGui.QWidget()
        self.MenuPage.setObjectName(_fromUtf8("MenuPage"))
        self.menuBackButton = QtGui.QPushButton(self.MenuPage)
        self.menuBackButton.setGeometry(QtCore.QRect(320, 160, 160, 160))
        self.menuBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.menuBackButton.setFont(font)
        self.menuBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}"))
        self.menuBackButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/arrows-4.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBackButton.setIcon(icon4)
        self.menuBackButton.setIconSize(QtCore.QSize(50, 50))
        self.menuBackButton.setCheckable(False)
        self.menuBackButton.setObjectName(_fromUtf8("menuBackButton"))
        self.menuControlButton = QtGui.QToolButton(self.MenuPage)
        self.menuControlButton.setGeometry(QtCore.QRect(160, 0, 160, 160))
        self.menuControlButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        self.menuControlButton.setFont(font)
        self.menuControlButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.menuControlButton.setIcon(icon3)
        self.menuControlButton.setIconSize(QtCore.QSize(80, 80))
        self.menuControlButton.setCheckable(False)
        self.menuControlButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.menuControlButton.setObjectName(_fromUtf8("menuControlButton"))
        self.menuPrintButton = QtGui.QToolButton(self.MenuPage)
        self.menuPrintButton.setGeometry(QtCore.QRect(0, 0, 160, 160))
        self.menuPrintButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        self.menuPrintButton.setFont(font)
        self.menuPrintButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"    padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/printer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuPrintButton.setIcon(icon5)
        self.menuPrintButton.setIconSize(QtCore.QSize(80, 80))
        self.menuPrintButton.setCheckable(False)
        self.menuPrintButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.menuPrintButton.setObjectName(_fromUtf8("menuPrintButton"))
        self.menuSettingsButton = QtGui.QToolButton(self.MenuPage)
        self.menuSettingsButton.setGeometry(QtCore.QRect(160, 160, 160, 160))
        self.menuSettingsButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        self.menuSettingsButton.setFont(font)
        self.menuSettingsButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSettingsButton.setIcon(icon6)
        self.menuSettingsButton.setIconSize(QtCore.QSize(80, 80))
        self.menuSettingsButton.setCheckable(False)
        self.menuSettingsButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.menuSettingsButton.setObjectName(_fromUtf8("menuSettingsButton"))
        self.menuCartButton = QtGui.QToolButton(self.MenuPage)
        self.menuCartButton.setGeometry(QtCore.QRect(0, 160, 160, 160))
        self.menuCartButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        self.menuCartButton.setFont(font)
        self.menuCartButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/cart.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCartButton.setIcon(icon7)
        self.menuCartButton.setIconSize(QtCore.QSize(80, 80))
        self.menuCartButton.setCheckable(False)
        self.menuCartButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.menuCartButton.setAutoRaise(False)
        self.menuCartButton.setObjectName(_fromUtf8("menuCartButton"))
        self.menuCaliberateButton = QtGui.QToolButton(self.MenuPage)
        self.menuCaliberateButton.setGeometry(QtCore.QRect(320, 0, 160, 160))
        self.menuCaliberateButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        self.menuCaliberateButton.setFont(font)
        self.menuCaliberateButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/reload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCaliberateButton.setIcon(icon8)
        self.menuCaliberateButton.setIconSize(QtCore.QSize(80, 80))
        self.menuCaliberateButton.setCheckable(False)
        self.menuCaliberateButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.menuCaliberateButton.setObjectName(_fromUtf8("menuCaliberateButton"))
        self.menuSettingsButton.raise_()
        self.menuControlButton.raise_()
        self.menuCartButton.raise_()
        self.menuCaliberateButton.raise_()
        self.menuBackButton.raise_()
        self.menuPrintButton.raise_()
        self.stackedWidget.addWidget(self.MenuPage)
        self.settingsPage = QtGui.QWidget()
        self.settingsPage.setObjectName(_fromUtf8("settingsPage"))
        self.scrollArea = QtGui.QScrollArea(self.settingsPage)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.scrollArea.setStyleSheet(_fromUtf8(" QScrollBar:vertical {\n"
"     border: 1px solid black;\n"
"border-radius: 5px;\n"
"    background-color: rgb(40,40,40);\n"
"     width: 80px;\n"
"     margin: 70px 0 70px 0;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 20px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height:65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height: 65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
" image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"QScrollBar::down-arrow:vertical {\n"
" image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }"))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 478, 700))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 3, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.settingsBackButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.settingsBackButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.settingsBackButton.setFont(font)
        self.settingsBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}"))
        self.settingsBackButton.setText(_fromUtf8(""))
        self.settingsBackButton.setIcon(icon4)
        self.settingsBackButton.setIconSize(QtCore.QSize(50, 50))
        self.settingsBackButton.setCheckable(False)
        self.settingsBackButton.setAutoDefault(False)
        self.settingsBackButton.setDefault(False)
        self.settingsBackButton.setFlat(False)
        self.settingsBackButton.setObjectName(_fromUtf8("settingsBackButton"))
        self.verticalLayout.addWidget(self.settingsBackButton)
        self.networkInfoButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.networkInfoButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.networkInfoButton.setFont(font)
        self.networkInfoButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.networkInfoButton.setIconSize(QtCore.QSize(40, 40))
        self.networkInfoButton.setObjectName(_fromUtf8("networkInfoButton"))
        self.verticalLayout.addWidget(self.networkInfoButton)
        self.configureWifiButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.configureWifiButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.configureWifiButton.setFont(font)
        self.configureWifiButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.configureWifiButton.setIconSize(QtCore.QSize(40, 40))
        self.configureWifiButton.setObjectName(_fromUtf8("configureWifiButton"))
        self.verticalLayout.addWidget(self.configureWifiButton)
        self.pairPhoneButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pairPhoneButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.pairPhoneButton.setFont(font)
        self.pairPhoneButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.pairPhoneButton.setIconSize(QtCore.QSize(40, 40))
        self.pairPhoneButton.setObjectName(_fromUtf8("pairPhoneButton"))
        self.verticalLayout.addWidget(self.pairPhoneButton)
        self.OTAButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.OTAButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.OTAButton.setFont(font)
        self.OTAButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.OTAButton.setIconSize(QtCore.QSize(40, 40))
        self.OTAButton.setObjectName(_fromUtf8("OTAButton"))
        self.verticalLayout.addWidget(self.OTAButton)
        self.caliberateTouch = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.caliberateTouch.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.caliberateTouch.setFont(font)
        self.caliberateTouch.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.caliberateTouch.setIconSize(QtCore.QSize(40, 40))
        self.caliberateTouch.setObjectName(_fromUtf8("caliberateTouch"))
        self.verticalLayout.addWidget(self.caliberateTouch)
        self.versionButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.versionButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.versionButton.setFont(font)
        self.versionButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.versionButton.setIconSize(QtCore.QSize(40, 40))
        self.versionButton.setObjectName(_fromUtf8("versionButton"))
        self.verticalLayout.addWidget(self.versionButton)
        self.restorePrintSettingsButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.restorePrintSettingsButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.restorePrintSettingsButton.setFont(font)
        self.restorePrintSettingsButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.restorePrintSettingsButton.setIconSize(QtCore.QSize(40, 40))
        self.restorePrintSettingsButton.setObjectName(_fromUtf8("restorePrintSettingsButton"))
        self.verticalLayout.addWidget(self.restorePrintSettingsButton)
        self.restoreFactoryDefaultsButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.restoreFactoryDefaultsButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.restoreFactoryDefaultsButton.setFont(font)
        self.restoreFactoryDefaultsButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.restoreFactoryDefaultsButton.setIconSize(QtCore.QSize(40, 40))
        self.restoreFactoryDefaultsButton.setObjectName(_fromUtf8("restoreFactoryDefaultsButton"))
        self.verticalLayout.addWidget(self.restoreFactoryDefaultsButton)
        self.restartButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.restartButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.restartButton.setFont(font)
        self.restartButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.restartButton.setIconSize(QtCore.QSize(40, 40))
        self.restartButton.setObjectName(_fromUtf8("restartButton"))
        self.verticalLayout.addWidget(self.restartButton)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.settingsPage)
        self.QRCodePage = QtGui.QWidget()
        self.QRCodePage.setObjectName(_fromUtf8("QRCodePage"))
        self.QRCodeBackButton = QtGui.QPushButton(self.QRCodePage)
        self.QRCodeBackButton.setGeometry(QtCore.QRect(0, 250, 481, 71))
        self.QRCodeBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.QRCodeBackButton.setFont(font)
        self.QRCodeBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}"))
        self.QRCodeBackButton.setText(_fromUtf8(""))
        self.QRCodeBackButton.setIcon(icon4)
        self.QRCodeBackButton.setIconSize(QtCore.QSize(50, 50))
        self.QRCodeBackButton.setCheckable(False)
        self.QRCodeBackButton.setAutoDefault(False)
        self.QRCodeBackButton.setDefault(False)
        self.QRCodeBackButton.setFlat(False)
        self.QRCodeBackButton.setObjectName(_fromUtf8("QRCodeBackButton"))
        self.QRCodeBackground = QtGui.QLabel(self.QRCodePage)
        self.QRCodeBackground.setGeometry(QtCore.QRect(120, 0, 251, 251))
        self.QRCodeBackground.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.QRCodeBackground.setText(_fromUtf8(""))
        self.QRCodeBackground.setObjectName(_fromUtf8("QRCodeBackground"))
        self.QRCodeLabel = QtGui.QLabel(self.QRCodePage)
        self.QRCodeLabel.setGeometry(QtCore.QRect(120, 0, 251, 251))
        self.QRCodeLabel.setStyleSheet(_fromUtf8(""))
        self.QRCodeLabel.setText(_fromUtf8(""))
        self.QRCodeLabel.setScaledContents(True)
        self.QRCodeLabel.setObjectName(_fromUtf8("QRCodeLabel"))
        self.QRCodeBackground.raise_()
        self.QRCodeLabel.raise_()
        self.QRCodeBackButton.raise_()
        self.stackedWidget.addWidget(self.QRCodePage)
        self.wifiSettingsPage = QtGui.QWidget()
        self.wifiSettingsPage.setObjectName(_fromUtf8("wifiSettingsPage"))
        self.wifiSettingsComboBox = QtGui.QComboBox(self.wifiSettingsPage)
        self.wifiSettingsComboBox.setGeometry(QtCore.QRect(0, 40, 421, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.wifiSettingsComboBox.setFont(font)
        self.wifiSettingsComboBox.setStyleSheet(_fromUtf8(" QScrollBar:vertical {\n"
"     border: 1px solid black;\n"
"border-radius: 5px;\n"
"    background-color: rgb(40,40,40);\n"
"     width: 60px;\n"
"     margin: 67px 0 67px 0;\n"
" }\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 7px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height:65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height: 65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
" image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"QScrollBar::down-arrow:vertical {\n"
" image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QComboBox {\n"
"border: 1px solid black;\n"
"    padding: 0px 18px 0px 3px;\n"
"    min-width: 6em;\n"
"\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 50px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"\n"
"image: url(./templates/img/arrows-5.png);\n"
"width: 30px;\n"
"height: 30px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(40, 40, 40);\n"
"    background: white;\n"
"}"))
        self.wifiSettingsComboBox.setEditable(False)
        self.wifiSettingsComboBox.setMaxVisibleItems(8)
        self.wifiSettingsComboBox.setIconSize(QtCore.QSize(30, 30))
        self.wifiSettingsComboBox.setObjectName(_fromUtf8("wifiSettingsComboBox"))
        self.ssidlabel = QtGui.QLabel(self.wifiSettingsPage)
        self.ssidlabel.setGeometry(QtCore.QRect(0, 0, 461, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ssidlabel.setFont(font)
        self.ssidlabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.ssidlabel.setObjectName(_fromUtf8("ssidlabel"))
        self.passwordlabel = QtGui.QLabel(self.wifiSettingsPage)
        self.passwordlabel.setGeometry(QtCore.QRect(0, 130, 461, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.passwordlabel.setFont(font)
        self.passwordlabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.passwordlabel.setObjectName(_fromUtf8("passwordlabel"))
        self.wifiSettingsDoneButton = QtGui.QPushButton(self.wifiSettingsPage)
        self.wifiSettingsDoneButton.setGeometry(QtCore.QRect(0, 230, 251, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.wifiSettingsDoneButton.setFont(font)
        self.wifiSettingsDoneButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.wifiSettingsDoneButton.setIconSize(QtCore.QSize(40, 40))
        self.wifiSettingsDoneButton.setObjectName(_fromUtf8("wifiSettingsDoneButton"))
        self.wifiSettingsCancelButton = QtGui.QPushButton(self.wifiSettingsPage)
        self.wifiSettingsCancelButton.setGeometry(QtCore.QRect(250, 230, 231, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.wifiSettingsCancelButton.setFont(font)
        self.wifiSettingsCancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.wifiSettingsCancelButton.setIconSize(QtCore.QSize(40, 40))
        self.wifiSettingsCancelButton.setObjectName(_fromUtf8("wifiSettingsCancelButton"))
        self.wifiSettingsSSIDKeyboardButton = QtGui.QPushButton(self.wifiSettingsPage)
        self.wifiSettingsSSIDKeyboardButton.setGeometry(QtCore.QRect(419, 40, 62, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(19)
        self.wifiSettingsSSIDKeyboardButton.setFont(font)
        self.wifiSettingsSSIDKeyboardButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.wifiSettingsSSIDKeyboardButton.setIconSize(QtCore.QSize(40, 40))
        self.wifiSettingsSSIDKeyboardButton.setObjectName(_fromUtf8("wifiSettingsSSIDKeyboardButton"))
        self.hiddenCheckBox = QtGui.QCheckBox(self.wifiSettingsPage)
        self.hiddenCheckBox.setGeometry(QtCore.QRect(0, 90, 161, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        self.hiddenCheckBox.setFont(font)
        self.hiddenCheckBox.setStyleSheet(_fromUtf8("QCheckBox {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(./templates/img/check-box.png);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(./templates/img/blank-check-box.png);\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.hiddenCheckBox.setIconSize(QtCore.QSize(40, 40))
        self.hiddenCheckBox.setChecked(False)
        self.hiddenCheckBox.setObjectName(_fromUtf8("hiddenCheckBox"))
        self.wifiSettingsComboBox.raise_()
        self.ssidlabel.raise_()
        self.passwordlabel.raise_()
        self.wifiSettingsSSIDKeyboardButton.raise_()
        self.wifiSettingsCancelButton.raise_()
        self.wifiSettingsDoneButton.raise_()
        self.hiddenCheckBox.raise_()
        self.stackedWidget.addWidget(self.wifiSettingsPage)
        self.networkInfoPage = QtGui.QWidget()
        self.networkInfoPage.setObjectName(_fromUtf8("networkInfoPage"))
        self.hostnameLabel = QtGui.QLabel(self.networkInfoPage)
        self.hostnameLabel.setGeometry(QtCore.QRect(10, 0, 201, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.hostnameLabel.setFont(font)
        self.hostnameLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.hostnameLabel.setObjectName(_fromUtf8("hostnameLabel"))
        self.hostname = QtGui.QLabel(self.networkInfoPage)
        self.hostname.setGeometry(QtCore.QRect(10, 22, 481, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.hostname.setFont(font)
        self.hostname.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.hostname.setObjectName(_fromUtf8("hostname"))
        self.wifiIpLabel = QtGui.QLabel(self.networkInfoPage)
        self.wifiIpLabel.setGeometry(QtCore.QRect(10, 90, 301, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.wifiIpLabel.setFont(font)
        self.wifiIpLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.wifiIpLabel.setObjectName(_fromUtf8("wifiIpLabel"))
        self.wifiIp = QtGui.QLabel(self.networkInfoPage)
        self.wifiIp.setGeometry(QtCore.QRect(10, 110, 481, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.wifiIp.setFont(font)
        self.wifiIp.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.wifiIp.setObjectName(_fromUtf8("wifiIp"))
        self.lanIpLabel = QtGui.QLabel(self.networkInfoPage)
        self.lanIpLabel.setGeometry(QtCore.QRect(10, 170, 301, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lanIpLabel.setFont(font)
        self.lanIpLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lanIpLabel.setObjectName(_fromUtf8("lanIpLabel"))
        self.lanIp = QtGui.QLabel(self.networkInfoPage)
        self.lanIp.setGeometry(QtCore.QRect(10, 190, 481, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lanIp.setFont(font)
        self.lanIp.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lanIp.setObjectName(_fromUtf8("lanIp"))
        self.networkInfoBackButton = QtGui.QPushButton(self.networkInfoPage)
        self.networkInfoBackButton.setGeometry(QtCore.QRect(0, 250, 481, 71))
        self.networkInfoBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.networkInfoBackButton.setFont(font)
        self.networkInfoBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}"))
        self.networkInfoBackButton.setText(_fromUtf8(""))
        self.networkInfoBackButton.setIcon(icon4)
        self.networkInfoBackButton.setIconSize(QtCore.QSize(50, 50))
        self.networkInfoBackButton.setCheckable(False)
        self.networkInfoBackButton.setAutoDefault(False)
        self.networkInfoBackButton.setDefault(False)
        self.networkInfoBackButton.setFlat(False)
        self.networkInfoBackButton.setObjectName(_fromUtf8("networkInfoBackButton"))
        self.printPreviewSelected_4 = QtGui.QLabel(self.networkInfoPage)
        self.printPreviewSelected_4.setGeometry(QtCore.QRect(280, 30, 210, 210))
        self.printPreviewSelected_4.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.printPreviewSelected_4.setText(_fromUtf8(""))
        self.printPreviewSelected_4.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/thumbnail.png")))
        self.printPreviewSelected_4.setScaledContents(True)
        self.printPreviewSelected_4.setObjectName(_fromUtf8("printPreviewSelected_4"))
        self.hostnameLabel.raise_()
        self.wifiIpLabel.raise_()
        self.wifiIp.raise_()
        self.lanIpLabel.raise_()
        self.lanIp.raise_()
        self.networkInfoBackButton.raise_()
        self.printPreviewSelected_4.raise_()
        self.hostname.raise_()
        self.stackedWidget.addWidget(self.networkInfoPage)
        self.OTAUpdatePage = QtGui.QWidget()
        self.OTAUpdatePage.setObjectName(_fromUtf8("OTAUpdatePage"))
        self.updateListWidget = QtGui.QListWidget(self.OTAUpdatePage)
        self.updateListWidget.setGeometry(QtCore.QRect(0, 0, 481, 251))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.updateListWidget.setFont(font)
        self.updateListWidget.setStyleSheet(_fromUtf8("\n"
"\n"
"QScrollBar:vertical {\n"
" border: 1px solid black; \n"
"border-radius: 5px;\n"
"background: rgb(40,40,40);\n"
"width: 62px;\n"
"}\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/* This remvoes the bottom button by setting the height to 0px */\n"
"QScrollBar::add-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* This remvoes the top button by setting the height to 0px */\n"
"QScrollBar::sub-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/*\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"border: 2px solid grey;\n"
"width: 5px;\n"
"height: 5px;\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QListView::item {\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"outline: none;\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:focus {\n"
"    outline: none;\n"
"}\n"
""))
        self.updateListWidget.setObjectName(_fromUtf8("updateListWidget"))
        self.softwareUpdateBackButton = QtGui.QPushButton(self.OTAUpdatePage)
        self.softwareUpdateBackButton.setGeometry(QtCore.QRect(250, 250, 231, 71))
        self.softwareUpdateBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.softwareUpdateBackButton.setFont(font)
        self.softwareUpdateBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}"))
        self.softwareUpdateBackButton.setText(_fromUtf8(""))
        self.softwareUpdateBackButton.setIcon(icon4)
        self.softwareUpdateBackButton.setIconSize(QtCore.QSize(50, 50))
        self.softwareUpdateBackButton.setCheckable(False)
        self.softwareUpdateBackButton.setAutoDefault(False)
        self.softwareUpdateBackButton.setDefault(False)
        self.softwareUpdateBackButton.setFlat(False)
        self.softwareUpdateBackButton.setObjectName(_fromUtf8("softwareUpdateBackButton"))
        self.performUpdateButton = QtGui.QPushButton(self.OTAUpdatePage)
        self.performUpdateButton.setGeometry(QtCore.QRect(0, 250, 251, 71))
        self.performUpdateButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(17)
        self.performUpdateButton.setFont(font)
        self.performUpdateButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}"))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/update-arrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.performUpdateButton.setIcon(icon9)
        self.performUpdateButton.setIconSize(QtCore.QSize(40, 40))
        self.performUpdateButton.setCheckable(False)
        self.performUpdateButton.setAutoDefault(False)
        self.performUpdateButton.setDefault(False)
        self.performUpdateButton.setFlat(False)
        self.performUpdateButton.setObjectName(_fromUtf8("performUpdateButton"))
        self.stackedWidget.addWidget(self.OTAUpdatePage)
        self.softwareUpdateProgressPage = QtGui.QWidget()
        self.softwareUpdateProgressPage.setObjectName(_fromUtf8("softwareUpdateProgressPage"))
        self.logTextEdit = QtGui.QTextEdit(self.softwareUpdateProgressPage)
        self.logTextEdit.setGeometry(QtCore.QRect(0, 0, 481, 321))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(10)
        self.logTextEdit.setFont(font)
        self.logTextEdit.setStyleSheet(_fromUtf8("QTextEdit{\n"
"background-color:  rgb(40, 40, 40);\n"
"font-color: white;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
" border: 1px solid black; \n"
"border-radius: 5px;\n"
"background: rgb(40,40,40);\n"
"width: 30px;\n"
"}\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/* This remvoes the bottom button by setting the height to 0px */\n"
"QScrollBar::add-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* This remvoes the top button by setting the height to 0px */\n"
"QScrollBar::sub-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/*\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"border: 2px solid grey;\n"
"width: 5px;\n"
"height: 5px;\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
""))
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setObjectName(_fromUtf8("logTextEdit"))
        self.stackedWidget.addWidget(self.softwareUpdateProgressPage)
        self.caliberatePage = QtGui.QWidget()
        self.caliberatePage.setObjectName(_fromUtf8("caliberatePage"))
        self.caliberateLabel = QtGui.QLabel(self.caliberatePage)
        self.caliberateLabel.setGeometry(QtCore.QRect(20, 20, 231, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel.setFont(font)
        self.caliberateLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.caliberateLabel.setObjectName(_fromUtf8("caliberateLabel"))
        self.caliberateBackButton = QtGui.QPushButton(self.caliberatePage)
        self.caliberateBackButton.setGeometry(QtCore.QRect(320, 210, 161, 111))
        self.caliberateBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.caliberateBackButton.setFont(font)
        self.caliberateBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}"))
        self.caliberateBackButton.setText(_fromUtf8(""))
        self.caliberateBackButton.setIcon(icon4)
        self.caliberateBackButton.setIconSize(QtCore.QSize(50, 50))
        self.caliberateBackButton.setCheckable(False)
        self.caliberateBackButton.setAutoDefault(False)
        self.caliberateBackButton.setDefault(False)
        self.caliberateBackButton.setFlat(False)
        self.caliberateBackButton.setObjectName(_fromUtf8("caliberateBackButton"))
        self.nozzleOffsetButton = QtGui.QToolButton(self.caliberatePage)
        self.nozzleOffsetButton.setGeometry(QtCore.QRect(160, 210, 161, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(17)
        self.nozzleOffsetButton.setFont(font)
        self.nozzleOffsetButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QToolButton:focus {\n"
"    outline: none;\n"
"}"))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Nozzle Offset Icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nozzleOffsetButton.setIcon(icon10)
        self.nozzleOffsetButton.setIconSize(QtCore.QSize(70, 70))
        self.nozzleOffsetButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.nozzleOffsetButton.setObjectName(_fromUtf8("nozzleOffsetButton"))
        self.caliberationWizardButton = QtGui.QToolButton(self.caliberatePage)
        self.caliberationWizardButton.setGeometry(QtCore.QRect(0, 210, 161, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.caliberationWizardButton.setFont(font)
        self.caliberationWizardButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QToolButton:focus {\n"
"    outline: none;\n"
"}"))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/magic-wand.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.caliberationWizardButton.setIcon(icon11)
        self.caliberationWizardButton.setIconSize(QtCore.QSize(60, 60))
        self.caliberationWizardButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.caliberationWizardButton.setObjectName(_fromUtf8("caliberationWizardButton"))
        self.stackedWidget.addWidget(self.caliberatePage)
        self.step1Page = QtGui.QWidget()
        self.step1Page.setObjectName(_fromUtf8("step1Page"))
        self.caliberateLabel_6 = QtGui.QLabel(self.step1Page)
        self.caliberateLabel_6.setGeometry(QtCore.QRect(10, 20, 461, 181))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_6.setFont(font)
        self.caliberateLabel_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.caliberateLabel_6.setWordWrap(True)
        self.caliberateLabel_6.setObjectName(_fromUtf8("caliberateLabel_6"))
        self.step1NextButton = QtGui.QPushButton(self.step1Page)
        self.step1NextButton.setGeometry(QtCore.QRect(0, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step1NextButton.setFont(font)
        self.step1NextButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step1NextButton.setIconSize(QtCore.QSize(40, 40))
        self.step1NextButton.setObjectName(_fromUtf8("step1NextButton"))
        self.step1CancelButton = QtGui.QPushButton(self.step1Page)
        self.step1CancelButton.setGeometry(QtCore.QRect(240, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step1CancelButton.setFont(font)
        self.step1CancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step1CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.step1CancelButton.setObjectName(_fromUtf8("step1CancelButton"))
        self.printPreviewSelected_3 = QtGui.QLabel(self.step1Page)
        self.printPreviewSelected_3.setGeometry(QtCore.QRect(160, 110, 150, 150))
        self.printPreviewSelected_3.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.printPreviewSelected_3.setText(_fromUtf8(""))
        self.printPreviewSelected_3.setScaledContents(True)
        self.printPreviewSelected_3.setObjectName(_fromUtf8("printPreviewSelected_3"))
        self.caliberateLabel_16 = QtGui.QLabel(self.step1Page)
        self.caliberateLabel_16.setGeometry(QtCore.QRect(0, 0, 481, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_16.setFont(font)
        self.caliberateLabel_16.setStyleSheet(_fromUtf8("    border: 1px solid rgb(87, 87, 87);\n"
" /*  border-bottom-left-radius: 10px;\n"
" border-bottom-right-radius: 10px;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(180, 180, 180, 255));"))
        self.caliberateLabel_16.setText(_fromUtf8(""))
        self.caliberateLabel_16.setObjectName(_fromUtf8("caliberateLabel_16"))
        self.caliberateLabel_5 = QtGui.QLabel(self.step1Page)
        self.caliberateLabel_5.setGeometry(QtCore.QRect(0, 0, 60, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_5.setFont(font)
        self.caliberateLabel_5.setStyleSheet(_fromUtf8("    background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:0, y2:0.534, stop:0 rgba(130, 203, 117, 255), stop:1 rgba(66, 191, 85, 255));\n"
"border: 1px solid green;"))
        self.caliberateLabel_5.setText(_fromUtf8(""))
        self.caliberateLabel_5.setObjectName(_fromUtf8("caliberateLabel_5"))
        self.caliberateLabel_16.raise_()
        self.caliberateLabel_6.raise_()
        self.step1NextButton.raise_()
        self.step1CancelButton.raise_()
        self.printPreviewSelected_3.raise_()
        self.caliberateLabel_5.raise_()
        self.stackedWidget.addWidget(self.step1Page)
        self.step2Page = QtGui.QWidget()
        self.step2Page.setObjectName(_fromUtf8("step2Page"))
        self.caliberateLabel_7 = QtGui.QLabel(self.step2Page)
        self.caliberateLabel_7.setGeometry(QtCore.QRect(10, 20, 471, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_7.setFont(font)
        self.caliberateLabel_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.caliberateLabel_7.setWordWrap(True)
        self.caliberateLabel_7.setObjectName(_fromUtf8("caliberateLabel_7"))
        self.step2NextButton = QtGui.QPushButton(self.step2Page)
        self.step2NextButton.setGeometry(QtCore.QRect(0, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step2NextButton.setFont(font)
        self.step2NextButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step2NextButton.setIconSize(QtCore.QSize(40, 40))
        self.step2NextButton.setObjectName(_fromUtf8("step2NextButton"))
        self.step2CancelButton = QtGui.QPushButton(self.step2Page)
        self.step2CancelButton.setGeometry(QtCore.QRect(240, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step2CancelButton.setFont(font)
        self.step2CancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step2CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.step2CancelButton.setObjectName(_fromUtf8("step2CancelButton"))
        self.caliberateLabel_21 = QtGui.QLabel(self.step2Page)
        self.caliberateLabel_21.setGeometry(QtCore.QRect(0, 0, 481, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_21.setFont(font)
        self.caliberateLabel_21.setStyleSheet(_fromUtf8("    border: 1px solid rgb(87, 87, 87);\n"
" /*  border-bottom-left-radius: 10px;\n"
" border-bottom-right-radius: 10px;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(180, 180, 180, 255));"))
        self.caliberateLabel_21.setText(_fromUtf8(""))
        self.caliberateLabel_21.setObjectName(_fromUtf8("caliberateLabel_21"))
        self.caliberateLabel_8 = QtGui.QLabel(self.step2Page)
        self.caliberateLabel_8.setGeometry(QtCore.QRect(0, 0, 120, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_8.setFont(font)
        self.caliberateLabel_8.setStyleSheet(_fromUtf8("    background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:0, y2:0.534, stop:0 rgba(130, 203, 117, 255), stop:1 rgba(66, 191, 85, 255));\n"
"border: 1px solid green;"))
        self.caliberateLabel_8.setText(_fromUtf8(""))
        self.caliberateLabel_8.setObjectName(_fromUtf8("caliberateLabel_8"))
        self.caliberateLabel_21.raise_()
        self.caliberateLabel_7.raise_()
        self.step2NextButton.raise_()
        self.step2CancelButton.raise_()
        self.caliberateLabel_8.raise_()
        self.stackedWidget.addWidget(self.step2Page)
        self.step3Page = QtGui.QWidget()
        self.step3Page.setObjectName(_fromUtf8("step3Page"))
        self.step3CancelButton = QtGui.QPushButton(self.step3Page)
        self.step3CancelButton.setGeometry(QtCore.QRect(240, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step3CancelButton.setFont(font)
        self.step3CancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step3CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.step3CancelButton.setObjectName(_fromUtf8("step3CancelButton"))
        self.step3NextButton = QtGui.QPushButton(self.step3Page)
        self.step3NextButton.setGeometry(QtCore.QRect(0, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step3NextButton.setFont(font)
        self.step3NextButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step3NextButton.setIconSize(QtCore.QSize(40, 40))
        self.step3NextButton.setObjectName(_fromUtf8("step3NextButton"))
        self.caliberateLabel_10 = QtGui.QLabel(self.step3Page)
        self.caliberateLabel_10.setGeometry(QtCore.QRect(10, 20, 471, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_10.setFont(font)
        self.caliberateLabel_10.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.caliberateLabel_10.setWordWrap(True)
        self.caliberateLabel_10.setObjectName(_fromUtf8("caliberateLabel_10"))
        self.caliberateLabel_22 = QtGui.QLabel(self.step3Page)
        self.caliberateLabel_22.setGeometry(QtCore.QRect(0, 0, 481, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_22.setFont(font)
        self.caliberateLabel_22.setStyleSheet(_fromUtf8("    border: 1px solid rgb(87, 87, 87);\n"
" /*  border-bottom-left-radius: 10px;\n"
" border-bottom-right-radius: 10px;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(180, 180, 180, 255));"))
        self.caliberateLabel_22.setText(_fromUtf8(""))
        self.caliberateLabel_22.setObjectName(_fromUtf8("caliberateLabel_22"))
        self.caliberateLabel_15 = QtGui.QLabel(self.step3Page)
        self.caliberateLabel_15.setGeometry(QtCore.QRect(0, 0, 180, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_15.setFont(font)
        self.caliberateLabel_15.setStyleSheet(_fromUtf8("    background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:0, y2:0.534, stop:0 rgba(130, 203, 117, 255), stop:1 rgba(66, 191, 85, 255));\n"
"border: 1px solid green;"))
        self.caliberateLabel_15.setText(_fromUtf8(""))
        self.caliberateLabel_15.setObjectName(_fromUtf8("caliberateLabel_15"))
        self.caliberateLabel_22.raise_()
        self.step3CancelButton.raise_()
        self.step3NextButton.raise_()
        self.caliberateLabel_10.raise_()
        self.caliberateLabel_15.raise_()
        self.stackedWidget.addWidget(self.step3Page)
        self.step4Page = QtGui.QWidget()
        self.step4Page.setObjectName(_fromUtf8("step4Page"))
        self.step4CancelButton = QtGui.QPushButton(self.step4Page)
        self.step4CancelButton.setGeometry(QtCore.QRect(240, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step4CancelButton.setFont(font)
        self.step4CancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step4CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.step4CancelButton.setObjectName(_fromUtf8("step4CancelButton"))
        self.step4NextButton = QtGui.QPushButton(self.step4Page)
        self.step4NextButton.setGeometry(QtCore.QRect(0, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step4NextButton.setFont(font)
        self.step4NextButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step4NextButton.setIconSize(QtCore.QSize(40, 40))
        self.step4NextButton.setObjectName(_fromUtf8("step4NextButton"))
        self.caliberateLabel_12 = QtGui.QLabel(self.step4Page)
        self.caliberateLabel_12.setGeometry(QtCore.QRect(10, 20, 471, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_12.setFont(font)
        self.caliberateLabel_12.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.caliberateLabel_12.setWordWrap(True)
        self.caliberateLabel_12.setObjectName(_fromUtf8("caliberateLabel_12"))
        self.caliberateLabel_23 = QtGui.QLabel(self.step4Page)
        self.caliberateLabel_23.setGeometry(QtCore.QRect(0, 0, 481, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_23.setFont(font)
        self.caliberateLabel_23.setStyleSheet(_fromUtf8("    border: 1px solid rgb(87, 87, 87);\n"
" /*  border-bottom-left-radius: 10px;\n"
" border-bottom-right-radius: 10px;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(180, 180, 180, 255));"))
        self.caliberateLabel_23.setText(_fromUtf8(""))
        self.caliberateLabel_23.setObjectName(_fromUtf8("caliberateLabel_23"))
        self.caliberateLabel_11 = QtGui.QLabel(self.step4Page)
        self.caliberateLabel_11.setGeometry(QtCore.QRect(0, 0, 240, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_11.setFont(font)
        self.caliberateLabel_11.setStyleSheet(_fromUtf8("    background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:0, y2:0.534, stop:0 rgba(130, 203, 117, 255), stop:1 rgba(66, 191, 85, 255));\n"
"border: 1px solid green;"))
        self.caliberateLabel_11.setText(_fromUtf8(""))
        self.caliberateLabel_11.setObjectName(_fromUtf8("caliberateLabel_11"))
        self.caliberateLabel_23.raise_()
        self.step4CancelButton.raise_()
        self.step4NextButton.raise_()
        self.caliberateLabel_12.raise_()
        self.caliberateLabel_11.raise_()
        self.stackedWidget.addWidget(self.step4Page)
        self.step5Page = QtGui.QWidget()
        self.step5Page.setObjectName(_fromUtf8("step5Page"))
        self.caliberateLabel_25 = QtGui.QLabel(self.step5Page)
        self.caliberateLabel_25.setGeometry(QtCore.QRect(0, 20, 481, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_25.setFont(font)
        self.caliberateLabel_25.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.caliberateLabel_25.setWordWrap(True)
        self.caliberateLabel_25.setObjectName(_fromUtf8("caliberateLabel_25"))
        self.caliberateLabel_92 = QtGui.QLabel(self.step5Page)
        self.caliberateLabel_92.setGeometry(QtCore.QRect(0, 0, 300, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_92.setFont(font)
        self.caliberateLabel_92.setStyleSheet(_fromUtf8("    background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:0, y2:0.534, stop:0 rgba(130, 203, 117, 255), stop:1 rgba(66, 191, 85, 255));\n"
"border: 1px solid green;"))
        self.caliberateLabel_92.setText(_fromUtf8(""))
        self.caliberateLabel_92.setObjectName(_fromUtf8("caliberateLabel_92"))
        self.caliberateLabel_93 = QtGui.QLabel(self.step5Page)
        self.caliberateLabel_93.setGeometry(QtCore.QRect(0, 0, 481, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_93.setFont(font)
        self.caliberateLabel_93.setStyleSheet(_fromUtf8("    border: 1px solid rgb(87, 87, 87);\n"
" /*  border-bottom-left-radius: 10px;\n"
" border-bottom-right-radius: 10px;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(180, 180, 180, 255));"))
        self.caliberateLabel_93.setText(_fromUtf8(""))
        self.caliberateLabel_93.setObjectName(_fromUtf8("caliberateLabel_93"))
        self.step5NextButton = QtGui.QPushButton(self.step5Page)
        self.step5NextButton.setGeometry(QtCore.QRect(0, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step5NextButton.setFont(font)
        self.step5NextButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step5NextButton.setIconSize(QtCore.QSize(40, 40))
        self.step5NextButton.setObjectName(_fromUtf8("step5NextButton"))
        self.step5CancelButton = QtGui.QPushButton(self.step5Page)
        self.step5CancelButton.setGeometry(QtCore.QRect(240, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step5CancelButton.setFont(font)
        self.step5CancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step5CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.step5CancelButton.setObjectName(_fromUtf8("step5CancelButton"))
        self.caliberateLabel_93.raise_()
        self.caliberateLabel_25.raise_()
        self.caliberateLabel_92.raise_()
        self.step5NextButton.raise_()
        self.step5CancelButton.raise_()
        self.stackedWidget.addWidget(self.step5Page)
        self.step6Page = QtGui.QWidget()
        self.step6Page.setObjectName(_fromUtf8("step6Page"))
        self.caliberateLabel_17 = QtGui.QLabel(self.step6Page)
        self.caliberateLabel_17.setGeometry(QtCore.QRect(0, 0, 360, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_17.setFont(font)
        self.caliberateLabel_17.setStyleSheet(_fromUtf8("    background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:0, y2:0.534, stop:0 rgba(130, 203, 117, 255), stop:1 rgba(66, 191, 85, 255));\n"
"border: 1px solid green;"))
        self.caliberateLabel_17.setText(_fromUtf8(""))
        self.caliberateLabel_17.setObjectName(_fromUtf8("caliberateLabel_17"))
        self.step6NextButton = QtGui.QPushButton(self.step6Page)
        self.step6NextButton.setGeometry(QtCore.QRect(0, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step6NextButton.setFont(font)
        self.step6NextButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step6NextButton.setIconSize(QtCore.QSize(40, 40))
        self.step6NextButton.setObjectName(_fromUtf8("step6NextButton"))
        self.caliberateNozzleHeightLabel_2 = QtGui.QLabel(self.step6Page)
        self.caliberateNozzleHeightLabel_2.setGeometry(QtCore.QRect(0, 20, 471, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateNozzleHeightLabel_2.setFont(font)
        self.caliberateNozzleHeightLabel_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.caliberateNozzleHeightLabel_2.setWordWrap(True)
        self.caliberateNozzleHeightLabel_2.setObjectName(_fromUtf8("caliberateNozzleHeightLabel_2"))
        self.step6CancelButton = QtGui.QPushButton(self.step6Page)
        self.step6CancelButton.setGeometry(QtCore.QRect(240, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step6CancelButton.setFont(font)
        self.step6CancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step6CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.step6CancelButton.setObjectName(_fromUtf8("step6CancelButton"))
        self.caliberateLabel_42 = QtGui.QLabel(self.step6Page)
        self.caliberateLabel_42.setGeometry(QtCore.QRect(0, 0, 481, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_42.setFont(font)
        self.caliberateLabel_42.setStyleSheet(_fromUtf8("    border: 1px solid rgb(87, 87, 87);\n"
" /*  border-bottom-left-radius: 10px;\n"
" border-bottom-right-radius: 10px;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(180, 180, 180, 255));"))
        self.caliberateLabel_42.setText(_fromUtf8(""))
        self.caliberateLabel_42.setObjectName(_fromUtf8("caliberateLabel_42"))
        self.caliberateLabel_42.raise_()
        self.caliberateLabel_17.raise_()
        self.step6NextButton.raise_()
        self.caliberateNozzleHeightLabel_2.raise_()
        self.step6CancelButton.raise_()
        self.stackedWidget.addWidget(self.step6Page)
        self.step7Page = QtGui.QWidget()
        self.step7Page.setObjectName(_fromUtf8("step7Page"))
        self.step7NextButton = QtGui.QPushButton(self.step7Page)
        self.step7NextButton.setGeometry(QtCore.QRect(0, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step7NextButton.setFont(font)
        self.step7NextButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step7NextButton.setIconSize(QtCore.QSize(40, 40))
        self.step7NextButton.setObjectName(_fromUtf8("step7NextButton"))
        self.caliberateLabel_87 = QtGui.QLabel(self.step7Page)
        self.caliberateLabel_87.setGeometry(QtCore.QRect(0, 0, 420, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_87.setFont(font)
        self.caliberateLabel_87.setStyleSheet(_fromUtf8("    background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:0, y2:0.534, stop:0 rgba(130, 203, 117, 255), stop:1 rgba(66, 191, 85, 255));\n"
"border: 1px solid green;"))
        self.caliberateLabel_87.setText(_fromUtf8(""))
        self.caliberateLabel_87.setObjectName(_fromUtf8("caliberateLabel_87"))
        self.caliberateLabel_88 = QtGui.QLabel(self.step7Page)
        self.caliberateLabel_88.setGeometry(QtCore.QRect(0, 0, 481, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_88.setFont(font)
        self.caliberateLabel_88.setStyleSheet(_fromUtf8("    border: 1px solid rgb(87, 87, 87);\n"
" /*  border-bottom-left-radius: 10px;\n"
" border-bottom-right-radius: 10px;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(180, 180, 180, 255));"))
        self.caliberateLabel_88.setText(_fromUtf8(""))
        self.caliberateLabel_88.setObjectName(_fromUtf8("caliberateLabel_88"))
        self.caliberateLabel_89 = QtGui.QLabel(self.step7Page)
        self.caliberateLabel_89.setGeometry(QtCore.QRect(0, 20, 471, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_89.setFont(font)
        self.caliberateLabel_89.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.caliberateLabel_89.setWordWrap(True)
        self.caliberateLabel_89.setObjectName(_fromUtf8("caliberateLabel_89"))
        self.step7CancelButton = QtGui.QPushButton(self.step7Page)
        self.step7CancelButton.setGeometry(QtCore.QRect(240, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step7CancelButton.setFont(font)
        self.step7CancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step7CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.step7CancelButton.setObjectName(_fromUtf8("step7CancelButton"))
        self.caliberateLabel_88.raise_()
        self.step7NextButton.raise_()
        self.caliberateLabel_87.raise_()
        self.caliberateLabel_89.raise_()
        self.step7CancelButton.raise_()
        self.stackedWidget.addWidget(self.step7Page)
        self.step8Page = QtGui.QWidget()
        self.step8Page.setObjectName(_fromUtf8("step8Page"))
        self.step8CancelButton = QtGui.QPushButton(self.step8Page)
        self.step8CancelButton.setGeometry(QtCore.QRect(240, 261, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step8CancelButton.setFont(font)
        self.step8CancelButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step8CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.step8CancelButton.setObjectName(_fromUtf8("step8CancelButton"))
        self.step8DoneButton = QtGui.QPushButton(self.step8Page)
        self.step8DoneButton.setGeometry(QtCore.QRect(0, 261, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.step8DoneButton.setFont(font)
        self.step8DoneButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.step8DoneButton.setIconSize(QtCore.QSize(40, 40))
        self.step8DoneButton.setObjectName(_fromUtf8("step8DoneButton"))
        self.caliberateLabel_90 = QtGui.QLabel(self.step8Page)
        self.caliberateLabel_90.setGeometry(QtCore.QRect(0, 21, 471, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_90.setFont(font)
        self.caliberateLabel_90.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.caliberateLabel_90.setWordWrap(True)
        self.caliberateLabel_90.setObjectName(_fromUtf8("caliberateLabel_90"))
        self.moveZPCaliberateButton = QtGui.QPushButton(self.step8Page)
        self.moveZPCaliberateButton.setGeometry(QtCore.QRect(160, 161, 161, 91))
        self.moveZPCaliberateButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveZPCaliberateButton.setFont(font)
        self.moveZPCaliberateButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.moveZPCaliberateButton.setText(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/arrows-5.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moveZPCaliberateButton.setIcon(icon12)
        self.moveZPCaliberateButton.setIconSize(QtCore.QSize(40, 40))
        self.moveZPCaliberateButton.setCheckable(False)
        self.moveZPCaliberateButton.setAutoDefault(False)
        self.moveZPCaliberateButton.setDefault(False)
        self.moveZPCaliberateButton.setFlat(False)
        self.moveZPCaliberateButton.setObjectName(_fromUtf8("moveZPCaliberateButton"))
        self.caliberateLabel_91 = QtGui.QLabel(self.step8Page)
        self.caliberateLabel_91.setGeometry(QtCore.QRect(0, 1, 481, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.caliberateLabel_91.setFont(font)
        self.caliberateLabel_91.setStyleSheet(_fromUtf8("    background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:0, y2:0.534, stop:0 rgba(130, 203, 117, 255), stop:1 rgba(66, 191, 85, 255));\n"
"border: 1px solid green;"))
        self.caliberateLabel_91.setText(_fromUtf8(""))
        self.caliberateLabel_91.setObjectName(_fromUtf8("caliberateLabel_91"))
        self.moveZMCaliberateButton = QtGui.QPushButton(self.step8Page)
        self.moveZMCaliberateButton.setGeometry(QtCore.QRect(160, 70, 161, 91))
        self.moveZMCaliberateButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveZMCaliberateButton.setFont(font)
        self.moveZMCaliberateButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.moveZMCaliberateButton.setText(_fromUtf8(""))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/arrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moveZMCaliberateButton.setIcon(icon13)
        self.moveZMCaliberateButton.setIconSize(QtCore.QSize(40, 40))
        self.moveZMCaliberateButton.setCheckable(False)
        self.moveZMCaliberateButton.setAutoDefault(False)
        self.moveZMCaliberateButton.setDefault(False)
        self.moveZMCaliberateButton.setFlat(False)
        self.moveZMCaliberateButton.setObjectName(_fromUtf8("moveZMCaliberateButton"))
        self.stackedWidget.addWidget(self.step8Page)
        self.nozzleOffsetPage = QtGui.QWidget()
        self.nozzleOffsetPage.setObjectName(_fromUtf8("nozzleOffsetPage"))
        self.nozzleOffsetDoubleSpinBox = QtGui.QDoubleSpinBox(self.nozzleOffsetPage)
        self.nozzleOffsetDoubleSpinBox.setGeometry(QtCore.QRect(60, 90, 321, 136))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.nozzleOffsetDoubleSpinBox.setFont(font)
        self.nozzleOffsetDoubleSpinBox.setStyleSheet(_fromUtf8("QDoubleSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QDoubleSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow { \n"
"image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow { \n"
"image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
""))
        self.nozzleOffsetDoubleSpinBox.setReadOnly(False)
        self.nozzleOffsetDoubleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.nozzleOffsetDoubleSpinBox.setAccelerated(True)
        self.nozzleOffsetDoubleSpinBox.setDecimals(2)
        self.nozzleOffsetDoubleSpinBox.setMinimum(-2.0)
        self.nozzleOffsetDoubleSpinBox.setMaximum(2.0)
        self.nozzleOffsetDoubleSpinBox.setSingleStep(0.05)
        self.nozzleOffsetDoubleSpinBox.setObjectName(_fromUtf8("nozzleOffsetDoubleSpinBox"))
        self.nozzleOffsetSetButton = QtGui.QPushButton(self.nozzleOffsetPage)
        self.nozzleOffsetSetButton.setGeometry(QtCore.QRect(378, 92, 91, 132))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.nozzleOffsetSetButton.setFont(font)
        self.nozzleOffsetSetButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.nozzleOffsetSetButton.setText(_fromUtf8(""))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/verification-mark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nozzleOffsetSetButton.setIcon(icon14)
        self.nozzleOffsetSetButton.setIconSize(QtCore.QSize(50, 50))
        self.nozzleOffsetSetButton.setObjectName(_fromUtf8("nozzleOffsetSetButton"))
        self.feedRateLabelControlPage_3 = QtGui.QLabel(self.nozzleOffsetPage)
        self.feedRateLabelControlPage_3.setGeometry(QtCore.QRect(10, 0, 481, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.feedRateLabelControlPage_3.setFont(font)
        self.feedRateLabelControlPage_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.feedRateLabelControlPage_3.setWordWrap(True)
        self.feedRateLabelControlPage_3.setObjectName(_fromUtf8("feedRateLabelControlPage_3"))
        self.nozzleOffsetBackButton = QtGui.QPushButton(self.nozzleOffsetPage)
        self.nozzleOffsetBackButton.setGeometry(QtCore.QRect(0, 260, 480, 60))
        self.nozzleOffsetBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.nozzleOffsetBackButton.setFont(font)
        self.nozzleOffsetBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.nozzleOffsetBackButton.setText(_fromUtf8(""))
        self.nozzleOffsetBackButton.setIcon(icon4)
        self.nozzleOffsetBackButton.setIconSize(QtCore.QSize(50, 50))
        self.nozzleOffsetBackButton.setCheckable(False)
        self.nozzleOffsetBackButton.setAutoDefault(False)
        self.nozzleOffsetBackButton.setDefault(False)
        self.nozzleOffsetBackButton.setFlat(False)
        self.nozzleOffsetBackButton.setObjectName(_fromUtf8("nozzleOffsetBackButton"))
        self.printPreviewSelected_2 = QtGui.QLabel(self.nozzleOffsetPage)
        self.printPreviewSelected_2.setGeometry(QtCore.QRect(150, 90, 161, 161))
        self.printPreviewSelected_2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.printPreviewSelected_2.setText(_fromUtf8(""))
        self.printPreviewSelected_2.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Nozzle Offset.png")))
        self.printPreviewSelected_2.setScaledContents(True)
        self.printPreviewSelected_2.setObjectName(_fromUtf8("printPreviewSelected_2"))
        self.feedRateLabelControlPage_3.raise_()
        self.nozzleOffsetDoubleSpinBox.raise_()
        self.nozzleOffsetSetButton.raise_()
        self.nozzleOffsetBackButton.raise_()
        self.printPreviewSelected_2.raise_()
        self.stackedWidget.addWidget(self.nozzleOffsetPage)
        self.printLocationPage = QtGui.QWidget()
        self.printLocationPage.setObjectName(_fromUtf8("printLocationPage"))
        self.fromUsbButton = QtGui.QPushButton(self.printLocationPage)
        self.fromUsbButton.setGeometry(QtCore.QRect(160, 210, 161, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.fromUsbButton.setFont(font)
        self.fromUsbButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}"))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/usb.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fromUsbButton.setIcon(icon15)
        self.fromUsbButton.setIconSize(QtCore.QSize(40, 40))
        self.fromUsbButton.setObjectName(_fromUtf8("fromUsbButton"))
        self.printFromLabel = QtGui.QLabel(self.printLocationPage)
        self.printFromLabel.setGeometry(QtCore.QRect(10, 80, 231, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.printFromLabel.setFont(font)
        self.printFromLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.printFromLabel.setObjectName(_fromUtf8("printFromLabel"))
        self.printLocationScreenBackButton = QtGui.QPushButton(self.printLocationPage)
        self.printLocationScreenBackButton.setGeometry(QtCore.QRect(320, 210, 161, 111))
        self.printLocationScreenBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.printLocationScreenBackButton.setFont(font)
        self.printLocationScreenBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}"))
        self.printLocationScreenBackButton.setText(_fromUtf8(""))
        self.printLocationScreenBackButton.setIcon(icon4)
        self.printLocationScreenBackButton.setIconSize(QtCore.QSize(50, 50))
        self.printLocationScreenBackButton.setCheckable(False)
        self.printLocationScreenBackButton.setAutoDefault(False)
        self.printLocationScreenBackButton.setDefault(False)
        self.printLocationScreenBackButton.setFlat(False)
        self.printLocationScreenBackButton.setObjectName(_fromUtf8("printLocationScreenBackButton"))
        self.fromLocalButton = QtGui.QPushButton(self.printLocationPage)
        self.fromLocalButton.setGeometry(QtCore.QRect(0, 210, 161, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.fromLocalButton.setFont(font)
        self.fromLocalButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}"))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fromLocalButton.setIcon(icon16)
        self.fromLocalButton.setIconSize(QtCore.QSize(40, 40))
        self.fromLocalButton.setObjectName(_fromUtf8("fromLocalButton"))
        self.stackedWidget.addWidget(self.printLocationPage)
        self.fileListLocalPage = QtGui.QWidget()
        self.fileListLocalPage.setObjectName(_fromUtf8("fileListLocalPage"))
        self.fileListWidget = QtGui.QListWidget(self.fileListLocalPage)
        self.fileListWidget.setGeometry(QtCore.QRect(0, 0, 321, 321))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(17)
        self.fileListWidget.setFont(font)
        self.fileListWidget.setStyleSheet(_fromUtf8("\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width\n"
" of the view */\n"
"    background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:!selected {\n"
"    color: black;\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border:  rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"     border: 1px solid rgb(182, 182, 182);\n"
"    background-color: rgb(40,40,40);\n"
"outline: none;\n"
"\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"     border: 1px solid  rgb(182, 182, 182);\n"
"    background-color: rgb(40,40,40);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected:focus {\n"
"    outline: none;\n"
"}\n"
""))
        self.fileListWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.fileListWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.fileListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fileListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fileListWidget.setAutoScrollMargin(4)
        self.fileListWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.fileListWidget.setObjectName(_fromUtf8("fileListWidget"))
        self.localStorageBackButton = QtGui.QPushButton(self.fileListLocalPage)
        self.localStorageBackButton.setGeometry(QtCore.QRect(390, 210, 91, 111))
        self.localStorageBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.localStorageBackButton.setFont(font)
        self.localStorageBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"        border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.localStorageBackButton.setText(_fromUtf8(""))
        self.localStorageBackButton.setIcon(icon4)
        self.localStorageBackButton.setIconSize(QtCore.QSize(50, 50))
        self.localStorageBackButton.setCheckable(False)
        self.localStorageBackButton.setAutoDefault(False)
        self.localStorageBackButton.setDefault(False)
        self.localStorageBackButton.setFlat(False)
        self.localStorageBackButton.setObjectName(_fromUtf8("localStorageBackButton"))
        self.localStorageSelectButton = QtGui.QPushButton(self.fileListLocalPage)
        self.localStorageSelectButton.setGeometry(QtCore.QRect(390, 0, 91, 111))
        self.localStorageSelectButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.localStorageSelectButton.setFont(font)
        self.localStorageSelectButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.localStorageSelectButton.setText(_fromUtf8(""))
        self.localStorageSelectButton.setIcon(icon14)
        self.localStorageSelectButton.setIconSize(QtCore.QSize(50, 50))
        self.localStorageSelectButton.setCheckable(False)
        self.localStorageSelectButton.setAutoDefault(False)
        self.localStorageSelectButton.setDefault(False)
        self.localStorageSelectButton.setFlat(False)
        self.localStorageSelectButton.setObjectName(_fromUtf8("localStorageSelectButton"))
        self.localStorageScrollDown = QtGui.QPushButton(self.fileListLocalPage)
        self.localStorageScrollDown.setGeometry(QtCore.QRect(310, 160, 81, 161))
        self.localStorageScrollDown.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.localStorageScrollDown.setFont(font)
        self.localStorageScrollDown.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.localStorageScrollDown.setText(_fromUtf8(""))
        self.localStorageScrollDown.setIcon(icon12)
        self.localStorageScrollDown.setIconSize(QtCore.QSize(40, 40))
        self.localStorageScrollDown.setCheckable(False)
        self.localStorageScrollDown.setAutoRepeat(True)
        self.localStorageScrollDown.setAutoExclusive(False)
        self.localStorageScrollDown.setAutoDefault(False)
        self.localStorageScrollDown.setDefault(False)
        self.localStorageScrollDown.setFlat(False)
        self.localStorageScrollDown.setObjectName(_fromUtf8("localStorageScrollDown"))
        self.localStorageScrollUp = QtGui.QPushButton(self.fileListLocalPage)
        self.localStorageScrollUp.setGeometry(QtCore.QRect(310, 0, 81, 161))
        self.localStorageScrollUp.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.localStorageScrollUp.setFont(font)
        self.localStorageScrollUp.setStyleSheet(_fromUtf8("QPushButton {\n"
"\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.localStorageScrollUp.setText(_fromUtf8(""))
        self.localStorageScrollUp.setIcon(icon13)
        self.localStorageScrollUp.setIconSize(QtCore.QSize(40, 40))
        self.localStorageScrollUp.setCheckable(False)
        self.localStorageScrollUp.setAutoRepeat(True)
        self.localStorageScrollUp.setAutoExclusive(False)
        self.localStorageScrollUp.setAutoDefault(False)
        self.localStorageScrollUp.setDefault(False)
        self.localStorageScrollUp.setFlat(False)
        self.localStorageScrollUp.setObjectName(_fromUtf8("localStorageScrollUp"))
        self.localStorageDeleteButton = QtGui.QPushButton(self.fileListLocalPage)
        self.localStorageDeleteButton.setGeometry(QtCore.QRect(390, 110, 91, 101))
        self.localStorageDeleteButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.localStorageDeleteButton.setFont(font)
        self.localStorageDeleteButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.localStorageDeleteButton.setText(_fromUtf8(""))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.localStorageDeleteButton.setIcon(icon17)
        self.localStorageDeleteButton.setIconSize(QtCore.QSize(50, 50))
        self.localStorageDeleteButton.setCheckable(False)
        self.localStorageDeleteButton.setAutoDefault(False)
        self.localStorageDeleteButton.setDefault(False)
        self.localStorageDeleteButton.setFlat(False)
        self.localStorageDeleteButton.setObjectName(_fromUtf8("localStorageDeleteButton"))
        self.stackedWidget.addWidget(self.fileListLocalPage)
        self.fileListUSBPage = QtGui.QWidget()
        self.fileListUSBPage.setObjectName(_fromUtf8("fileListUSBPage"))
        self.USBStorageSaveButton = QtGui.QPushButton(self.fileListUSBPage)
        self.USBStorageSaveButton.setGeometry(QtCore.QRect(390, 110, 91, 101))
        self.USBStorageSaveButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.USBStorageSaveButton.setFont(font)
        self.USBStorageSaveButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.USBStorageSaveButton.setText(_fromUtf8(""))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.USBStorageSaveButton.setIcon(icon18)
        self.USBStorageSaveButton.setIconSize(QtCore.QSize(50, 50))
        self.USBStorageSaveButton.setCheckable(False)
        self.USBStorageSaveButton.setAutoDefault(False)
        self.USBStorageSaveButton.setDefault(False)
        self.USBStorageSaveButton.setFlat(False)
        self.USBStorageSaveButton.setObjectName(_fromUtf8("USBStorageSaveButton"))
        self.USBStorageScrollUp = QtGui.QPushButton(self.fileListUSBPage)
        self.USBStorageScrollUp.setGeometry(QtCore.QRect(310, 0, 81, 161))
        self.USBStorageScrollUp.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.USBStorageScrollUp.setFont(font)
        self.USBStorageScrollUp.setStyleSheet(_fromUtf8("QPushButton {\n"
"\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.USBStorageScrollUp.setText(_fromUtf8(""))
        self.USBStorageScrollUp.setIcon(icon13)
        self.USBStorageScrollUp.setIconSize(QtCore.QSize(40, 40))
        self.USBStorageScrollUp.setCheckable(False)
        self.USBStorageScrollUp.setAutoRepeat(True)
        self.USBStorageScrollUp.setAutoExclusive(False)
        self.USBStorageScrollUp.setAutoDefault(False)
        self.USBStorageScrollUp.setDefault(False)
        self.USBStorageScrollUp.setFlat(False)
        self.USBStorageScrollUp.setObjectName(_fromUtf8("USBStorageScrollUp"))
        self.USBStorageSelectButton = QtGui.QPushButton(self.fileListUSBPage)
        self.USBStorageSelectButton.setGeometry(QtCore.QRect(390, 0, 91, 111))
        self.USBStorageSelectButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.USBStorageSelectButton.setFont(font)
        self.USBStorageSelectButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.USBStorageSelectButton.setText(_fromUtf8(""))
        self.USBStorageSelectButton.setIcon(icon14)
        self.USBStorageSelectButton.setIconSize(QtCore.QSize(50, 50))
        self.USBStorageSelectButton.setCheckable(False)
        self.USBStorageSelectButton.setAutoDefault(False)
        self.USBStorageSelectButton.setDefault(False)
        self.USBStorageSelectButton.setFlat(False)
        self.USBStorageSelectButton.setObjectName(_fromUtf8("USBStorageSelectButton"))
        self.USBStorageBackButton = QtGui.QPushButton(self.fileListUSBPage)
        self.USBStorageBackButton.setGeometry(QtCore.QRect(390, 210, 91, 111))
        self.USBStorageBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.USBStorageBackButton.setFont(font)
        self.USBStorageBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"        border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.USBStorageBackButton.setText(_fromUtf8(""))
        self.USBStorageBackButton.setIcon(icon4)
        self.USBStorageBackButton.setIconSize(QtCore.QSize(50, 50))
        self.USBStorageBackButton.setCheckable(False)
        self.USBStorageBackButton.setAutoDefault(False)
        self.USBStorageBackButton.setDefault(False)
        self.USBStorageBackButton.setFlat(False)
        self.USBStorageBackButton.setObjectName(_fromUtf8("USBStorageBackButton"))
        self.USBStorageScrollDown = QtGui.QPushButton(self.fileListUSBPage)
        self.USBStorageScrollDown.setGeometry(QtCore.QRect(310, 160, 81, 161))
        self.USBStorageScrollDown.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.USBStorageScrollDown.setFont(font)
        self.USBStorageScrollDown.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.USBStorageScrollDown.setText(_fromUtf8(""))
        self.USBStorageScrollDown.setIcon(icon12)
        self.USBStorageScrollDown.setIconSize(QtCore.QSize(40, 40))
        self.USBStorageScrollDown.setCheckable(False)
        self.USBStorageScrollDown.setAutoRepeat(True)
        self.USBStorageScrollDown.setAutoExclusive(False)
        self.USBStorageScrollDown.setAutoDefault(False)
        self.USBStorageScrollDown.setDefault(False)
        self.USBStorageScrollDown.setFlat(False)
        self.USBStorageScrollDown.setObjectName(_fromUtf8("USBStorageScrollDown"))
        self.fileListWidgetUSB = QtGui.QListWidget(self.fileListUSBPage)
        self.fileListWidgetUSB.setGeometry(QtCore.QRect(0, 0, 311, 321))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(17)
        self.fileListWidgetUSB.setFont(font)
        self.fileListWidgetUSB.setStyleSheet(_fromUtf8("\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width\n"
" of the view */\n"
"    background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:!selected {\n"
"    color: black;\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border:  rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"     border: 1px solid rgb(182, 182, 182);\n"
"    background-color: rgb(40,40,40);\n"
"outline: none;\n"
"\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"     border: 1px solid  rgb(182, 182, 182);\n"
"    background-color: rgb(40,40,40);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected:focus {\n"
"    outline: none;\n"
"}\n"
""))
        self.fileListWidgetUSB.setFrameShape(QtGui.QFrame.NoFrame)
        self.fileListWidgetUSB.setFrameShadow(QtGui.QFrame.Plain)
        self.fileListWidgetUSB.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fileListWidgetUSB.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fileListWidgetUSB.setAutoScrollMargin(4)
        self.fileListWidgetUSB.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.fileListWidgetUSB.setObjectName(_fromUtf8("fileListWidgetUSB"))
        self.USBStorageSaveButton.raise_()
        self.USBStorageSelectButton.raise_()
        self.USBStorageBackButton.raise_()
        self.fileListWidgetUSB.raise_()
        self.USBStorageScrollDown.raise_()
        self.USBStorageScrollUp.raise_()
        self.stackedWidget.addWidget(self.fileListUSBPage)
        self.printSelectedLocalPage = QtGui.QWidget()
        self.printSelectedLocalPage.setObjectName(_fromUtf8("printSelectedLocalPage"))
        self.fileSelected = QtGui.QLabel(self.printSelectedLocalPage)
        self.fileSelected.setGeometry(QtCore.QRect(10, 0, 461, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.fileSelected.setFont(font)
        self.fileSelected.setStyleSheet(_fromUtf8("color:  white;\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.fileSelected.setScaledContents(True)
        self.fileSelected.setWordWrap(True)
        self.fileSelected.setObjectName(_fromUtf8("fileSelected"))
        self.fileSelectedBackButton = QtGui.QPushButton(self.printSelectedLocalPage)
        self.fileSelectedBackButton.setGeometry(QtCore.QRect(240, 230, 241, 91))
        self.fileSelectedBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.fileSelectedBackButton.setFont(font)
        self.fileSelectedBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}"))
        self.fileSelectedBackButton.setText(_fromUtf8(""))
        self.fileSelectedBackButton.setIcon(icon4)
        self.fileSelectedBackButton.setIconSize(QtCore.QSize(50, 50))
        self.fileSelectedBackButton.setCheckable(False)
        self.fileSelectedBackButton.setAutoDefault(False)
        self.fileSelectedBackButton.setDefault(False)
        self.fileSelectedBackButton.setFlat(False)
        self.fileSelectedBackButton.setObjectName(_fromUtf8("fileSelectedBackButton"))
        self.fileSelectedPrintButton = QtGui.QToolButton(self.printSelectedLocalPage)
        self.fileSelectedPrintButton.setGeometry(QtCore.QRect(0, 230, 241, 91))
        self.fileSelectedPrintButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        self.fileSelectedPrintButton.setFont(font)
        self.fileSelectedPrintButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.fileSelectedPrintButton.setIcon(icon5)
        self.fileSelectedPrintButton.setIconSize(QtCore.QSize(40, 40))
        self.fileSelectedPrintButton.setCheckable(False)
        self.fileSelectedPrintButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.fileSelectedPrintButton.setObjectName(_fromUtf8("fileSelectedPrintButton"))
        self.fileSizeSelected = QtGui.QLabel(self.printSelectedLocalPage)
        self.fileSizeSelected.setGeometry(QtCore.QRect(60, 60, 161, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.fileSizeSelected.setFont(font)
        self.fileSizeSelected.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.fileSizeSelected.setScaledContents(True)
        self.fileSizeSelected.setObjectName(_fromUtf8("fileSizeSelected"))
        self.fileDateSelected = QtGui.QLabel(self.printSelectedLocalPage)
        self.fileDateSelected.setGeometry(QtCore.QRect(70, 90, 201, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.fileDateSelected.setFont(font)
        self.fileDateSelected.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.fileDateSelected.setScaledContents(True)
        self.fileDateSelected.setObjectName(_fromUtf8("fileDateSelected"))
        self.filePrintTimeSelected = QtGui.QLabel(self.printSelectedLocalPage)
        self.filePrintTimeSelected.setGeometry(QtCore.QRect(130, 137, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.filePrintTimeSelected.setFont(font)
        self.filePrintTimeSelected.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.filePrintTimeSelected.setScaledContents(True)
        self.filePrintTimeSelected.setObjectName(_fromUtf8("filePrintTimeSelected"))
        self.filamentVolumeSelected = QtGui.QLabel(self.printSelectedLocalPage)
        self.filamentVolumeSelected.setGeometry(QtCore.QRect(110, 160, 161, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.filamentVolumeSelected.setFont(font)
        self.filamentVolumeSelected.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.filamentVolumeSelected.setScaledContents(True)
        self.filamentVolumeSelected.setObjectName(_fromUtf8("filamentVolumeSelected"))
        self.fileSizeSelectedLabel = QtGui.QLabel(self.printSelectedLocalPage)
        self.fileSizeSelectedLabel.setGeometry(QtCore.QRect(10, 60, 51, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fileSizeSelectedLabel.setFont(font)
        self.fileSizeSelectedLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.fileSizeSelectedLabel.setObjectName(_fromUtf8("fileSizeSelectedLabel"))
        self.fileDateSelectedLabel = QtGui.QLabel(self.printSelectedLocalPage)
        self.fileDateSelectedLabel.setGeometry(QtCore.QRect(10, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fileDateSelectedLabel.setFont(font)
        self.fileDateSelectedLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.fileDateSelectedLabel.setObjectName(_fromUtf8("fileDateSelectedLabel"))
        self.filePrintTimeSelectedLabel = QtGui.QLabel(self.printSelectedLocalPage)
        self.filePrintTimeSelectedLabel.setGeometry(QtCore.QRect(10, 110, 121, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.filePrintTimeSelectedLabel.setFont(font)
        self.filePrintTimeSelectedLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.filePrintTimeSelectedLabel.setWordWrap(True)
        self.filePrintTimeSelectedLabel.setObjectName(_fromUtf8("filePrintTimeSelectedLabel"))
        self.filamentVolumeSelectedLabel = QtGui.QLabel(self.printSelectedLocalPage)
        self.filamentVolumeSelectedLabel.setGeometry(QtCore.QRect(10, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.filamentVolumeSelectedLabel.setFont(font)
        self.filamentVolumeSelectedLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.filamentVolumeSelectedLabel.setObjectName(_fromUtf8("filamentVolumeSelectedLabel"))
        self.filamentLengthFileSelected = QtGui.QLabel(self.printSelectedLocalPage)
        self.filamentLengthFileSelected.setGeometry(QtCore.QRect(110, 190, 161, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Medium"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.filamentLengthFileSelected.setFont(font)
        self.filamentLengthFileSelected.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.filamentLengthFileSelected.setScaledContents(True)
        self.filamentLengthFileSelected.setObjectName(_fromUtf8("filamentLengthFileSelected"))
        self.filamentLengthSelectedLabel = QtGui.QLabel(self.printSelectedLocalPage)
        self.filamentLengthSelectedLabel.setGeometry(QtCore.QRect(10, 190, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.filamentLengthSelectedLabel.setFont(font)
        self.filamentLengthSelectedLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.filamentLengthSelectedLabel.setObjectName(_fromUtf8("filamentLengthSelectedLabel"))
        self.printPreviewSelected = QtGui.QLabel(self.printSelectedLocalPage)
        self.printPreviewSelected.setGeometry(QtCore.QRect(260, 20, 210, 210))
        self.printPreviewSelected.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.printPreviewSelected.setText(_fromUtf8(""))
        self.printPreviewSelected.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/thumbnail.png")))
        self.printPreviewSelected.setScaledContents(True)
        self.printPreviewSelected.setObjectName(_fromUtf8("printPreviewSelected"))
        self.printPreviewSelected.raise_()
        self.fileSelected.raise_()
        self.fileSelectedBackButton.raise_()
        self.fileSelectedPrintButton.raise_()
        self.fileSizeSelected.raise_()
        self.fileDateSelected.raise_()
        self.filePrintTimeSelected.raise_()
        self.filamentVolumeSelected.raise_()
        self.fileSizeSelectedLabel.raise_()
        self.fileDateSelectedLabel.raise_()
        self.filePrintTimeSelectedLabel.raise_()
        self.filamentVolumeSelectedLabel.raise_()
        self.filamentLengthFileSelected.raise_()
        self.filamentLengthSelectedLabel.raise_()
        self.stackedWidget.addWidget(self.printSelectedLocalPage)
        self.printSelectedUSBPage = QtGui.QWidget()
        self.printSelectedUSBPage.setObjectName(_fromUtf8("printSelectedUSBPage"))
        self.fileSelectedUSBTransferButton = QtGui.QToolButton(self.printSelectedUSBPage)
        self.fileSelectedUSBTransferButton.setGeometry(QtCore.QRect(0, 230, 161, 91))
        self.fileSelectedUSBTransferButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        self.fileSelectedUSBTransferButton.setFont(font)
        self.fileSelectedUSBTransferButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.fileSelectedUSBTransferButton.setIcon(icon18)
        self.fileSelectedUSBTransferButton.setIconSize(QtCore.QSize(40, 40))
        self.fileSelectedUSBTransferButton.setCheckable(False)
        self.fileSelectedUSBTransferButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.fileSelectedUSBTransferButton.setObjectName(_fromUtf8("fileSelectedUSBTransferButton"))
        self.printPreviewSelectedUSB = QtGui.QLabel(self.printSelectedUSBPage)
        self.printPreviewSelectedUSB.setGeometry(QtCore.QRect(130, 20, 210, 210))
        self.printPreviewSelectedUSB.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.printPreviewSelectedUSB.setText(_fromUtf8(""))
        self.printPreviewSelectedUSB.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/thumbnail.png")))
        self.printPreviewSelectedUSB.setScaledContents(True)
        self.printPreviewSelectedUSB.setObjectName(_fromUtf8("printPreviewSelectedUSB"))
        self.fileSelectedUSBBackButton = QtGui.QPushButton(self.printSelectedUSBPage)
        self.fileSelectedUSBBackButton.setGeometry(QtCore.QRect(320, 230, 161, 91))
        self.fileSelectedUSBBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.fileSelectedUSBBackButton.setFont(font)
        self.fileSelectedUSBBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}"))
        self.fileSelectedUSBBackButton.setText(_fromUtf8(""))
        self.fileSelectedUSBBackButton.setIcon(icon4)
        self.fileSelectedUSBBackButton.setIconSize(QtCore.QSize(50, 50))
        self.fileSelectedUSBBackButton.setCheckable(False)
        self.fileSelectedUSBBackButton.setAutoDefault(False)
        self.fileSelectedUSBBackButton.setDefault(False)
        self.fileSelectedUSBBackButton.setFlat(False)
        self.fileSelectedUSBBackButton.setObjectName(_fromUtf8("fileSelectedUSBBackButton"))
        self.fileSelectedUSBName = QtGui.QLabel(self.printSelectedUSBPage)
        self.fileSelectedUSBName.setGeometry(QtCore.QRect(0, 0, 481, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.fileSelectedUSBName.setFont(font)
        self.fileSelectedUSBName.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.fileSelectedUSBName.setObjectName(_fromUtf8("fileSelectedUSBName"))
        self.fileSelectedUSBPrintButton = QtGui.QToolButton(self.printSelectedUSBPage)
        self.fileSelectedUSBPrintButton.setGeometry(QtCore.QRect(160, 230, 161, 91))
        self.fileSelectedUSBPrintButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        self.fileSelectedUSBPrintButton.setFont(font)
        self.fileSelectedUSBPrintButton.setStyleSheet(_fromUtf8("QToolButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}"))
        self.fileSelectedUSBPrintButton.setIcon(icon5)
        self.fileSelectedUSBPrintButton.setIconSize(QtCore.QSize(40, 40))
        self.fileSelectedUSBPrintButton.setCheckable(False)
        self.fileSelectedUSBPrintButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.fileSelectedUSBPrintButton.setObjectName(_fromUtf8("fileSelectedUSBPrintButton"))
        self.printPreviewSelectedUSB.raise_()
        self.fileSelectedUSBTransferButton.raise_()
        self.fileSelectedUSBBackButton.raise_()
        self.fileSelectedUSBName.raise_()
        self.fileSelectedUSBPrintButton.raise_()
        self.stackedWidget.addWidget(self.printSelectedUSBPage)
        self.controlPage = QtGui.QWidget()
        self.controlPage.setObjectName(_fromUtf8("controlPage"))
        self.controlTabWidget = QtGui.QTabWidget(self.controlPage)
        self.controlTabWidget.setGeometry(QtCore.QRect(0, 0, 491, 321))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(12)
        self.controlTabWidget.setFont(font)
        self.controlTabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.controlTabWidget.setAutoFillBackground(False)
        self.controlTabWidget.setStyleSheet(_fromUtf8("QTabWidget::pane { /* The tab widget frame */\n"
"    position: absolute;\n"
"\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"   border-right: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    width: 69px;\n"
"     height: 50px;\n"
"    padding-left: 25px;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"/*    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"*/\n"
"background-color: rgb(40, 40, 40);\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"QTabBar::tab:first {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"/*border-bottom-left-radius: 15px;*/\n"
"}\n"
"QTabBar::tab:last {\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"QTabBar::tab:focus {\n"
"    outline: none;\n"
"}\n"
"QTabBar:focus {\n"
"    outline: none;\n"
"}"))
        self.controlTabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.controlTabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.controlTabWidget.setIconSize(QtCore.QSize(45, 45))
        self.controlTabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.controlTabWidget.setUsesScrollButtons(False)
        self.controlTabWidget.setTabsClosable(False)
        self.controlTabWidget.setObjectName(_fromUtf8("controlTabWidget"))
        self.feedRateTab = QtGui.QWidget()
        self.feedRateTab.setObjectName(_fromUtf8("feedRateTab"))
        self.flowRateLabelControlPage_2 = QtGui.QLabel(self.feedRateTab)
        self.flowRateLabelControlPage_2.setGeometry(QtCore.QRect(65, 40, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.flowRateLabelControlPage_2.setFont(font)
        self.flowRateLabelControlPage_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.flowRateLabelControlPage_2.setObjectName(_fromUtf8("flowRateLabelControlPage_2"))
        self.feedRateSpinBox = QtGui.QSpinBox(self.feedRateTab)
        self.feedRateSpinBox.setGeometry(QtCore.QRect(62, 28, 241, 136))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(24)
        self.feedRateSpinBox.setFont(font)
        self.feedRateSpinBox.setStyleSheet(_fromUtf8("QSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow { image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px; }\n"
"\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
""))
        self.feedRateSpinBox.setFrame(False)
        self.feedRateSpinBox.setReadOnly(False)
        self.feedRateSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.feedRateSpinBox.setAccelerated(True)
        self.feedRateSpinBox.setMinimum(50)
        self.feedRateSpinBox.setMaximum(200)
        self.feedRateSpinBox.setSingleStep(1)
        self.feedRateSpinBox.setProperty("value", 100)
        self.feedRateSpinBox.setObjectName(_fromUtf8("feedRateSpinBox"))
        self.setFeedRateButton = QtGui.QPushButton(self.feedRateTab)
        self.setFeedRateButton.setGeometry(QtCore.QRect(300, 30, 91, 132))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.setFeedRateButton.setFont(font)
        self.setFeedRateButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.setFeedRateButton.setText(_fromUtf8(""))
        self.setFeedRateButton.setIcon(icon14)
        self.setFeedRateButton.setIconSize(QtCore.QSize(50, 50))
        self.setFeedRateButton.setObjectName(_fromUtf8("setFeedRateButton"))
        self.feedRateSpinBox.raise_()
        self.flowRateLabelControlPage_2.raise_()
        self.setFeedRateButton.raise_()
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/FeedRate.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/FeedRate_Selected.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.controlTabWidget.addTab(self.feedRateTab, icon19, _fromUtf8(""))
        self.temperatureTab = QtGui.QWidget()
        self.temperatureTab.setObjectName(_fromUtf8("temperatureTab"))
        self.toolLabel = QtGui.QLabel(self.temperatureTab)
        self.toolLabel.setGeometry(QtCore.QRect(0, 20, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.toolLabel.setFont(font)
        self.toolLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.toolLabel.setObjectName(_fromUtf8("toolLabel"))
        self.cooldownButton = QtGui.QPushButton(self.temperatureTab)
        self.cooldownButton.setGeometry(QtCore.QRect(120, 210, 101, 60))
        self.cooldownButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.cooldownButton.setFont(font)
        self.cooldownButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.cooldownButton.setText(_fromUtf8(""))
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/snowflake.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cooldownButton.setIcon(icon20)
        self.cooldownButton.setIconSize(QtCore.QSize(40, 40))
        self.cooldownButton.setObjectName(_fromUtf8("cooldownButton"))
        self.fanOffButton = QtGui.QPushButton(self.temperatureTab)
        self.fanOffButton.setGeometry(QtCore.QRect(300, 210, 81, 60))
        self.fanOffButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.fanOffButton.setFont(font)
        self.fanOffButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.fanOffButton.setText(_fromUtf8(""))
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/fan-black-silhouette-off.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fanOffButton.setIcon(icon21)
        self.fanOffButton.setIconSize(QtCore.QSize(40, 40))
        self.fanOffButton.setCheckable(False)
        self.fanOffButton.setAutoDefault(False)
        self.fanOffButton.setDefault(False)
        self.fanOffButton.setFlat(False)
        self.fanOffButton.setObjectName(_fromUtf8("fanOffButton"))
        self.fanOnButton = QtGui.QPushButton(self.temperatureTab)
        self.fanOnButton.setGeometry(QtCore.QRect(220, 210, 81, 60))
        self.fanOnButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.fanOnButton.setFont(font)
        self.fanOnButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.fanOnButton.setText(_fromUtf8(""))
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/fan-black-silhouette.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fanOnButton.setIcon(icon22)
        self.fanOnButton.setIconSize(QtCore.QSize(40, 40))
        self.fanOnButton.setCheckable(False)
        self.fanOnButton.setAutoDefault(False)
        self.fanOnButton.setDefault(False)
        self.fanOnButton.setFlat(False)
        self.fanOnButton.setObjectName(_fromUtf8("fanOnButton"))
        self.toolTempSpinBox = QtGui.QSpinBox(self.temperatureTab)
        self.toolTempSpinBox.setGeometry(QtCore.QRect(0, 60, 161, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.toolTempSpinBox.setFont(font)
        self.toolTempSpinBox.setStyleSheet(_fromUtf8("QSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow { image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px; }\n"
"\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
""))
        self.toolTempSpinBox.setReadOnly(False)
        self.toolTempSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.toolTempSpinBox.setAccelerated(True)
        self.toolTempSpinBox.setMaximum(300)
        self.toolTempSpinBox.setSingleStep(1)
        self.toolTempSpinBox.setProperty("value", 0)
        self.toolTempSpinBox.setObjectName(_fromUtf8("toolTempSpinBox"))
        self.setToolTempButton = QtGui.QPushButton(self.temperatureTab)
        self.setToolTempButton.setGeometry(QtCore.QRect(159, 60, 71, 130))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.setToolTempButton.setFont(font)
        self.setToolTempButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-right-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.setToolTempButton.setText(_fromUtf8(""))
        self.setToolTempButton.setIcon(icon14)
        self.setToolTempButton.setIconSize(QtCore.QSize(50, 50))
        self.setToolTempButton.setObjectName(_fromUtf8("setToolTempButton"))
        self.bedTempSpinBox = QtGui.QSpinBox(self.temperatureTab)
        self.bedTempSpinBox.setGeometry(QtCore.QRect(241, 58, 161, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.bedTempSpinBox.setFont(font)
        self.bedTempSpinBox.setStyleSheet(_fromUtf8("QSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow { image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px; }\n"
"\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
""))
        self.bedTempSpinBox.setReadOnly(False)
        self.bedTempSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.bedTempSpinBox.setAccelerated(True)
        self.bedTempSpinBox.setMaximum(150)
        self.bedTempSpinBox.setSingleStep(1)
        self.bedTempSpinBox.setProperty("value", 0)
        self.bedTempSpinBox.setObjectName(_fromUtf8("bedTempSpinBox"))
        self.bedLabel_2 = QtGui.QLabel(self.temperatureTab)
        self.bedLabel_2.setGeometry(QtCore.QRect(341, 18, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.bedLabel_2.setFont(font)
        self.bedLabel_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.bedLabel_2.setObjectName(_fromUtf8("bedLabel_2"))
        self.setBedTempButton = QtGui.QPushButton(self.temperatureTab)
        self.setBedTempButton.setGeometry(QtCore.QRect(400, 60, 71, 128))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.setBedTempButton.setFont(font)
        self.setBedTempButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.setBedTempButton.setText(_fromUtf8(""))
        self.setBedTempButton.setIcon(icon14)
        self.setBedTempButton.setIconSize(QtCore.QSize(50, 50))
        self.setBedTempButton.setObjectName(_fromUtf8("setBedTempButton"))
        self.toolLabel.raise_()
        self.cooldownButton.raise_()
        self.fanOffButton.raise_()
        self.fanOnButton.raise_()
        self.setToolTempButton.raise_()
        self.toolTempSpinBox.raise_()
        self.bedTempSpinBox.raise_()
        self.bedLabel_2.raise_()
        self.setBedTempButton.raise_()
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/thermometer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/thermometer_Selected.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.controlTabWidget.addTab(self.temperatureTab, icon23, _fromUtf8(""))
        self.motionTab = QtGui.QWidget()
        self.motionTab.setObjectName(_fromUtf8("motionTab"))
        self.step1Button = QtGui.QPushButton(self.motionTab)
        self.step1Button.setGeometry(QtCore.QRect(102, 225, 100, 45))
        self.step1Button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.step1Button.setFont(font)
        self.step1Button.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"     border-bottom: none; /* no border for a flat push button */\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border-bottom: none; /* no border for a flat push button */\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.step1Button.setIconSize(QtCore.QSize(40, 40))
        self.step1Button.setCheckable(False)
        self.step1Button.setAutoDefault(False)
        self.step1Button.setDefault(False)
        self.step1Button.setFlat(False)
        self.step1Button.setObjectName(_fromUtf8("step1Button"))
        self.step10Button = QtGui.QPushButton(self.motionTab)
        self.step10Button.setGeometry(QtCore.QRect(201, 225, 100, 45))
        self.step10Button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.step10Button.setFont(font)
        self.step10Button.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"     border-bottom: none; /* no border for a flat push button */\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border-bottom: none; /* no border for a flat push button */\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.step10Button.setIconSize(QtCore.QSize(40, 40))
        self.step10Button.setCheckable(False)
        self.step10Button.setAutoDefault(False)
        self.step10Button.setDefault(False)
        self.step10Button.setFlat(False)
        self.step10Button.setObjectName(_fromUtf8("step10Button"))
        self.step100Button = QtGui.QPushButton(self.motionTab)
        self.step100Button.setGeometry(QtCore.QRect(300, 225, 101, 45))
        self.step100Button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.step100Button.setFont(font)
        self.step100Button.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"     border-bottom: none; /* no border for a flat push button */\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border-bottom: none; /* no border for a flat push button */\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.step100Button.setIconSize(QtCore.QSize(40, 40))
        self.step100Button.setCheckable(True)
        self.step100Button.setChecked(False)
        self.step100Button.setAutoDefault(False)
        self.step100Button.setDefault(False)
        self.step100Button.setFlat(False)
        self.step100Button.setObjectName(_fromUtf8("step100Button"))
        self.moveYPButton = QtGui.QPushButton(self.motionTab)
        self.moveYPButton.setGeometry(QtCore.QRect(80, 6, 70, 70))
        self.moveYPButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveYPButton.setFont(font)
        self.moveYPButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.moveYPButton.setText(_fromUtf8(""))
        self.moveYPButton.setIcon(icon13)
        self.moveYPButton.setIconSize(QtCore.QSize(40, 40))
        self.moveYPButton.setCheckable(False)
        self.moveYPButton.setAutoDefault(False)
        self.moveYPButton.setDefault(False)
        self.moveYPButton.setFlat(False)
        self.moveYPButton.setObjectName(_fromUtf8("moveYPButton"))
        self.moveYMButton = QtGui.QPushButton(self.motionTab)
        self.moveYMButton.setGeometry(QtCore.QRect(80, 144, 70, 70))
        self.moveYMButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveYMButton.setFont(font)
        self.moveYMButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.moveYMButton.setText(_fromUtf8(""))
        self.moveYMButton.setIcon(icon12)
        self.moveYMButton.setIconSize(QtCore.QSize(40, 40))
        self.moveYMButton.setCheckable(False)
        self.moveYMButton.setAutoDefault(False)
        self.moveYMButton.setDefault(False)
        self.moveYMButton.setFlat(False)
        self.moveYMButton.setObjectName(_fromUtf8("moveYMButton"))
        self.moveXPButton = QtGui.QPushButton(self.motionTab)
        self.moveXPButton.setGeometry(QtCore.QRect(149, 75, 70, 70))
        self.moveXPButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveXPButton.setFont(font)
        self.moveXPButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.moveXPButton.setText(_fromUtf8(""))
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/arrows-2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moveXPButton.setIcon(icon24)
        self.moveXPButton.setIconSize(QtCore.QSize(40, 40))
        self.moveXPButton.setCheckable(False)
        self.moveXPButton.setAutoDefault(False)
        self.moveXPButton.setDefault(False)
        self.moveXPButton.setFlat(False)
        self.moveXPButton.setObjectName(_fromUtf8("moveXPButton"))
        self.moveXMButton = QtGui.QPushButton(self.motionTab)
        self.moveXMButton.setGeometry(QtCore.QRect(11, 75, 70, 70))
        self.moveXMButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveXMButton.setFont(font)
        self.moveXMButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-left-radius: 15px;\n"
"    border-bottom-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.moveXMButton.setText(_fromUtf8(""))
        self.moveXMButton.setIcon(icon4)
        self.moveXMButton.setIconSize(QtCore.QSize(40, 40))
        self.moveXMButton.setCheckable(False)
        self.moveXMButton.setAutoDefault(False)
        self.moveXMButton.setDefault(False)
        self.moveXMButton.setFlat(False)
        self.moveXMButton.setObjectName(_fromUtf8("moveXMButton"))
        self.homeXYButton = QtGui.QPushButton(self.motionTab)
        self.homeXYButton.setGeometry(QtCore.QRect(80, 75, 70, 70))
        self.homeXYButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.homeXYButton.setFont(font)
        self.homeXYButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.homeXYButton.setText(_fromUtf8(""))
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/home-icon-silhouette.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeXYButton.setIcon(icon25)
        self.homeXYButton.setIconSize(QtCore.QSize(40, 40))
        self.homeXYButton.setCheckable(False)
        self.homeXYButton.setAutoDefault(False)
        self.homeXYButton.setDefault(False)
        self.homeXYButton.setFlat(False)
        self.homeXYButton.setObjectName(_fromUtf8("homeXYButton"))
        self.homeZButton = QtGui.QPushButton(self.motionTab)
        self.homeZButton.setGeometry(QtCore.QRect(240, 75, 70, 70))
        self.homeZButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.homeZButton.setFont(font)
        self.homeZButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.homeZButton.setText(_fromUtf8(""))
        self.homeZButton.setIcon(icon25)
        self.homeZButton.setIconSize(QtCore.QSize(40, 40))
        self.homeZButton.setCheckable(False)
        self.homeZButton.setAutoDefault(False)
        self.homeZButton.setDefault(False)
        self.homeZButton.setFlat(False)
        self.homeZButton.setObjectName(_fromUtf8("homeZButton"))
        self.motorOffButton = QtGui.QPushButton(self.motionTab)
        self.motorOffButton.setGeometry(QtCore.QRect(400, 225, 81, 45))
        self.motorOffButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.motorOffButton.setFont(font)
        self.motorOffButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"     border-bottom: none; /* no border for a flat push button */\n"
" border-top-right-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}"))
        self.motorOffButton.setText(_fromUtf8(""))
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/motor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.motorOffButton.setIcon(icon26)
        self.motorOffButton.setIconSize(QtCore.QSize(40, 40))
        self.motorOffButton.setCheckable(False)
        self.motorOffButton.setAutoDefault(False)
        self.motorOffButton.setDefault(False)
        self.motorOffButton.setFlat(False)
        self.motorOffButton.setObjectName(_fromUtf8("motorOffButton"))
        self.moveZMButton = QtGui.QPushButton(self.motionTab)
        self.moveZMButton.setGeometry(QtCore.QRect(240, 6, 70, 70))
        self.moveZMButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveZMButton.setFont(font)
        self.moveZMButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.moveZMButton.setText(_fromUtf8(""))
        self.moveZMButton.setIcon(icon13)
        self.moveZMButton.setIconSize(QtCore.QSize(40, 40))
        self.moveZMButton.setCheckable(False)
        self.moveZMButton.setAutoDefault(False)
        self.moveZMButton.setDefault(False)
        self.moveZMButton.setFlat(False)
        self.moveZMButton.setObjectName(_fromUtf8("moveZMButton"))
        self.moveZPButton = QtGui.QPushButton(self.motionTab)
        self.moveZPButton.setGeometry(QtCore.QRect(240, 144, 70, 70))
        self.moveZPButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.moveZPButton.setFont(font)
        self.moveZPButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.moveZPButton.setText(_fromUtf8(""))
        self.moveZPButton.setIcon(icon12)
        self.moveZPButton.setIconSize(QtCore.QSize(40, 40))
        self.moveZPButton.setCheckable(False)
        self.moveZPButton.setAutoDefault(False)
        self.moveZPButton.setDefault(False)
        self.moveZPButton.setFlat(False)
        self.moveZPButton.setObjectName(_fromUtf8("moveZPButton"))
        self.XYLabel = QtGui.QLabel(self.motionTab)
        self.XYLabel.setGeometry(QtCore.QRect(2, 10, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.XYLabel.setFont(font)
        self.XYLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.XYLabel.setObjectName(_fromUtf8("XYLabel"))
        self.ZLabel = QtGui.QLabel(self.motionTab)
        self.ZLabel.setGeometry(QtCore.QRect(200, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ZLabel.setFont(font)
        self.ZLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.ZLabel.setObjectName(_fromUtf8("ZLabel"))
        self.retractButton = QtGui.QPushButton(self.motionTab)
        self.retractButton.setGeometry(QtCore.QRect(370, 110, 70, 81))
        self.retractButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.retractButton.setFont(font)
        self.retractButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.retractButton.setText(_fromUtf8(""))
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.retractButton.setIcon(icon27)
        self.retractButton.setIconSize(QtCore.QSize(40, 40))
        self.retractButton.setCheckable(False)
        self.retractButton.setAutoDefault(False)
        self.retractButton.setDefault(False)
        self.retractButton.setFlat(False)
        self.retractButton.setObjectName(_fromUtf8("retractButton"))
        self.extruderButton = QtGui.QPushButton(self.motionTab)
        self.extruderButton.setGeometry(QtCore.QRect(370, 30, 70, 81))
        self.extruderButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)
        self.extruderButton.setFont(font)
        self.extruderButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.extruderButton.setText(_fromUtf8(""))
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.extruderButton.setIcon(icon28)
        self.extruderButton.setIconSize(QtCore.QSize(40, 40))
        self.extruderButton.setCheckable(False)
        self.extruderButton.setAutoDefault(False)
        self.extruderButton.setDefault(False)
        self.extruderButton.setFlat(False)
        self.extruderButton.setObjectName(_fromUtf8("extruderButton"))
        self.ELabel = QtGui.QLabel(self.motionTab)
        self.ELabel.setGeometry(QtCore.QRect(320, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ELabel.setFont(font)
        self.ELabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.ELabel.setObjectName(_fromUtf8("ELabel"))
        self.moveByLabel = QtGui.QLabel(self.motionTab)
        self.moveByLabel.setGeometry(QtCore.QRect(10, 235, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.moveByLabel.setFont(font)
        self.moveByLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.moveByLabel.setObjectName(_fromUtf8("moveByLabel"))
        self.moveByLabel.raise_()
        self.step1Button.raise_()
        self.step10Button.raise_()
        self.step100Button.raise_()
        self.moveYPButton.raise_()
        self.moveYMButton.raise_()
        self.moveXPButton.raise_()
        self.moveXMButton.raise_()
        self.homeXYButton.raise_()
        self.homeZButton.raise_()
        self.motorOffButton.raise_()
        self.moveZMButton.raise_()
        self.moveZPButton.raise_()
        self.XYLabel.raise_()
        self.ZLabel.raise_()
        self.retractButton.raise_()
        self.extruderButton.raise_()
        self.ELabel.raise_()
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Motion.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon29.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Motion_Selected.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.controlTabWidget.addTab(self.motionTab, icon29, _fromUtf8(""))
        self.filamentTab = QtGui.QWidget()
        self.filamentTab.setObjectName(_fromUtf8("filamentTab"))
        self.changeFilamentButton = QtGui.QToolButton(self.filamentTab)
        self.changeFilamentButton.setGeometry(QtCore.QRect(110, 180, 241, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(12)
        self.changeFilamentButton.setFont(font)
        self.changeFilamentButton.setStyleSheet(_fromUtf8("QToolButton  {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 15px;\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton :pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton :flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton :default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QToolButton :focus {\n"
"    outline: none;\n"
"}"))
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/changeFilament.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changeFilamentButton.setIcon(icon30)
        self.changeFilamentButton.setIconSize(QtCore.QSize(60, 60))
        self.changeFilamentButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.changeFilamentButton.setObjectName(_fromUtf8("changeFilamentButton"))
        self.setFlowRateButton = QtGui.QPushButton(self.filamentTab)
        self.setFlowRateButton.setGeometry(QtCore.QRect(300, 30, 91, 132))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.setFlowRateButton.setFont(font)
        self.setFlowRateButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.setFlowRateButton.setText(_fromUtf8(""))
        self.setFlowRateButton.setIcon(icon14)
        self.setFlowRateButton.setIconSize(QtCore.QSize(50, 50))
        self.setFlowRateButton.setObjectName(_fromUtf8("setFlowRateButton"))
        self.flowRateSpinBox = QtGui.QSpinBox(self.filamentTab)
        self.flowRateSpinBox.setGeometry(QtCore.QRect(62, 28, 241, 136))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(24)
        self.flowRateSpinBox.setFont(font)
        self.flowRateSpinBox.setStyleSheet(_fromUtf8("QSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow { image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px; }\n"
"\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
""))
        self.flowRateSpinBox.setFrame(False)
        self.flowRateSpinBox.setReadOnly(False)
        self.flowRateSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.flowRateSpinBox.setAccelerated(True)
        self.flowRateSpinBox.setMinimum(75)
        self.flowRateSpinBox.setMaximum(125)
        self.flowRateSpinBox.setSingleStep(1)
        self.flowRateSpinBox.setProperty("value", 100)
        self.flowRateSpinBox.setObjectName(_fromUtf8("flowRateSpinBox"))
        self.flowRateLabelControlPage = QtGui.QLabel(self.filamentTab)
        self.flowRateLabelControlPage.setGeometry(QtCore.QRect(65, 40, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.flowRateLabelControlPage.setFont(font)
        self.flowRateLabelControlPage.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.flowRateLabelControlPage.setObjectName(_fromUtf8("flowRateLabelControlPage"))
        self.flowRateSpinBox.raise_()
        self.setFlowRateButton.raise_()
        self.flowRateLabelControlPage.raise_()
        self.changeFilamentButton.raise_()
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Spool.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon31.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/Spool_Selected.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon31.addPixmap(QtGui.QPixmap(_fromUtf8("png/Spool.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon31.addPixmap(QtGui.QPixmap(_fromUtf8("png/Spool_Selected.png")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon31.addPixmap(QtGui.QPixmap(_fromUtf8("png/Spool_Selected.png")), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.controlTabWidget.addTab(self.filamentTab, icon31, _fromUtf8(""))
        self.controlBackButton = QtGui.QPushButton(self.controlPage)
        self.controlBackButton.setGeometry(QtCore.QRect(380, 0, 100, 50))
        self.controlBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.controlBackButton.setFont(font)
        self.controlBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"    border: none; /* no border for a flat push button */\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    /*border-bottom-right-radius: 15px;*/\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
"}"))
        self.controlBackButton.setText(_fromUtf8(""))
        self.controlBackButton.setIcon(icon4)
        self.controlBackButton.setIconSize(QtCore.QSize(40, 40))
        self.controlBackButton.setCheckable(False)
        self.controlBackButton.setAutoDefault(False)
        self.controlBackButton.setDefault(False)
        self.controlBackButton.setFlat(False)
        self.controlBackButton.setObjectName(_fromUtf8("controlBackButton"))
        self.stackedWidget.addWidget(self.controlPage)
        self.changeFilamentPage = QtGui.QWidget()
        self.changeFilamentPage.setObjectName(_fromUtf8("changeFilamentPage"))
        self.selectFilamentlabel = QtGui.QLabel(self.changeFilamentPage)
        self.selectFilamentlabel.setGeometry(QtCore.QRect(0, 0, 381, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.selectFilamentlabel.setFont(font)
        self.selectFilamentlabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.selectFilamentlabel.setObjectName(_fromUtf8("selectFilamentlabel"))
        self.changeFilamentComboBox = QtGui.QComboBox(self.changeFilamentPage)
        self.changeFilamentComboBox.setGeometry(QtCore.QRect(0, 40, 481, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(24)
        self.changeFilamentComboBox.setFont(font)
        self.changeFilamentComboBox.setStyleSheet(_fromUtf8(" QScrollBar:vertical {\n"
"     border: 1px solid black;\n"
"border-radius: 5px;\n"
"    background-color: rgb(40,40,40);\n"
"     width: 60px;\n"
"     margin: 67px 0 67px 0;\n"
" }\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 7px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height:65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height: 65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
" image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"QScrollBar::down-arrow:vertical {\n"
" image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QComboBox {\n"
"border: 1px solid black;\n"
"    padding: 0px 18px 0px 3px;\n"
"    min-width: 6em;\n"
"\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 50px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"\n"
"image: url(./templates/img/arrows-5.png);\n"
"width: 30px;\n"
"height: 30px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(40, 40, 40);\n"
"    background: white;\n"
"}"))
        self.changeFilamentComboBox.setEditable(False)
        self.changeFilamentComboBox.setMaxVisibleItems(8)
        self.changeFilamentComboBox.setIconSize(QtCore.QSize(30, 30))
        self.changeFilamentComboBox.setObjectName(_fromUtf8("changeFilamentComboBox"))
        self.changeFilamentLoadButton = QtGui.QPushButton(self.changeFilamentPage)
        self.changeFilamentLoadButton.setGeometry(QtCore.QRect(0, 170, 241, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.changeFilamentLoadButton.setFont(font)
        self.changeFilamentLoadButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/load.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changeFilamentLoadButton.setIcon(icon32)
        self.changeFilamentLoadButton.setIconSize(QtCore.QSize(60, 60))
        self.changeFilamentLoadButton.setObjectName(_fromUtf8("changeFilamentLoadButton"))
        self.changeFilamentUnloadButton = QtGui.QPushButton(self.changeFilamentPage)
        self.changeFilamentUnloadButton.setGeometry(QtCore.QRect(240, 170, 240, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(20)
        self.changeFilamentUnloadButton.setFont(font)
        self.changeFilamentUnloadButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(_fromUtf8("templates/img/unload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changeFilamentUnloadButton.setIcon(icon33)
        self.changeFilamentUnloadButton.setIconSize(QtCore.QSize(60, 60))
        self.changeFilamentUnloadButton.setObjectName(_fromUtf8("changeFilamentUnloadButton"))
        self.changeFilamentBackButton = QtGui.QPushButton(self.changeFilamentPage)
        self.changeFilamentBackButton.setGeometry(QtCore.QRect(0, 260, 480, 60))
        self.changeFilamentBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(9)
        self.changeFilamentBackButton.setFont(font)
        self.changeFilamentBackButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.changeFilamentBackButton.setText(_fromUtf8(""))
        self.changeFilamentBackButton.setIcon(icon4)
        self.changeFilamentBackButton.setIconSize(QtCore.QSize(50, 50))
        self.changeFilamentBackButton.setCheckable(False)
        self.changeFilamentBackButton.setAutoDefault(False)
        self.changeFilamentBackButton.setDefault(False)
        self.changeFilamentBackButton.setFlat(False)
        self.changeFilamentBackButton.setObjectName(_fromUtf8("changeFilamentBackButton"))
        self.stackedWidget.addWidget(self.changeFilamentPage)
        self.changeFilamentProgressPage = QtGui.QWidget()
        self.changeFilamentProgressPage.setObjectName(_fromUtf8("changeFilamentProgressPage"))
        self.changeFilamentStatus = QtGui.QLabel(self.changeFilamentProgressPage)
        self.changeFilamentStatus.setGeometry(QtCore.QRect(0, 160, 471, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.changeFilamentStatus.setFont(font)
        self.changeFilamentStatus.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.changeFilamentStatus.setObjectName(_fromUtf8("changeFilamentStatus"))
        self.changeFilamentProgress = QtGui.QProgressBar(self.changeFilamentProgressPage)
        self.changeFilamentProgress.setGeometry(QtCore.QRect(0, 190, 481, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.changeFilamentProgress.setFont(font)
        self.changeFilamentProgress.setStyleSheet(_fromUtf8("QProgressBar::chunk {\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.517, x2:0, y2:0.512, stop:0 rgba(255, 28, 35, 255), stop:1 rgba(255, 68, 74, 255));\n"
"border-bottom-right-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
" /*  border-bottom-left-radius: 10px;\n"
" border-bottom-right-radius: 10px;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(180, 180, 180, 255));\n"
"}\n"
""))
        self.changeFilamentProgress.setMaximum(100)
        self.changeFilamentProgress.setProperty("value", 0)
        self.changeFilamentProgress.setAlignment(QtCore.Qt.AlignCenter)
        self.changeFilamentProgress.setTextVisible(True)
        self.changeFilamentProgress.setOrientation(QtCore.Qt.Horizontal)
        self.changeFilamentProgress.setObjectName(_fromUtf8("changeFilamentProgress"))
        self.changeFilamentNameOperation = QtGui.QLabel(self.changeFilamentProgressPage)
        self.changeFilamentNameOperation.setGeometry(QtCore.QRect(0, 0, 471, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.changeFilamentNameOperation.setFont(font)
        self.changeFilamentNameOperation.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.changeFilamentNameOperation.setObjectName(_fromUtf8("changeFilamentNameOperation"))
        self.changeFilamentBackButton2 = QtGui.QPushButton(self.changeFilamentProgressPage)
        self.changeFilamentBackButton2.setGeometry(QtCore.QRect(0, 230, 481, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(13)
        self.changeFilamentBackButton2.setFont(font)
        self.changeFilamentBackButton2.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.changeFilamentBackButton2.setText(_fromUtf8(""))
        self.changeFilamentBackButton2.setIcon(icon4)
        self.changeFilamentBackButton2.setIconSize(QtCore.QSize(50, 50))
        self.changeFilamentBackButton2.setObjectName(_fromUtf8("changeFilamentBackButton2"))
        self.label_2 = QtGui.QLabel(self.changeFilamentProgressPage)
        self.label_2.setGeometry(QtCore.QRect(190, 55, 100, 100))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/changeFilament2.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.stackedWidget.addWidget(self.changeFilamentProgressPage)
        self.changeFilamentExtrudePage = QtGui.QWidget()
        self.changeFilamentExtrudePage.setObjectName(_fromUtf8("changeFilamentExtrudePage"))
        self.feedFilamentlabel = QtGui.QLabel(self.changeFilamentExtrudePage)
        self.feedFilamentlabel.setGeometry(QtCore.QRect(10, 10, 461, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.feedFilamentlabel.setFont(font)
        self.feedFilamentlabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.feedFilamentlabel.setObjectName(_fromUtf8("feedFilamentlabel"))
        self.loadDoneButton = QtGui.QPushButton(self.changeFilamentExtrudePage)
        self.loadDoneButton.setGeometry(QtCore.QRect(0, 230, 480, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(16)
        self.loadDoneButton.setFont(font)
        self.loadDoneButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.loadDoneButton.setIconSize(QtCore.QSize(40, 40))
        self.loadDoneButton.setObjectName(_fromUtf8("loadDoneButton"))
        self.ExtrudeButton = QtGui.QPushButton(self.changeFilamentExtrudePage)
        self.ExtrudeButton.setGeometry(QtCore.QRect(0, 140, 480, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(16)
        self.ExtrudeButton.setFont(font)
        self.ExtrudeButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.ExtrudeButton.setIconSize(QtCore.QSize(40, 40))
        self.ExtrudeButton.setObjectName(_fromUtf8("ExtrudeButton"))
        self.feedFilamentlabel_2 = QtGui.QLabel(self.changeFilamentExtrudePage)
        self.feedFilamentlabel_2.setGeometry(QtCore.QRect(10, 40, 461, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.feedFilamentlabel_2.setFont(font)
        self.feedFilamentlabel_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.feedFilamentlabel_2.setObjectName(_fromUtf8("feedFilamentlabel_2"))
        self.stackedWidget.addWidget(self.changeFilamentExtrudePage)
        self.changeFilamentRetractPage = QtGui.QWidget()
        self.changeFilamentRetractPage.setObjectName(_fromUtf8("changeFilamentRetractPage"))
        self.feedFilamentlabel_3 = QtGui.QLabel(self.changeFilamentRetractPage)
        self.feedFilamentlabel_3.setGeometry(QtCore.QRect(10, 40, 461, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.feedFilamentlabel_3.setFont(font)
        self.feedFilamentlabel_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.feedFilamentlabel_3.setObjectName(_fromUtf8("feedFilamentlabel_3"))
        self.unloadDoneButton = QtGui.QPushButton(self.changeFilamentRetractPage)
        self.unloadDoneButton.setGeometry(QtCore.QRect(0, 230, 480, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(16)
        self.unloadDoneButton.setFont(font)
        self.unloadDoneButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.unloadDoneButton.setIconSize(QtCore.QSize(40, 40))
        self.unloadDoneButton.setObjectName(_fromUtf8("unloadDoneButton"))
        self.feedFilamentlabel_4 = QtGui.QLabel(self.changeFilamentRetractPage)
        self.feedFilamentlabel_4.setGeometry(QtCore.QRect(10, 10, 461, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham Light"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.feedFilamentlabel_4.setFont(font)
        self.feedFilamentlabel_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.feedFilamentlabel_4.setObjectName(_fromUtf8("feedFilamentlabel_4"))
        self.retractFilamentButton = QtGui.QPushButton(self.changeFilamentRetractPage)
        self.retractFilamentButton.setGeometry(QtCore.QRect(0, 140, 480, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(16)
        self.retractFilamentButton.setFont(font)
        self.retractFilamentButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
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
        self.retractFilamentButton.setIconSize(QtCore.QSize(40, 40))
        self.retractFilamentButton.setObjectName(_fromUtf8("retractFilamentButton"))
        self.stackedWidget.addWidget(self.changeFilamentRetractPage)
        MainWindow.setCentralWidget(self.mainApplication)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.controlTabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.FileNameLabel.setText(_translate("MainWindow", "File:", None))
        self.printTimeLabel.setText(_translate("MainWindow", "Print Time:", None))
        self.fileName.setText(_translate("MainWindow", "fileName", None))
        self.printTime.setText(_translate("MainWindow", "printTime", None))
        self.timeLeftLabel.setText(_translate("MainWindow", "Time Left:", None))
        self.tool0TargetTemperature.setText(_translate("MainWindow", "0", None))
        self.tool0TempBar.setFormat(_translate("MainWindow", "%v", None))
        self.tool0ActualTemperature.setText(_translate("MainWindow", "0", None))
        self.printProgressBar.setFormat(_translate("MainWindow", "%p%", None))
        self.timeLeft.setText(_translate("MainWindow", "timeLeft", None))
        self.printerStatus.setText(_translate("MainWindow", "Status", None))
        self.celciusLabel.setText(_translate("MainWindow", "°C", None))
        self.celciusLabel_2.setText(_translate("MainWindow", "°C", None))
        self.bedTempBar.setFormat(_translate("MainWindow", "%v", None))
        self.bedActualTemperatute.setText(_translate("MainWindow", "0", None))
        self.bedTargetTemperature.setText(_translate("MainWindow", "0", None))
        self.menuControlButton.setText(_translate("MainWindow", "Control", None))
        self.menuPrintButton.setText(_translate("MainWindow", "Print", None))
        self.menuSettingsButton.setText(_translate("MainWindow", "Settings", None))
        self.menuCartButton.setText(_translate("MainWindow", "Cart", None))
        self.menuCaliberateButton.setText(_translate("MainWindow", "Calibrate", None))
        self.networkInfoButton.setText(_translate("MainWindow", "Network info", None))
        self.configureWifiButton.setText(_translate("MainWindow", "Configure WiFi", None))
        self.pairPhoneButton.setText(_translate("MainWindow", "Open in Smartphone", None))
        self.OTAButton.setText(_translate("MainWindow", "Check for Updates", None))
        self.caliberateTouch.setText(_translate("MainWindow", "Caliberate Touch", None))
        self.versionButton.setText(_translate("MainWindow", "Version", None))
        self.restorePrintSettingsButton.setText(_translate("MainWindow", "Restore Print Settings", None))
        self.restoreFactoryDefaultsButton.setText(_translate("MainWindow", "Restore Factory Defaults", None))
        self.restartButton.setText(_translate("MainWindow", "Restart", None))
        self.ssidlabel.setText(_translate("MainWindow", "Enter SSID:", None))
        self.passwordlabel.setText(_translate("MainWindow", "Enter Password:", None))
        self.wifiSettingsDoneButton.setText(_translate("MainWindow", "Done", None))
        self.wifiSettingsCancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.wifiSettingsSSIDKeyboardButton.setText(_translate("MainWindow", "...", None))
        self.hiddenCheckBox.setText(_translate("MainWindow", "Hidden ", None))
        self.hostnameLabel.setText(_translate("MainWindow", "URL: ", None))
        self.hostname.setText(_translate("MainWindow", "Hostname", None))
        self.wifiIpLabel.setText(_translate("MainWindow", "Wi-Fi IP address: ", None))
        self.wifiIp.setText(_translate("MainWindow", "Hostname: ", None))
        self.lanIpLabel.setText(_translate("MainWindow", "LAN IP address: ", None))
        self.lanIp.setText(_translate("MainWindow", "Hostname: ", None))
        self.performUpdateButton.setText(_translate("MainWindow", "Update", None))
        self.logTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gotham\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Software Update Starting, Please Wait....</p></body></html>", None))
        self.caliberateLabel.setText(_translate("MainWindow", "Caliberate:", None))
        self.nozzleOffsetButton.setText(_translate("MainWindow", "Height", None))
        self.caliberationWizardButton.setText(_translate("MainWindow", "Wizard", None))
        self.caliberateLabel_6.setText(_translate("MainWindow", "We start by caliberating the print bed\'s level. A perfectly leveled bed is essential to get reliable printing performance. Wait for all moves to finish and click Next", None))
        self.step1NextButton.setText(_translate("MainWindow", "Next", None))
        self.step1CancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.caliberateLabel_7.setText(_translate("MainWindow", "Release All Leveling Screws", None))
        self.step2NextButton.setText(_translate("MainWindow", "Next", None))
        self.step2CancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.step3CancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.step3NextButton.setText(_translate("MainWindow", "Next", None))
        self.caliberateLabel_10.setText(_translate("MainWindow", "After Nozzle is finished pressing down on bed, tighten right leveling screw", None))
        self.step4CancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.step4NextButton.setText(_translate("MainWindow", "Next", None))
        self.caliberateLabel_12.setText(_translate("MainWindow", "Do the same for the left screw", None))
        self.caliberateLabel_25.setText(_translate("MainWindow", "Now tighten the center back  screw", None))
        self.step5NextButton.setText(_translate("MainWindow", "Next", None))
        self.step5CancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.step6NextButton.setText(_translate("MainWindow", "Next", None))
        self.caliberateNozzleHeightLabel_2.setText(_translate("MainWindow", "We shall now set the height of the nozzle from the bed. Wait for the movements to finish, and then click Next.", None))
        self.step6CancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.step7NextButton.setText(_translate("MainWindow", "Next", None))
        self.caliberateLabel_89.setText(_translate("MainWindow", "Use a sheet of paper, and slide it under the nozzle while moving the bed upwards, untill the paper is just unable to slide. Click Next to start this process", None))
        self.step7CancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.step8CancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.step8DoneButton.setText(_translate("MainWindow", "Done", None))
        self.caliberateLabel_90.setText(_translate("MainWindow", "Move the bed towards the Nozzle untill the paper stops sliding", None))
        self.nozzleOffsetDoubleSpinBox.setSuffix(_translate("MainWindow", "mm", None))
        self.feedRateLabelControlPage_3.setText(_translate("MainWindow", "Change the initial height for the first layer of the print. +ve value increases height, -ve value reduces it.", None))
        self.fromUsbButton.setText(_translate("MainWindow", "USB", None))
        self.printFromLabel.setText(_translate("MainWindow", "Print From :", None))
        self.fromLocalButton.setText(_translate("MainWindow", "Local ", None))
        self.fileSelected.setText(_translate("MainWindow", "You Selected: ", None))
        self.fileSelectedPrintButton.setText(_translate("MainWindow", "Print", None))
        self.fileSizeSelected.setText(_translate("MainWindow", "Size", None))
        self.fileDateSelected.setText(_translate("MainWindow", "Date", None))
        self.filePrintTimeSelected.setText(_translate("MainWindow", "EST", None))
        self.filamentVolumeSelected.setText(_translate("MainWindow", "Fil. Volume", None))
        self.fileSizeSelectedLabel.setText(_translate("MainWindow", "Size:", None))
        self.fileDateSelectedLabel.setText(_translate("MainWindow", "Date:", None))
        self.filePrintTimeSelectedLabel.setText(_translate("MainWindow", "Estimated Print Time:", None))
        self.filamentVolumeSelectedLabel.setText(_translate("MainWindow", "Volume:", None))
        self.filamentLengthFileSelected.setText(_translate("MainWindow", "Fil. Length", None))
        self.filamentLengthSelectedLabel.setText(_translate("MainWindow", "Length:", None))
        self.fileSelectedUSBTransferButton.setText(_translate("MainWindow", "Save to Local", None))
        self.fileSelectedUSBName.setText(_translate("MainWindow", "File Name", None))
        self.fileSelectedUSBPrintButton.setText(_translate("MainWindow", "Print", None))
        self.flowRateLabelControlPage_2.setText(_translate("MainWindow", "Feed Rate :", None))
        self.feedRateSpinBox.setSuffix(_translate("MainWindow", "%", None))
        self.toolLabel.setText(_translate("MainWindow", "Nozzle:", None))
        self.toolTempSpinBox.setSuffix(_translate("MainWindow", "°C", None))
        self.bedTempSpinBox.setSuffix(_translate("MainWindow", "°C", None))
        self.bedLabel_2.setText(_translate("MainWindow", "Bed:", None))
        self.step1Button.setText(_translate("MainWindow", "1 mm", None))
        self.step10Button.setText(_translate("MainWindow", "10 mm", None))
        self.step100Button.setText(_translate("MainWindow", "100 mm", None))
        self.XYLabel.setText(_translate("MainWindow", "X/Y :", None))
        self.ZLabel.setText(_translate("MainWindow", "Z:", None))
        self.ELabel.setText(_translate("MainWindow", "E:", None))
        self.moveByLabel.setText(_translate("MainWindow", "Move By:", None))
        self.changeFilamentButton.setText(_translate("MainWindow", "Change Filament", None))
        self.flowRateSpinBox.setSuffix(_translate("MainWindow", "%", None))
        self.flowRateLabelControlPage.setText(_translate("MainWindow", "Flow Rate :", None))
        self.selectFilamentlabel.setText(_translate("MainWindow", "Select Filament :", None))
        self.changeFilamentLoadButton.setText(_translate("MainWindow", "Load", None))
        self.changeFilamentUnloadButton.setText(_translate("MainWindow", "Unload", None))
        self.changeFilamentStatus.setText(_translate("MainWindow", "Heating ...", None))
        self.changeFilamentProgress.setFormat(_translate("MainWindow", "%p%", None))
        self.changeFilamentNameOperation.setText(_translate("MainWindow", "Loading Filament", None))
        self.feedFilamentlabel.setText(_translate("MainWindow", "Feed Filament into Extruder", None))
        self.loadDoneButton.setText(_translate("MainWindow", "Done", None))
        self.ExtrudeButton.setText(_translate("MainWindow", "Extrude", None))
        self.feedFilamentlabel_2.setText(_translate("MainWindow", "Click \"Extrude\" untill filament starts extruding", None))
        self.feedFilamentlabel_3.setText(_translate("MainWindow", "Click \"Retract\" untill filament is removed", None))
        self.unloadDoneButton.setText(_translate("MainWindow", "Done", None))
        self.feedFilamentlabel_4.setText(_translate("MainWindow", "Retract Filament From Extruder", None))
        self.retractFilamentButton.setText(_translate("MainWindow", "Retract", None))

