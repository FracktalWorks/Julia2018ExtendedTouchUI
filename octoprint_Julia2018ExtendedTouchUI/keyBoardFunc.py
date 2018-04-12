from PyQt4 import QtCore, QtGui
import keyBoard
from functools import partial

class Keyboard(QtGui.QDialog, keyBoard.Ui_Form):
    '''
    Class that sets up the Keyboard UI and functionality
    '''

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setActions()
        self.textEdit.setText("")

    def setActions(self):
        # self.pushButton.clicked.connect(partial(self.add, self.pushButton.text()))
        # self.pushButton_2.clicked.connect(partial(self.window1.stopAction(), self.lineEdit.text()))
        self.ButtonEnter.clicked.connect(self.enterKeyBoardValue)
        self.ButtonEnter2.clicked.connect(self.enterKeyBoardValue)
        self.ButtonEnter3.clicked.connect(self.KeyBoardHome)
        self.ButtonNumeric.clicked.connect(self.Numeric)
        self.ButtonNumeric2.clicked.connect(self.Numeric)
        self.ButtonLowerCase.clicked.connect(self.LowerCase)
        self.ButtonUpperCase.clicked.connect(self.UpperCase)
        self.ButtonSpace.clicked.connect(self.enterSpace)
        self.ButtonSpace2.clicked.connect(self.enterSpace)
        self.ButtonBackSpace.clicked.connect(self.backSpace)
        self.ButtonBackSpace2.clicked.connect(self.backSpace)
        # for i in range(5):
        # list = [self.pushButton, self.pushButton_1, self.pushButton_4]
        for i in range(1, 95):
            temp = "Button" + str(i)
            button = getattr(self, temp)
            button.clicked.connect(partial(self.add, button.text()))
            # button.clicked.connect(lambda: self.add(text))

    def LowerCase(self):
        self.stackedWidget.setCurrentWidget(self.page_2)

    def UpperCase(self):
        self.stackedWidget.setCurrentWidget(self.page)

    def KeyBoardHome(self):
        self.stackedWidget.setCurrentWidget(self.page)

    def Numeric(self):
        self.stackedWidget.setCurrentWidget(self.page_11)

    def enterKeyBoardValue(self):
        self.close()
        self.emit(QtCore.SIGNAL('KEYBOARD'),self.textEdit.toPlainText())
        self.textEdit.setText("")

    def enterSpace(self):
        self.textEdit.setText(self.textEdit.toPlainText() + " ")

    def backSpace(self):
        st = self.textEdit.toPlainText()
        self.textEdit.setText(st[:-1])

    def add(self, arg):
        self.textEdit.setText(self.textEdit.toPlainText() + arg)

