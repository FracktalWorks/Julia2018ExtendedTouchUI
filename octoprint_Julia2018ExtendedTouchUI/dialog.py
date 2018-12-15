from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


def font(size=14, weight=50, bold=False, underline=False, strikeout=False):
    font = QtGui.QFont()
    # QtGui.QInputMethodEvent
    font.setFamily(_fromUtf8("Gotham"))
    font.setPointSize(size)
    font.setWeight(weight)
    font.setBold(bold)
    font.setUnderline(underline)
    font.setStrikeOut(strikeout)
    return font


msgbox = _fromUtf8("""
QPushButton {
  border: 1px solid rgb(87, 87, 87);
  background-color: qlineargradient(spread: pad, x1: 0, y1: 1, x2: 0, y2: 0.188, stop: 0 rgba(180, 180, 180, 255), stop: 1 rgba(255, 255, 255, 255));
  height: 50px;
  width: 100px;
  border-radius: 5px;
  font: 14pt "Gotham";
}

QPushButton: pressed {
  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,	stop: 0 #dadbde, stop: 1 #f6f7fa);
}

QPushButton: focus {
  outline: none;
}

QLabel {
    margin-top: 20px;
    margin-bottom: 20px;
}
""")

msgbox_icon = _fromUtf8("""
    margin-top: 15px;
    margin-bottom: 5px;
    margin-left: 10px;
""")

msgbox_label = _fromUtf8("""
    margin-top: 5px;
    margin-bottom: 5px;
    margin-right: 10px;
""")


class Overlay(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        palette = QtGui.QPalette(self.palette())
        palette.setColor(palette.Background, QtCore.Qt.transparent)
        self.setPalette(palette)

        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        geom = QtGui.QApplication.desktop().screenGeometry(screen)
        self.setGeometry(geom)

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setOpacity(0.8)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.fillRect(event.rect(), QtGui.QBrush(QtGui.QColor(0, 0, 0, 127)))
        painter.end()


class SelfCenteringMessageBox(QtGui.QMessageBox):
    def __init__(self, timeout=3, parent=None, overlay=False):
        self._showOverlay = overlay
        self.overlay = Overlay(None)

        super(SelfCenteringMessageBox, self).__init__(None)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        objIcon = self.findChild(QtGui.QLabel, 'qt_msgboxex_icon_label')
        if objIcon:
            objIcon.setStyleSheet(msgbox_icon)
            # objIcon.setMinimumSize(60, 60)
            # objIcon.setGeometry(QtCore.QRect(0, 0, 60, 60))
            # height = objIcon.height()

        objLabel = self.findChild(QtGui.QLabel, 'qt_msgbox_label')
        if objLabel:
            objLabel.setStyleSheet(msgbox_label)
            objLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            objLabel.setMinimumSize(250, 80)

    def show(self):
        if self._showOverlay:
            self.overlay.show()
        super(SelfCenteringMessageBox, self).show()

        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def hide(self):
        super(SelfCenteringMessageBox, self).hide()
        self.overlay.hide()

    def showOverlay(self, overlay):
        self._showOverlay = overlay


def dialog(parent, text, **kwargs):
    fontSize = kwargs.get('fontSize', 14)
    icon = kwargs.get('icon', None)
    buttons = kwargs.get('buttons', QtGui.QMessageBox.Ok)
    geometry = kwargs.get('geometry', None)
    overlay = kwargs.get('overlay', False)

    choice = SelfCenteringMessageBox(parent)  # QtGui.QMessageBox()
    choice.setFont(font(fontSize))
    choice.setText(text)
    choice.setStandardButtons(buttons)
    choice.showOverlay(overlay)

    if icon:
        choice.setIconPixmap(QtGui.QPixmap(_fromUtf8("templates/img/" + icon)).scaled(40, 40))
        # choice.setIcon(QtGui.QMessageBox.Information)

    if geometry:
        choice.setGeometry(geometry)

    choice.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    choice.setStyleSheet(msgbox)
    choice.show()
    return choice


def Ok(parent, text, **kwargs):
    return dialog(parent, text, **kwargs).exec_() == QtGui.QMessageBox.Ok


def Cancel(parent, text, **kwargs):
    return dialog(parent, text, buttons=QtGui.QMessageBox.Cancel, **kwargs).exec_() == QtGui.QMessageBox.Cancel


def Yes(parent, text, **kwargs):
    return dialog(parent, text, buttons=QtGui.QMessageBox.Yes, **kwargs).exec_() == QtGui.QMessageBox.Yes


def YesNo(parent, text, **kwargs):
    return dialog(parent, text, buttons=QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, **kwargs).exec_() == QtGui.QMessageBox.Yes


def WarningOk(parent, text, **kwargs):
    return Ok(parent, text, icon="exclamation-mark.png", **kwargs)


def WarningCancel(parent, text, **kwargs):
    return Cancel(parent, text, icon="exclamation-mark.png", **kwargs)


def WarningYes(parent, text, **kwargs):
    return Yes(parent, text, icon="exclamation-mark.png", **kwargs)


def WarningYesNo(parent, text, **kwargs):
    return YesNo(parent, text, icon="exclamation-mark.png", **kwargs)


def SuccessOk(parent, text, **kwargs):
    return Ok(parent, text, icon="success.png", **kwargs)


def SuccessYesNo(parent, text, **kwargs):
    return YesNo(parent, text, icon="success.png", **kwargs)
