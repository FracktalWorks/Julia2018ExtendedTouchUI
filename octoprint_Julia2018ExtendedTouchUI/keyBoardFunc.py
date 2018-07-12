from PyQt4 import QtCore, QtGui
import keyBoard
from functools import partial

class Keyboard(QtGui.QDialog, keyBoard.Ui_Form):
    '''
    Class that sets up the Keyboard UI and functionality
    '''

    def __init__(self, parent=None, onlyNumeric = False, noSpace = False, text = ""):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setActions()
        # self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setText(text)
        self.setTextFocus()

        self.ButtonBackNumeric.setEnabled(not onlyNumeric)
        self.ButtonSpecialNumeric.setEnabled(not onlyNumeric)

        self.ButtonSpaceAlpha.setEnabled(not noSpace)
        self.ButtonSpaceAlphaU.setEnabled(not noSpace)
        self.ButtonSpaceNumeric.setEnabled(not noSpace)
        self.ButtonSpaceSpecial.setEnabled(not noSpace)

        if not onlyNumeric:
            self.ShowAlpha()
        else:
            self.ShowNumeric()

    def setActions(self):
        # self.pushButton.clicked.connect(partial(self.add, self.pushButton.text()))
        # self.pushButton_2.clicked.connect(partial(self.window1.stopAction(), self.lineEdit.text()))
        
        # Space
        self.ButtonSpaceAlpha.clicked.connect(self.Space)
        self.ButtonSpaceAlphaU.clicked.connect(self.Space)
        self.ButtonSpaceNumeric.clicked.connect(self.Space)
        self.ButtonSpaceSpecial.clicked.connect(self.Space)
        
        # Backspace
        self.ButtonBackspaceAlpha.clicked.connect(self.Backspace)
        self.ButtonBackspaceAlphaU.clicked.connect(self.Backspace)
        self.ButtonBackspaceNumeric.clicked.connect(self.Backspace)
        self.ButtonBackspaceSpecial.clicked.connect(self.Backspace)

        # Char casess
        self.ButtonLowercase.clicked.connect(self.ShowAlpha)
        self.ButtonUppercase.clicked.connect(self.ShowAlphaU)

        # Submit
        self.ButtonSubmitAlpha.clicked.connect(self.submit)
        self.ButtonSubmitAlphaU.clicked.connect(self.submit)
        self.ButtonSubmitNumeric.clicked.connect(self.submit)
        self.ButtonSubmitSpecial.clicked.connect(self.submit)

        # Show Numeric
        self.ButtonNumericAlpha.clicked.connect(self.ShowNumeric)
        self.ButtonNumericAlphaU.clicked.connect(self.ShowNumeric)
        self.ButtonNumericSpecial.clicked.connect(self.ShowNumeric)

        # ShowSpecial
        self.ButtonSpecialAlpha.clicked.connect(self.ShowSpecial)
        self.ButtonSpecialAlphaU.clicked.connect(self.ShowSpecial)
        self.ButtonSpecialNumeric.clicked.connect(self.ShowSpecial)

        # Back
        self.ButtonBackNumeric.clicked.connect(self.ShowHome)
        self.ButtonBackSpecial.clicked.connect(self.ShowHome)

        # Cursor
        self.ButtonCursorLeft.clicked.connect(self.CaretLeft)
        self.ButtonCursorRight.clicked.connect(self.CaretRight)

        # for i in range(5):s
        # list = [self.pushButton, self.pushButton_1, self.pushButton_4]
        for i in range(1, 95):
            self.connectClick(str(i))

        # repeated elements
        rep = ["27_2", "56_2", "69_2", "74_2", "79_2", "27_3", "56_3"]
        for i in rep:
            self.connectClick(i)

    def connectClick(self, s):
        temp = "Button" + s
        button = getattr(self, temp)
        button.clicked.connect(partial(self.add, button.text()))

    def ShowAlpha(self):
        self.stackedWidget.setCurrentWidget(self.pageAlpha)
        self.setTextFocus()

    def ShowAlphaU(self):
        self.stackedWidget.setCurrentWidget(self.pageAlphaU)
        self.setTextFocus()

    def ShowHome(self):
        self.stackedWidget.setCurrentWidget(self.pageAlpha)
        self.setTextFocus()

    def ShowNumeric(self):
        self.stackedWidget.setCurrentWidget(self.pageNumeric)
        self.setTextFocus()

    def ShowSpecial(self):
        self.stackedWidget.setCurrentWidget(self.pageSpecial)
        self.setTextFocus()


    def Space(self):
        # self.textEdit.setText(self.textEdit.toPlainText() + " ")
        self.addText(" ")
        self.textEdit.setFocus()

    def Backspace(self):
        cursor = self.textEdit.textCursor()
        pos = cursor.position() - 1
        st = self.textEdit.toPlainText()
        # self.textEdit.setText(st[:-1])
        if pos >= 0:
            st = st[:pos] + st[(pos+1):]
            self.textEdit.setText(st)
            cursor.setPosition(pos)
            self.textEdit.setTextCursor(cursor)
        self.textEdit.setFocus()

    def add(self, arg):
        # self.textEdit.setText(self.textEdit.toPlainText() + arg)
        self.addText(arg)
        self.textEdit.setFocus()

    def CaretLeft(self):
        self.textEdit.moveCursor(QtGui.QTextCursor.Left, QtGui.QTextCursor.MoveAnchor)
        self.textEdit.setFocus()

    def CaretRight(self):
        self.textEdit.moveCursor(QtGui.QTextCursor.Right, QtGui.QTextCursor.MoveAnchor)
        self.textEdit.setFocus()

    def CaretStart(self):
        self.textEdit.moveCursor(QtGui.QTextCursor.Start, QtGui.QTextCursor.MoveAnchor)
        self.textEdit.setFocus()

    def CaretEnd(self):
        self.setTextFocus()

    def setTextFocus(self):
        self.textEdit.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
        self.textEdit.setFocus()

    def addText(self, txt):
        cursor = self.textEdit.textCursor()
        cursor.insertText(txt)
        self.textEdit.setFocus()

    # Submit
    def submit(self):
        self.close()
        self.emit(QtCore.SIGNAL('KEYBOARD'), self.textEdit.toPlainText())
        self.textEdit.setText("")