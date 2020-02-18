#!/usr/bin/python

'''
*************************************************************************
 *
 * Fracktal Works
 * __________________
 * Authors: Vijay Varada
 * Created: Nov 2016
 *
 * Licence: AGPLv3
*************************************************************************
'''
import mainGUI_extended 
import keyboard
import dialog
import styles
import asset_bundle

from PyQt4 import QtCore, QtGui
import time
import sys
import subprocess
from octoprintAPI import octoprintAPI
from hurry.filesize import size
from datetime import datetime
# from functools import partial
import qrcode
# pip install websocket-client
import websocket
import json
import random
import uuid
import os
# import serial
import io
import requests
import re
import logging

import RPi.GPIO as GPIO

    #Update
    #Update
from collections import OrderedDict


GPIO.setmode(GPIO.BCM)  # Use the board numbering scheme
GPIO.setwarnings(False)  # Disable GPIO warnings

# TODO:
'''
# Remove SD card capability from octoprint settings
# Should add error/status checking in the response in some functions in the octoprintAPI
# session keys??
# printer status should show errors from printer.
# async requests
# http://eli.thegreenplace.net/2011/04/25/passing-extra-arguments-to-pyqt-slot
# fix wifi
# status bar netweorking and wifi stuff
# reconnect to printer using GUI
# check if disk is getting full
# recheck for internet being conneted, refresh button
# load filaments from a file
# store settings to a file
# change the way active extruder print stores the current active extruder using positionEvent
#settings should show the current wifi
#clean up keyboard nameing
#add asertions and exeptions
#disaable done button if empty
#oncancel change filament cooldown
#toggle temperature indipendant of motion
#get active extruder from motion controller. when pausing, note down and resume with active extruder
#QR code has dictionary with IP address also
Testing:
# handle nothing selected in file select menus when deleting and printing etc.
# Delete items from local and USB
# different file list pages for local and USB
# test USB/Local properly
# check for uploading error when uploading from USB
# Test if active extruder goes back after pausing
# TRy to fuck with printing process from GUI
# PNG Handaling
# dissable buttons while printing
'''

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++Global variables++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

ip = '0.0.0.0:5000'
apiKey = 'B508534ED20348F090B4D0AD637D3660'

file_name = ''
Development = True
    #Update


filaments = [
                ("PLA", 200),
                ("ABS", 220),
                ("PETG", 230),
                ("PVA", 220),
                ("TPU", 230),
                ("Nylon", 250),
                ("PolyCarbonate", 275),
                ("HIPS", 220),
                ("WoodFill", 200),
                ("CopperFill", 180),
                ("Breakaway", 230)
]

filaments = OrderedDict(filaments)

calibrationPosition = {'X1': 193, 'Y1': 31,
                       'X2': 48, 'Y2': 31,
                       'X3': 120, 'Y3': 249
                       }

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


def run_async(func):
    '''
    Function decorater to make methods run in a thread
    '''
    from threading import Thread
    from functools import wraps

    @wraps(func)
    def async_func(*args, **kwargs):
        func_hl = Thread(target=func, args=args, kwargs=kwargs)
        func_hl.start()
        return func_hl

    return async_func


def getIP(interface):
    try:
        scan_result = \
            subprocess.Popen("ifconfig | grep " + interface + " -A 1", stdout=subprocess.PIPE, shell=True).communicate()[0]
        # Processing STDOUT into a dictionary that later will be converted to a json file later
        rInetAddr = r"inet addr:\s*([\d.]+)"
        mtIp = re.search(rInetAddr, scan_result)
        if mtIp and len(mtIp.groups()) == 1:
            return str(mtIp.group(1))
    except:
        return None


def getMac(interface):
    try:
        mac = subprocess.Popen(" cat /sys/class/net/" + interface + "/address", 
                               stdout=subprocess.PIPE, shell=True).communicate()[0].rstrip()
        if not mac:
            return "Not found"
        return mac.upper()
    except:
        return "Error"


def getWifiAp():
    try:
        ap = subprocess.Popen("iwgetid -r", 
                              stdout=subprocess.PIPE, shell=True).communicate()[0].rstrip()
        if not ap:
            return "Not connected"
        return ap
    except:
        return "Error"


def getHostname():
    try:
        hostname = subprocess.Popen("cat /etc/hostname", stdout=subprocess.PIPE, shell=True).communicate()[0].rstrip()
        if not hostname:
            return "Not connected"
        return hostname + ".local"
    except:
        return "Error"


class BuzzerFeedback(object):
    def __init__(self, buzzerPin):
        GPIO.cleanup()
        self.buzzerPin = buzzerPin
        GPIO.setup(self.buzzerPin, GPIO.OUT)
        GPIO.output(self.buzzerPin, GPIO.LOW)

    @run_async
    def buzz(self):
        GPIO.output(self.buzzerPin, (GPIO.HIGH))
        time.sleep(0.005)
        GPIO.output(self.buzzerPin, GPIO.LOW)


buzzer = BuzzerFeedback(12)

'''
To get the buzzer to beep on button press
'''

OriginalPushButton = QtGui.QPushButton
OriginalToolButton = QtGui.QToolButton


class QPushButtonFeedback(QtGui.QPushButton):
    def mousePressEvent(self, QMouseEvent):
        buzzer.buzz()
        OriginalPushButton.mousePressEvent(self, QMouseEvent)


class QToolButtonFeedback(QtGui.QToolButton):
    def mousePressEvent(self, QMouseEvent):
        buzzer.buzz()
        OriginalToolButton.mousePressEvent(self, QMouseEvent)


QtGui.QToolButton = QToolButtonFeedback
QtGui.QPushButton = QPushButtonFeedback


class Image(qrcode.image.base.BaseImage):
    def __init__(self, border, width, box_size):
        self.border = border
        self.width = width
        self.box_size = box_size
        size = (width + border * 2) * box_size
        self._image = QtGui.QImage(
            size, size, QtGui.QImage.Format_RGB16)
        self._image.fill(QtCore.Qt.white)

    def pixmap(self):
        return QtGui.QPixmap.fromImage(self._image)

    def drawrect(self, row, col):
        painter = QtGui.QPainter(self._image)
        painter.fillRect(
            (col + self.border) * self.box_size,
            (row + self.border) * self.box_size,
            self.box_size, self.box_size,
            QtCore.Qt.black)

    def save(self, stream, kind=None):
        pass


class ClickableLineEdit(QtGui.QLineEdit):
    def __init__(self, parent):
        QtGui.QLineEdit.__init__(self, parent)

    def mousePressEvent(self, QMouseEvent):
        buzzer.buzz()
        self.emit(QtCore.SIGNAL("clicked()"))


class MainUiClass(QtGui.QMainWindow, mainGUI_extended.Ui_MainWindow):
    '''
    Main GUI Workhorse, all slots and events defined within
    The main implementation class that inherits methods, variables etc from mainGUI_extended.py and QMainWindow
    '''

    def setupUi(self, MainWindow):
        super(MainUiClass, self).setupUi(MainWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gotham"))
        font.setPointSize(15)

        self.wifiPasswordLineEdit = ClickableLineEdit(self.wifiSettingsPage)
        self.wifiPasswordLineEdit.setGeometry(QtCore.QRect(0, 170, 480, 60))
        self.wifiPasswordLineEdit.setFont(font)
        self.wifiPasswordLineEdit.setStyleSheet(styles.textedit)
        self.wifiPasswordLineEdit.setObjectName(_fromUtf8("wifiPasswordLineEdit"))

        font.setPointSize(11)
        self.ethStaticIpLineEdit = ClickableLineEdit(self.ethStaticSettings)
        self.ethStaticIpLineEdit.setGeometry(QtCore.QRect(120, 10, 300, 30))
        self.ethStaticIpLineEdit.setFont(font)
        self.ethStaticIpLineEdit.setStyleSheet(styles.textedit)
        self.ethStaticIpLineEdit.setObjectName(_fromUtf8("ethStaticIpLineEdit"))

        self.ethStaticGatewayLineEdit = ClickableLineEdit(self.ethStaticSettings)
        self.ethStaticGatewayLineEdit.setGeometry(QtCore.QRect(120, 60, 300, 30))
        self.ethStaticGatewayLineEdit.setFont(font)
        self.ethStaticGatewayLineEdit.setStyleSheet(styles.textedit)
        self.ethStaticGatewayLineEdit.setObjectName(_fromUtf8("ethStaticGatewayLineEdit"))

        self.menuCartButton.setDisabled(True)

        self.movie = QtGui.QMovie("templates/img/loading.gif")
        self.loadingGif.setMovie(self.movie)
        self.movie.start()

    def __init__(self):
        '''
        This method gets called when an object of type MainUIClass is defined
        '''
        super(MainUiClass, self).__init__()
        formatter = logging.Formatter("%(asctime)s %(message)s")
        self._logger = logging.getLogger("TouchUI")
        file_handler = logging.FileHandler("/home/pi/ui.log")
        file_handler.setFormatter(formatter)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        # file_handler.setLevel(logging.DEBUG)
        self._logger.addHandler(file_handler)
        self._logger.addHandler(stream_handler)

        # Calls setupUi that sets up layout and geometry of all UI elements
        try:
            self.__packager = asset_bundle.AssetBundle()
            self.__packager.save_time()
            self.__timelapse_enabled = self.__packager.read_match() if self.__packager.time_delta() else True
            self.__timelapse_started = not self.__packager.time_delta()

            self._logger.info("Hardware ID = {}, Unlocked = {}".format(self.__packager.hc(), self.__timelapse_enabled))
            print("Hardware ID = {}, Unlocked = {}".format(self.__packager.hc(), self.__timelapse_enabled))
            self._logger.info("File time = {}, Demo = {}".format(self.__packager.read_time(), self.__timelapse_started))
            print("File time = {}, Demo = {}".format(self.__packager.read_time(), self.__timelapse_started))
            self.setupUi(self)
            self.stackedWidget.setCurrentWidget(self.loadingPage)
            self.setStep(10)
            self.keyboardWindow = None
            self.changeFilamentHeatingFlag = False
            self.setHomeOffsetBool = False
            self.currentImage = None
            self.currentFile = None
            self.sanityCheck = ThreadSanityCheck(self._logger, virtual=not self.__timelapse_enabled)
            self.sanityCheck.start()
            self.connect(self.sanityCheck, QtCore.SIGNAL('LOADED'), self.proceed)
            self.connect(self.sanityCheck, QtCore.SIGNAL('STARTUP_ERROR'), self.handleStartupError)

            for spinbox in self.findChildren(QtGui.QSpinBox):
                lineEdit = spinbox.lineEdit()
                lineEdit.setReadOnly(True)
                lineEdit.setDisabled(True)
                p = lineEdit.palette()
                p.setColor(QtGui.QPalette.Highlight, QtGui.QColor(40, 40, 40))
                lineEdit.setPalette(p)

        except Exception as e:
            self._logger.error(e.message)

        # Thread to get the get the state of the Printer as well as the temperature

    def proceed(self):
        '''
        Startes websocket, as well as initialises button actions and callbacks. THis is done in such a manner so that the callbacks that dnepend on websockets
        load only after the socket is available which in turn is dependent on the server being available which is checked in the sanity check thread
        '''
        self.QtSocket = QtWebsocket()
        self.QtSocket.start()
        self.setActions()
        self.movie.stop()
        self.stackedWidget.setCurrentWidget(self.pgLock)
        self.Lock_showLock()
        self.isFilamentSensorInstalled()
        self.setIPStatus()

    def setActions(self):

        '''
        defines all the Slots and Button events.
        '''
        self.connect(self.QtSocket, QtCore.SIGNAL('SET_Z_HOME_OFFSET'), self.setZHomeOffset)
        self.connect(self.QtSocket, QtCore.SIGNAL('Z_HOME_OFFSET'), self.getZHomeOffset)
        self.connect(self.QtSocket, QtCore.SIGNAL('TEMPERATURES'), self.updateTemperature)
        self.connect(self.QtSocket, QtCore.SIGNAL('STATUS'), self.updateStatus)
        self.connect(self.QtSocket, QtCore.SIGNAL('PRINT_STATUS'), self.updatePrintStatus)
        self.connect(self.QtSocket, QtCore.SIGNAL('UPDATE_STARTED'), self.softwareUpdateProgress)
        self.connect(self.QtSocket, QtCore.SIGNAL('UPDATE_LOG'), self.softwareUpdateProgressLog)
        self.connect(self.QtSocket, QtCore.SIGNAL('UPDATE_LOG_RESULT'), self.softwareUpdateResult)
        self.connect(self.QtSocket, QtCore.SIGNAL('UPDATE_FAILED'), self.updateFailed)
        self.connect(self.QtSocket, QtCore.SIGNAL('CONNECTED'), self.onServerConnected)
        self.connect(self.QtSocket, QtCore.SIGNAL('FILAMENT_SENSOR_TRIGGERED'), self.filamentSensorHandler)
        self.connect(self.QtSocket, QtCore.SIGNAL('FIRMWARE_UPDATER'), self.firmwareUpdateHandler)

        # Text Input events
        self.connect(self.wifiPasswordLineEdit, QtCore.SIGNAL("clicked()"),
                     lambda: self.startKeyboard(self.wifiPasswordLineEdit.setText))
        self.connect(self.ethStaticIpLineEdit, QtCore.SIGNAL("clicked()"),
                     lambda: self.ethShowKeyboard(self.ethStaticIpLineEdit))
        self.connect(self.ethStaticGatewayLineEdit, QtCore.SIGNAL("clicked()"),
                     lambda: self.ethShowKeyboard(self.ethStaticGatewayLineEdit))

        # Button Events:

        # Home Screen:
        self.stopButton.pressed.connect(self.stopActionMessageBox)
        # self.menuButton.pressed.connect(self.keyboardButton)
        self.menuButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.MenuPage))
        self.controlButton.pressed.connect(self.control)
        self.playPauseButton.clicked.connect(self.playPauseAction)

        # MenuScreen
        self.menuBackButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.homePage))
        self.menuControlButton.pressed.connect(self.control)
        self.menuPrintButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.printLocationPage))
        self.menuCalibrateButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.calibratePage))
        self.menuSettingsButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.settingsPage))

        # Calibrate Page
        self.calibrateBackButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.MenuPage))
        self.nozzleOffsetButton.pressed.connect(self.nozzleOffset)
        # the -ve sign is such that its converted to home offset and not just distance between nozzle and bed
        self.nozzleOffsetSetButton.pressed.connect(
            lambda: self.setZHomeOffset(self.nozzleOffsetDoubleSpinBox.value(), True))
        self.nozzleOffsetBackButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.calibratePage))

        self.calibrationWizardButton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.calibrationWizardPage))
        self.calibrationWizardBackButton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.calibratePage))
        self.quickCalibrationButton.clicked.connect(lambda: self.quickStep1(False))
        self.fullCalibrationButton.clicked.connect(lambda: self.quickStep1(True))
        self.quickStep1NextButton.clicked.connect(self.quickStep2)
        self.quickStep2NextButton.clicked.connect(self.quickStep3)
        self.quickStep3NextButton.clicked.connect(self.quickStep4)
        self.quickStep4NextButton.clicked.connect(self.quickStep5)
        self.quickStep5NextButton.clicked.connect(self.proceedToFull)
        self.fullStep1NextButton.clicked.connect(self.fullStep2)
        self.fullStep2NextButton.clicked.connect(self.fullStep2)
        # self.moveZPCalibrateButton.pressed.connect(lambda: octopiclient.jog(z=-0.05))
        # self.moveZPCalibrateButton.pressed.connect(lambda: octopiclient.jog(z=0.05))
        self.moveZMFullCalibrateButton.pressed.connect(lambda: octopiclient.jog(z=-0.025))
        self.moveZPFullCalibrateButton.pressed.connect(lambda: octopiclient.jog(z=0.025))
        self.quickStep1CancelButton.pressed.connect(self.cancelStep)
        self.quickStep2CancelButton.pressed.connect(self.cancelStep)
        self.quickStep3CancelButton.pressed.connect(self.cancelStep)
        self.quickStep4CancelButton.pressed.connect(self.cancelStep)
        self.quickStep5CancelButton.pressed.connect(self.cancelStep)
        self.fullStep1CancelButton.pressed.connect(self.cancelStep)
        self.fullStep2CancelButton.pressed.connect(self.cancelStep)

        # PrintLocationScreen
        self.printLocationScreenBackButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.MenuPage))
        self.fromLocalButton.pressed.connect(self.fileListLocal)
        self.fromUsbButton.pressed.connect(self.fileListUSB)

        # fileListLocalScreen
        self.localStorageBackButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.printLocationPage))
        self.localStorageScrollUp.pressed.connect(
            lambda: self.fileListWidget.setCurrentRow(self.fileListWidget.currentRow() - 1))
        self.localStorageScrollDown.pressed.connect(
            lambda: self.fileListWidget.setCurrentRow(self.fileListWidget.currentRow() + 1))
        self.localStorageSelectButton.pressed.connect(self.printSelectedLocal)
        self.localStorageDeleteButton.pressed.connect(self.deleteItem)

        # selectedFile Local Screen
        self.fileSelectedBackButton.pressed.connect(self.fileListLocal)
        self.fileSelectedPrintButton.pressed.connect(self.printFile)

        # filelistUSBPage
        self.USBStorageBackButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.printLocationPage))
        self.USBStorageScrollUp.pressed.connect(
            lambda: self.fileListWidgetUSB.setCurrentRow(self.fileListWidgetUSB.currentRow() - 1))
        self.USBStorageScrollDown.pressed.connect(
            lambda: self.fileListWidgetUSB.setCurrentRow(self.fileListWidgetUSB.currentRow() + 1))
        self.USBStorageSelectButton.pressed.connect(self.printSelectedUSB)
        self.USBStorageSaveButton.pressed.connect(lambda: self.transferToLocal(prnt=False))

        # selectedFile USB Screen
        self.fileSelectedUSBBackButton.pressed.connect(self.fileListUSB)
        self.fileSelectedUSBTransferButton.pressed.connect(lambda: self.transferToLocal(prnt=False))
        self.fileSelectedUSBPrintButton.pressed.connect(lambda: self.transferToLocal(prnt=True))

        # ControlScreen
        self.moveYPButton.pressed.connect(lambda: octopiclient.jog(y=self.step, speed=1000))
        self.moveYMButton.pressed.connect(lambda: octopiclient.jog(y=-self.step, speed=1000))
        self.moveXMButton.pressed.connect(lambda: octopiclient.jog(x=-self.step, speed=1000))
        self.moveXPButton.pressed.connect(lambda: octopiclient.jog(x=self.step, speed=1000))
        self.moveZPButton.pressed.connect(lambda: octopiclient.jog(z=self.step, speed=1000))
        self.moveZMButton.pressed.connect(lambda: octopiclient.jog(z=-self.step, speed=1000))
        self.extruderButton.pressed.connect(lambda: octopiclient.extrude(self.step))
        self.retractButton.pressed.connect(lambda: octopiclient.extrude(-self.step))
        self.motorOffButton.pressed.connect(lambda: octopiclient.gcode(command='M18'))
        self.fanOnButton.pressed.connect(lambda: octopiclient.gcode(command='M106'))
        self.fanOffButton.pressed.connect(lambda: octopiclient.gcode(command='M107'))
        self.cooldownButton.pressed.connect(self.coolDownAction)
        self.step100Button.pressed.connect(lambda: self.setStep(100))
        self.step1Button.pressed.connect(lambda: self.setStep(1))
        self.step10Button.pressed.connect(lambda: self.setStep(10))
        self.homeXYButton.pressed.connect(lambda: octopiclient.home(['x', 'y']))
        self.homeZButton.pressed.connect(lambda: octopiclient.home(['z']))
        self.controlBackButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.homePage))
        self.setToolTempButton.pressed.connect(lambda: octopiclient.setToolTemperature(
            self.toolTempSpinBox.value()))
        self.setBedTempButton.pressed.connect(lambda: octopiclient.setBedTemperature(self.bedTempSpinBox.value()))

        self.setFlowRateButton.pressed.connect(lambda: octopiclient.flowrate(self.flowRateSpinBox.value()))
        self.setFeedRateButton.pressed.connect(lambda: octopiclient.feedrate(self.feedRateSpinBox.value()))

        self.moveZPBabyStep.pressed.connect(lambda: octopiclient.gcode(command='M290 Z0.025'))
        self.moveZMBabyStep.pressed.connect(lambda: octopiclient.gcode(command='M290 Z-0.025'))


        # ChangeFilament rutien
        self.changeFilamentButton.pressed.connect(self.changeFilament)
        self.changeFilamentBackButton.pressed.connect(self.control)
        self.changeFilamentBackButton2.pressed.connect(self.changeFilamentCancel)
        self.changeFilamentUnloadButton.pressed.connect(lambda: self.unloadFilament())
        self.changeFilamentLoadButton.pressed.connect(lambda: self.loadFilament())
        self.loadDoneButton.pressed.connect(self.control)
        self.unloadDoneButton.pressed.connect(self.changeFilament)
        self.retractFilamentButton.pressed.connect(lambda: octopiclient.extrude(-20))
        self.ExtrudeButton.pressed.connect(lambda: octopiclient.extrude(20))

        # Settings Page
        self.networkSettingsButton.pressed.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.networkSettingsPage))
        self.displaySettingsButton.pressed.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.displaySettingsPage))
        self.settingsBackButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.MenuPage))
        self.pairPhoneButton.pressed.connect(self.pairPhoneApp)
        self.OTAButton.pressed.connect(self.softwareUpdate)
        self.versionButton.pressed.connect(self.displayVersionInfo)

        self.restartButton.pressed.connect(self.askAndReboot)
        self.restoreFactoryDefaultsButton.pressed.connect(self.restoreFactoryDefaults)
        self.restorePrintSettingsButton.pressed.connect(self.restorePrintDefaults)

        # Network settings page
        self.networkInfoButton.pressed.connect(self.networkInfo)
        self.configureWifiButton.pressed.connect(self.wifiSettings)
        self.configureEthButton.pressed.connect(self.ethSettings)
        self.networkSettingsBackButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.settingsPage))

        # Network Info Page
        self.networkInfoBackButton.pressed.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.networkSettingsPage))

        # WifiSetings page
        self.wifiSettingsSSIDKeyboardButton.pressed.connect(
            lambda: self.startKeyboard(self.wifiSettingsComboBox.addItem))
        self.wifiSettingsCancelButton.pressed.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.networkSettingsPage))
        self.wifiSettingsDoneButton.pressed.connect(self.acceptWifiSettings)

        # Ethernet setings page
        self.ethStaticCheckBox.stateChanged.connect(self.ethStaticChanged)
        # self.ethStaticCheckBox.stateChanged.connect(lambda: self.ethStaticSettings.setVisible(self.ethStaticCheckBox.isChecked()))
        self.ethStaticIpKeyboardButton.pressed.connect(lambda: self.ethShowKeyboard(self.ethStaticIpLineEdit))
        self.ethStaticGatewayKeyboardButton.pressed.connect(lambda: self.ethShowKeyboard(self.ethStaticGatewayLineEdit))
        self.ethSettingsDoneButton.pressed.connect(self.ethSaveStaticNetworkInfo)
        self.ethSettingsCancelButton.pressed.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.networkSettingsPage))

        # Display settings
        self.rotateDisplay.pressed.connect(self.showRotateDisplaySettingsPage)
        self.calibrateTouch.pressed.connect(self.touchCalibration)
        self.displaySettingsBackButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.settingsPage))

        # Rotate Display Settings
        self.rotateDisplaySettingsDoneButton.pressed.connect(self.saveRotateDisplaySettings)
        self.rotateDisplaySettingsCancelButton.pressed.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.displaySettingsPage))

        # QR Code
        self.QRCodeBackButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.settingsPage))

        # SoftwareUpdatePage
        self.softwareUpdateBackButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.settingsPage))
        self.performUpdateButton.pressed.connect(lambda: octopiclient.performSoftwareUpdate())

        # Firmware update page
        self.firmwareUpdateBackButton.pressed.connect(self.firmwareUpdateBack)

        # Filament sensor toggle
        self.toggleFilamentSensorButton.clicked.connect(self.toggleFilamentSensor)

        # Lock settings
        self.pgLock_pin.textChanged.connect(self.Lock_onPinInputChanged)

        self.pgLock_bt1.clicked.connect(lambda: self.Lock_kbAdd("1"))
        self.pgLock_bt2.clicked.connect(lambda: self.Lock_kbAdd("2"))
        self.pgLock_bt3.clicked.connect(lambda: self.Lock_kbAdd("3"))
        self.pgLock_bt4.clicked.connect(lambda: self.Lock_kbAdd("4"))
        self.pgLock_bt5.clicked.connect(lambda: self.Lock_kbAdd("5"))
        self.pgLock_bt6.clicked.connect(lambda: self.Lock_kbAdd("6"))
        self.pgLock_bt7.clicked.connect(lambda: self.Lock_kbAdd("7"))
        self.pgLock_bt8.clicked.connect(lambda: self.Lock_kbAdd("8"))
        self.pgLock_bt9.clicked.connect(lambda: self.Lock_kbAdd("9"))
        self.pgLock_bt0.clicked.connect(lambda: self.Lock_kbAdd("0"))
        self.pgLock_btBackspace.clicked.connect(lambda: self.pgLock_pin.backspace())
        self.pgLock_btSubmit.clicked.connect(self.Lock_submitPIN)

    ''' +++++++++++++++++++++++++Lock Settings+++++++++++++++++++++++++++++++++++ '''
    def Lock_showLock(self):
        self.pgLock_HID.setText(str(self.__packager.hc()))
        self.pgLock_pin.setText("")
        if not self.__timelapse_enabled:
            # dialog.WarningOk(self, "Machine locked!", overlay=True)
            self.stackedWidget.setCurrentWidget(self.pgLock)
        else:
            # if self.__timelapse_started:
            #     dialog.WarningOk(self, "Demo mode!", overlay=True)
            self.stackedWidget.setCurrentWidget(self.homePage)

    def Lock_kbAdd(self, txt):
        if len(str(self.pgLock_pin.text())) < 9:
            self.pgLock_pin.setText(str(self.pgLock_pin.text()) + txt)
        self.pgLock_pin.setFocus()

    def Lock_onPinInputChanged(self):
        self.pgLock_btBackspace.setEnabled(len(str(self.pgLock_pin.text())) > 0)
        self.pgLock_btSubmit.setEnabled(len(str(self.pgLock_pin.text())) > 3)

    def Lock_submitPIN(self):
        k = -1
        t = self.pgLock_pin.text()
        try:
            k = int(t)
            if self.__packager.match(k):
                self.__packager.save(k)
                # self.__timelapse_enabled = True
                if dialog.SuccessOk(self, "Machine unlocked!", overlay=True):
                    self.tellAndReboot()
                self.stackedWidget.setCurrentWidget(self.homePage)
            else:
                dialog.WarningOk(self, "Incorrect unlock code")
        except Exception as e:
            dialog.WarningOk(self, "Error while parsing unlock code")
            print(e.message)

    ''' +++++++++++++++++++++++++Print Restore+++++++++++++++++++++++++++++++++++ '''

    def printRestoreMessageBox(self, file):
        '''
        Displays a message box alerting the user of a filament error
        '''
        if dialog.WarningYesNo(self, file + " Did not finish, would you like to restore?"):
            response = octopiclient.restore(restore=True)
            if response["status"] == "Successfully Restored":
                dialog.WarningOk(response["status"])
            else:
                dialog.WarningOk(response["status"])
        else:
            octoprintAPI.restore(restore=False)

    def onServerConnected(self):
        self.isFilamentSensorInstalled()
        # if not self.__timelapse_enabled:
        #     return
        # if self.__timelapse_started:
        #     return
        try:
            response = octopiclient.isFailureDetected()
            if response["canRestore"] is True:
                self.printRestoreMessageBox(response["file"])
            else:
                self.firmwareUpdateCheck()
        except:
            pass

    ''' +++++++++++++++++++++++++Filament Sensor++++++++++++++++++++++++++++++++++++++ '''

    def isFilamentSensorInstalled(self):
        success = False
        try:
            headers = {'X-Api-Key': apiKey}
            req = requests.get('http://{}/plugin/Julia2018FilamentSensor/status'.format(ip), headers=headers)
            success = req.status_code == requests.codes.ok
        except:
            pass
        self.toggleFilamentSensorButton.setEnabled(success)
        return success

    def toggleFilamentSensor(self):
        headers = {'X-Api-Key': apiKey}
        # payload = {'sensor_enabled': self.toggleFilamentSensorButton.isChecked()}
        requests.get('http://{}/plugin/Julia2018FilamentSensor/toggle'.format(ip), headers=headers)   # , data=payload)

    def filamentSensorHandler(self, data):
        sensor_enabled = False
        # print(data)

        if 'sensor_enabled' in data:
            sensor_enabled = data["sensor_enabled"] == 1

        icon = 'filamentSensorOn' if sensor_enabled else 'filamentSensorOff'
        self.toggleFilamentSensorButton.setIcon(QtGui.QIcon(_fromUtf8("templates/img/" + icon)))

        if not sensor_enabled:
            return

        triggered_extruder0 = False
        triggered_door = False
        pause_print = False

        if 'filament' in data:
            triggered_extruder0 = data["filament"] == 0
        elif 'extruder0' in data:
            triggered_extruder0 = data["extruder0"] == 0

        if 'door' in data:
            triggered_door = data["door"] == 0
        if 'pause_print' in data:
            pause_print = data["pause_print"]

        #Update
        if triggered_extruder0 and self.stackedWidget.currentWidget() not in [self.changeFilamentPage, self.changeFilamentProgressPage,
                                  self.changeFilamentExtrudePage, self.changeFilamentRetractPage]:
            if dialog.WarningOk(self, "Filament outage in Extruder 0"):
                pass

        if triggered_door:
            if self.printerStatusText == "Printing":
                no_pause_pages = [self.controlPage, self.changeFilamentPage, self.changeFilamentProgressPage,
                                  self.changeFilamentExtrudePage, self.changeFilamentRetractPage]
                if not pause_print or self.stackedWidget.currentWidget() in no_pause_pages:
                    if dialog.WarningOk(self, "Door opened"):
                        return
                octopiclient.pausePrint()
                if dialog.WarningOk(self, "Door opened. Print paused.", overlay=True):
                    return
            else:
                if dialog.WarningOk(self, "Door opened"):
                    return

    ''' +++++++++++++++++++++++++++ Firmware Update+++++++++++++++++++++++++++++++++++ '''

    isFirmwareUpdateInProgress = False

    def firmwareUpdateCheck(self):
        headers = {'X-Api-Key': apiKey}
        requests.get('http://{}/plugin/JuliaFirmwareUpdater/update/check'.format(ip), headers=headers)

    def firmwareUpdateStart(self):
        headers = {'X-Api-Key': apiKey}
        requests.get('http://{}/plugin/JuliaFirmwareUpdater/update/start'.format(ip), headers=headers)

    def firmwareUpdateStartProgress(self):
        self.stackedWidget.setCurrentWidget(self.firmwareUpdateProgressPage)
        # self.firmwareUpdateLog.setTextColor(QtCore.Qt.yellow)
        self.firmwareUpdateLog.setText("<span style='color: cyan'>Julia Firmware Updater<span>")
        self.firmwareUpdateLog.append("<span style='color: cyan'>---------------------------------------------------------------</span>")
        self.firmwareUpdateBackButton.setEnabled(False)

    def firmwareUpdateProgress(self, text, backEnabled=False):
        self.stackedWidget.setCurrentWidget(self.firmwareUpdateProgressPage)
        # self.firmwareUpdateLog.setTextColor(QtCore.Qt.yellow)
        self.firmwareUpdateLog.append(str(text))
        self.firmwareUpdateBackButton.setEnabled(backEnabled)

    def firmwareUpdateBack(self):
        self.isFirmwareUpdateInProgress = False
        self.firmwareUpdateBackButton.setEnabled(False)
        self.stackedWidget.setCurrentWidget(self.homePage)

    def firmwareUpdateHandler(self, data):
        if "type" not in data or data["type"] != "status":
            return

        if "status" not in data:
            return

        status = data["status"]
        subtype = data["subtype"] if "subtype" in data else None

        if status == "update_check":    # update check
            if subtype == "error":  # notify error in ok diag
                self.isFirmwareUpdateInProgress = False
                if "message" in data:
                    dialog.WarningOk(self, "Firmware Updater Error: " + str(data["message"]), overlay=True)
            elif subtype == "success":
                if dialog.SuccessYesNo(self, "Firmware update found.\nPress yes to update now!", overlay=True):
                    self.isFirmwareUpdateInProgress = True
                    self.firmwareUpdateStart()
        elif status == "update_start":  # update started
            if subtype == "success":    # update progress
                self.isFirmwareUpdateInProgress = True
                self.firmwareUpdateStartProgress()
                if "message" in data:
                    message = "<span style='color: yellow'>{}</span>".format(data["message"])
                    self.firmwareUpdateProgress(message)
            else:   # show error
                self.isFirmwareUpdateInProgress = False
                # self.firmwareUpdateProgress(data["message"] if "message" in data else "Unknown error!", backEnabled=True)
                if "message" in data:
                    dialog.WarningOk(self, "Firmware Updater Error: " + str(data["message"]), overlay=True)
        elif status == "flasherror" or status == "progress":    # show software update dialog and update textview
            if "message" in data:
                message = "<span style='color: {}'>{}</span>".format("teal" if status == "progress" else "red", data["message"])
                self.firmwareUpdateProgress(message, backEnabled=(status == "flasherror"))
        elif status == "success":    # show ok diag to show done
            self.isFirmwareUpdateInProgress = False
            message = data["message"] if "message" in data else "Flash successful!"
            message = "<span style='color: green'>{}</span>".format(message)
            message = message + "<br/><br/><span style='color: white'>Press back to continue...</span>"
            self.firmwareUpdateProgress(message, backEnabled=True)

    ''' +++++++++++++++++++++++++++++++++OTA Update+++++++++++++++++++++++++++++++++++ '''

    def getFirmwareVersion(self):
        try:
            headers = {'X-Api-Key': apiKey}
            req = requests.get('http://{}/plugin/JuliaFirmwareUpdater/hardware/version'.format(ip), headers=headers)
            data = req.json()
            # print(data)
            if req.status_code == requests.codes.ok:
                info = u'\u2713' if not data["update_available"] else u"\u2717"    # icon
                info += " Firmware: "
                info += "Unknown" if not data["variant_name"] else data["variant_name"]
                info += "\n"
                if data["variant_name"]:
                    info += "   Installed: "
                    info += "Unknown" if not data["version_board"] else data["version_board"]
                info += "\n"
                info += "" if not data["version_repo"] else "   Available: " + data["version_repo"]
                return info
        except:
            print("Error accessing /plugin/JuliaFirmwareUpdater/hardware/version")
            pass
        return u'\u2713' + "Firmware: Unknown\n"

    def displayVersionInfo(self):
        self.updateListWidget.clear()
        updateAvailable = False
        self.performUpdateButton.setDisabled(True)

        self.updateListWidget.addItem(self.getFirmwareVersion())

        data = octopiclient.getSoftwareUpdateInfo()
        if data:
            for item in data["information"]:
                # print(item)
                plugin = data["information"][item]
                info = u'\u2713' if not plugin["updateAvailable"] else u"\u2717"    # icon
                info += plugin["displayName"] + "  " + plugin["displayVersion"] + "\n"
                info += "   Available: "
                if "information" in plugin and "remote" in plugin["information"] and plugin["information"]["remote"]["value"] is not None:
                    info += plugin["information"]["remote"]["value"]
                else:
                    info += "Unknown"
                self.updateListWidget.addItem(info)

                if plugin["updateAvailable"]:
                    updateAvailable = True

                # if not updatable:
                #     self.updateListWidget.addItem(u'\u2713' + data["information"][item]["displayName"] +
                #                                   "  " + data["information"][item]["displayVersion"] + "\n"
                #                                   + "   Available: " +
                #                                   )
                # else:
                #     updateAvailable = True
                #     self.updateListWidget.addItem(u"\u2717" + data["information"][item]["displayName"] +
                #                                   "  " + data["information"][item]["displayVersion"] + "\n"
                #                                   + "   Available: " +
                #                                   data["information"][item]["information"]["remote"]["value"])
        if updateAvailable:
            self.performUpdateButton.setDisabled(False)
        self.stackedWidget.setCurrentWidget(self.OTAUpdatePage)

    def softwareUpdateResult(self, data):
        messageText = ""
        for item in data:
            messageText += item + ": " + data[item][0] + ".\n"
        messageText += "Restart required"
        self.askAndReboot(messageText)

    def softwareUpdateProgress(self, data):
        self.stackedWidget.setCurrentWidget(self.softwareUpdateProgressPage)
        self.logTextEdit.setTextColor(QtCore.Qt.red)
        self.logTextEdit.append("---------------------------------------------------------------\n"
                                "Updating " + data["name"] + " to " + data["version"] + "\n"
                                                                                        "---------------------------------------------------------------")

    def softwareUpdateProgressLog(self, data):
        self.logTextEdit.setTextColor(QtCore.Qt.white)
        for line in data:
            self.logTextEdit.append(line["line"])

    def updateFailed(self, data):
        self.stackedWidget.setCurrentWidget(self.settingsPage)
        messageText = (data["name"] + " failed to update\n")
        if dialog.WarningOkCancel(self, messageText, overlay=True):
            pass

    def softwareUpdate(self):
        data = octopiclient.getSoftwareUpdateInfo()
        updateAvailable = False
        if data:
            for item in data["information"]:
                if data["information"][item]["updateAvailable"]:
                    updateAvailable = True
        if updateAvailable:
            print('Update Available')
            if dialog.SuccessYesNo(self, "Update Available! Update Now?", overlay=True):
                octopiclient.performSoftwareUpdate()

        else:
            if dialog.SuccessOk(self, "System is Up To Date!", overlay=True):
                print('Update Unavailable')

    ''' +++++++++++++++++++++++++++++++++Wifi Config+++++++++++++++++++++++++++++++++++ '''

    def acceptWifiSettings(self):
        wlan0_config_file = io.open("/etc/wpa_supplicant/wpa_supplicant.conf", "r+", encoding='utf8')
        wlan0_config_file.truncate()
        ascii_ssid = self.wifiSettingsComboBox.currentText()
        # unicode_ssid = ascii_ssid.decode('string_escape').decode('utf-8')
        wlan0_config_file.write(u"network={\n")
        wlan0_config_file.write(u'ssid="' + str(ascii_ssid) + '"\n')
        if self.hiddenCheckBox.isChecked():
            wlan0_config_file.write(u'scan_ssid=1\n')
        if str(self.wifiPasswordLineEdit.text()) != "":
            wlan0_config_file.write(u'psk="' + str(self.wifiPasswordLineEdit.text()) + '"\n')
        wlan0_config_file.write(u'}')
        wlan0_config_file.close()
        signal = 'WIFI_RECONNECT_RESULT'
        self.restartWifiThreadObject = ThreadRestartNetworking(ThreadRestartNetworking.WLAN, signal)
        self.restartWifiThreadObject.start()
        self.connect(self.restartWifiThreadObject, QtCore.SIGNAL(signal), self.wifiReconnectResult)
        self.wifiMessageBox = dialog.dialog(self,
                                            "Restarting networking, please wait...",
                                            icon="exclamation-mark.png",
                                            buttons=QtGui.QMessageBox.Cancel)
        if self.wifiMessageBox.exec_() in {QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel}:
            self.stackedWidget.setCurrentWidget(self.networkSettingsPage)

    def wifiReconnectResult(self, x):
        self.wifiMessageBox.setStandardButtons(QtGui.QMessageBox.Ok)
        if x is not None:
            self.wifiMessageBox.setLocalIcon('success.png')
            self.wifiMessageBox.setText('Connected, IP: ' + x)
            self.wifiMessageBox.setStandardButtons(QtGui.QMessageBox.Ok)
            self.ipStatus.setText(x) #sets the IP addr. in the status bar

        else:
            self.wifiMessageBox.setText("Not able to connect to WiFi")

    def networkInfo(self):
        ipWifi = getIP(ThreadRestartNetworking.WLAN)
        ipEth = getIP(ThreadRestartNetworking.ETH)

        self.hostname.setText(getHostname())
        self.wifiAp.setText(getWifiAp())
        self.wifiIp.setText("Not connected" if not ipWifi else ipWifi)
        self.ipStatus.setText("Not connected" if not ipWifi else ipWifi)
        self.lanIp.setText("Not connected" if not ipEth else ipEth)
        self.wifiMac.setText(getMac(ThreadRestartNetworking.WLAN))
        self.lanMac.setText(getMac(ThreadRestartNetworking.ETH))
        self.stackedWidget.setCurrentWidget(self.networkInfoPage)

    def wifiSettings(self):
        self.stackedWidget.setCurrentWidget(self.wifiSettingsPage)
        self.wifiSettingsComboBox.clear()
        self.wifiSettingsComboBox.addItems(self.scan_wifi())

    def scan_wifi(self):
        '''
        uses linux shell and WIFI interface to scan available networks
        :return: dictionary of the SSID and the signal strength
        '''
        # scanData = {}
        # print "Scanning available wireless signals available to wlan0"
        scan_result = \
            subprocess.Popen("iwlist wlan0 scan | grep 'ESSID'", stdout=subprocess.PIPE, shell=True).communicate()[0]
        # Processing STDOUT into a dictionary that later will be converted to a json file later
        scan_result = scan_result.split('ESSID:')  # each ssid and pass from an item in a list ([ssid pass,ssid paas])
        scan_result = [s.strip() for s in scan_result]
        scan_result = [s.strip('"') for s in scan_result]
        scan_result = filter(None, scan_result)
        return scan_result

    @run_async
    def setIPStatus(self):
        '''
        Function to update IP address of printer on the status bar. Refreshes at a particular interval.
        '''
        while(True):
            try:
                if getIP("eth0"):
                    self.ipStatus.setText(getIP("eth0"))
                elif getIP("wlan0"):
                    self.ipStatus.setText(getIP("wlan0"))
                else:
                    self.ipStatus.setText("Not connected")

            except:
                self.ipStatus.setText("Not connected")
            time.sleep(60)


    ''' +++++++++++++++++++++++++++++++++Ethernet Settings+++++++++++++++++++++++++++++ '''

    def ethSettings(self):
        self.stackedWidget.setCurrentWidget(self.ethSettingsPage)
        # self.ethStaticCheckBox.setChecked(True)
        self.ethNetworkInfo()

    def ethStaticChanged(self, state):
        self.ethStaticSettings.setVisible(self.ethStaticCheckBox.isChecked())
        self.ethStaticSettings.setEnabled(self.ethStaticCheckBox.isChecked())
        # if state == QtCore.Qt.Checked:
        #     self.ethStaticSettings.setVisible(True)
        # else:
        #     self.ethStaticSettings.setVisible(False)

    def ethNetworkInfo(self):
        txt = subprocess.Popen("cat /etc/dhcpcd.conf", stdout=subprocess.PIPE, shell=True).communicate()[0]

        reEthGlobal = r"interface\s+eth0\s?(static\s+[a-z0-9./_=\s]+\n)*"
        reEthAddress = r"static\s+ip_address=([\d.]+)(/[\d]{1,2})?"
        reEthGateway = r"static\s+routers=([\d.]+)(/[\d]{1,2})?"

        mtEthGlobal = re.search(reEthGlobal, txt)

        cbStaticEnabled = False
        txtEthAddress = ""
        txtEthGateway = ""

        if mtEthGlobal:
            sz = len(mtEthGlobal.groups())
            cbStaticEnabled = (sz == 1)

            if sz == 1:
                mtEthAddress = re.search(reEthAddress, mtEthGlobal.group(0))
                if mtEthAddress and len(mtEthAddress.groups()) == 2:
                    txtEthAddress = mtEthAddress.group(1)
                mtEthGateway = re.search(reEthGateway, mtEthGlobal.group(0))
                if mtEthGateway and len(mtEthGateway.groups()) == 2:
                    txtEthGateway = mtEthGateway.group(1)

        self.ethStaticCheckBox.setChecked(cbStaticEnabled)
        self.ethStaticSettings.setVisible(cbStaticEnabled)
        self.ethStaticIpLineEdit.setText(txtEthAddress)
        self.ethStaticGatewayLineEdit.setText(txtEthGateway)

    def isIpErr(self, ip):
        return (re.search(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$", ip) is None)

    def showIpErr(self, var):
        return dialog.WarningOk(self, "Invalid input: {0}".format(var))

    def ethSaveStaticNetworkInfo(self):
        cbStaticEnabled = self.ethStaticCheckBox.isChecked()
        txtEthAddress = str(self.ethStaticIpLineEdit.text())
        txtEthGateway = str(self.ethStaticGatewayLineEdit.text())

        if cbStaticEnabled:
            if self.isIpErr(txtEthAddress):
                return self.showIpErr("IP Address")
            if self.isIpErr(txtEthGateway):
                return self.showIpErr("Gateway")

        txt = subprocess.Popen("cat /etc/dhcpcd.conf", stdout=subprocess.PIPE, shell=True).communicate()[0]
        op = ""

        reEthGlobal = r"interface\s+eth0"
        mtEthGlobal = re.search(reEthGlobal, txt)

        if cbStaticEnabled:
            if not mtEthGlobal:
                txt = txt + "\n" + "interface eth0" + "\n"
            op = "interface eth0\nstatic ip_address={0}/24\nstatic routers={1}\nstatic domain_name_servers=8.8.8.8 8.8.4.4\n\n".format(
                txtEthAddress, txtEthGateway)

        res = re.sub(r"interface\s+eth0\s?(static\s+[a-z0-9./_=\s]+\n)*", op, txt)
        try:
            file = open("/etc/dhcpcd.conf", "w")
            file.write(res)
            file.close()
        except:
            if dialog.WarningOk(self, "Failed to change Ethernet Interface configuration."):
                pass

        signal = 'ETH_RECONNECT_RESULT'
        self.restartEthThreadObject = ThreadRestartNetworking(ThreadRestartNetworking.ETH, signal)
        self.restartEthThreadObject.start()
        self.connect(self.restartEthThreadObject, QtCore.SIGNAL(signal), self.ethReconnectResult)
        self.ethMessageBox = dialog.dialog(self,
                                           "Restarting networking, please wait...",
                                           icon="exclamation-mark.png",
                                           buttons=QtGui.QMessageBox.Cancel)
        if self.ethMessageBox.exec_() in {QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel}:
            self.stackedWidget.setCurrentWidget(self.networkSettingsPage)

    def ethReconnectResult(self, x):
        self.ethMessageBox.setStandardButtons(QtGui.QMessageBox.Ok)
        if x is not None:
            self.ethMessageBox.setLocalIcon('success.png')
            self.ethMessageBox.setText('Connected, IP: ' + x)
        else:

            self.ethMessageBox.setText("Not able to connect to Ethernet")

    def ethShowKeyboard(self, textbox):
        self.startKeyboard(textbox.setText, onlyNumeric=True, noSpace=True, text=str(textbox.text()))

    ''' ++++++++++++++++++++++++++++++++Display Settings+++++++++++++++++++++++++++++++ '''

    def touchCalibration(self):
        os.system('sudo /home/pi/setenv.sh')

    def showRotateDisplaySettingsPage(self):
        txt = subprocess.Popen("cat /boot/config.txt", stdout=subprocess.PIPE, shell=True).communicate()[0]

        reRot = r"dtoverlay\s*=\s*waveshare35a(\s*:\s*rotate\s*=\s*([0-9]{1,3})){0,1}"
        mtRot = re.search(reRot, txt)
        # print(mtRot.group(0))

        if mtRot and len(mtRot.groups()) == 2 and str(mtRot.group(2)) == "270":
            self.rotateDisplaySettingsComboBox.setCurrentIndex(1)
        else:
            self.rotateDisplaySettingsComboBox.setCurrentIndex(0)

        self.stackedWidget.setCurrentWidget(self.rotateDisplaySettingsPage)

    def saveRotateDisplaySettings(self):
        txt1 = subprocess.Popen("cat /boot/config.txt", stdout=subprocess.PIPE, shell=True).communicate()[0]

        reRot = r"dtoverlay\s*=\s*waveshare35a(\s*:\s*rotate\s*=\s*([0-9]{1,3})){0,1}"
        if self.rotateDisplaySettingsComboBox.currentIndex() == 1:
            op1 = "dtoverlay=waveshare35a:rotate=270"
        else:
            op1 = "dtoverlay=waveshare35a"
        res1 = re.sub(reRot, op1, txt1)

        try:
            file1 = open("/boot/config.txt", "w")
            file1.write(res1)
            file1.close()
        except:
            if dialog.WarningOk(self, "Failed to change rotation settings", overlay=True):
                return

        txt2 = subprocess.Popen("cat /etc/X11/xorg.conf.d/99-calibration.conf", stdout=subprocess.PIPE,
                                shell=True).communicate()[0]

        reTouch = r"Option\s+\"TransformationMatrix\"\s+\"([\d\s-]+)\""
        if self.rotateDisplaySettingsComboBox.currentIndex() == 1:
            op2 = "Option \"TransformationMatrix\"  \"0 1 0 -1 0 1 0 0 1\""
        else:
            op2 = "Option \"TransformationMatrix\"  \"0 -1 1 1 0 0 0 0 1\""
        res2 = re.sub(reTouch, op2, txt2, flags=re.I)

        try:
            file2 = open("/etc/X11/xorg.conf.d/99-calibration.conf", "w")
            file2.write(res2)
            file2.close()
        except:
            if dialog.WarningOk(self, "Failed to change touch settings", overlay=True):
                return

        self.askAndReboot()
        self.stackedWidget.setCurrentWidget(self.displaySettingsPage)

    ''' +++++++++++++++++++++++++++++++++Change Filament+++++++++++++++++++++++++++++++ '''

    def unloadFilament(self):
        #Update
        if self.changeFilamentComboBox.findText("Loaded Filament") == -1:
            octopiclient.setToolTemperature(
                filaments[str(self.changeFilamentComboBox.currentText())])
        self.stackedWidget.setCurrentWidget(self.changeFilamentProgressPage)
        self.changeFilamentStatus.setText("Heating , Please Wait...")
        self.changeFilamentNameOperation.setText("Unloading {}".format(str(self.changeFilamentComboBox.currentText())))
        # this flag tells the updateTemperature function that runs every second to update the filament change progress bar as well, and to load or unload after heating done
        self.changeFilamentHeatingFlag = True
        self.loadFlag = False

    def loadFilament(self):
        #Update
        if self.changeFilamentComboBox.findText("Loaded Filament") == -1:
            octopiclient.setToolTemperature(
                filaments[str(self.changeFilamentComboBox.currentText())])
        self.stackedWidget.setCurrentWidget(self.changeFilamentProgressPage)
        self.changeFilamentStatus.setText("Heating , Please Wait...")
        self.changeFilamentNameOperation.setText("Loading {}".format(str(self.changeFilamentComboBox.currentText())))
        # this flag tells the updateTemperature function that runs every second to update the filament change progress bar as well, and to load or unload after heating done
        self.changeFilamentHeatingFlag = True
        self.loadFlag = True

    def changeFilament(self):
        self.stackedWidget.setCurrentWidget(self.changeFilamentPage)
        self.changeFilamentComboBox.clear()
        self.changeFilamentComboBox.addItems(filaments.keys())
        #Update
        if self.tool0TargetTemperature > 0 and self.printerStatusText in ["Printing","Paused"]:
            self.changeFilamentComboBox.addItem("Loaded Filament")
            index = self.changeFilamentComboBox.findText("Loaded Filament")
            if index >= 0 :
                self.changeFilamentComboBox.setCurrentIndex(index)



    def changeFilamentCancel(self):
        self.changeFilamentHeatingFlag = False
        self.coolDownAction()
        self.control()

    ''' +++++++++++++++++++++++++++++++++Job Operations+++++++++++++++++++++++++++++++ '''

    def stopActionMessageBox(self):
        '''
        Displays a message box asking if the user is sure if he wants to turn off the print
        '''
        if dialog.WarningYesNo(self, "Are you sure you want to stop the print?"):
            octopiclient.cancelPrint()

    def playPauseAction(self):
        '''
        Toggles Play/Pause of a print depending on the status of the print
        '''
        if self.printerStatusText == "Operational":
            if self.playPauseButton.isChecked:
                octopiclient.startPrint()
        elif self.printerStatusText == "Printing":
            octopiclient.pausePrint()
        elif self.printerStatusText == "Paused":
            octopiclient.pausePrint()

    def fileListLocal(self):
        '''
        Gets the file list from octoprint server, displays it on the list, as well as
        sets the stacked widget page to the file list page
        '''
        self.stackedWidget.setCurrentWidget(self.fileListLocalPage)
        files = []
        for file in octopiclient.retrieveFileInformation()['files']:
            if file["type"] == "machinecode":
                files.append(file)

        self.fileListWidget.clear()
        files.sort(key=lambda d: d['date'], reverse=True)
        # for item in [f['name'] for f in files] :
        #     self.fileListWidget.addItem(item)
        self.fileListWidget.addItems([f['name'] for f in files])
        self.fileListWidget.setCurrentRow(0)

    def fileListUSB(self):
        '''
        Gets the file list from octoprint server, displays it on the list, as well as
        sets the stacked widget page to the file list page
        ToDO: Add deapth of folders recursively get all gcodes
        '''
        self.stackedWidget.setCurrentWidget(self.fileListUSBPage)
        self.fileListWidgetUSB.clear()
        files = subprocess.Popen("ls /media/usb0 | grep gcode", stdout=subprocess.PIPE, shell=True).communicate()[0]
        files = files.split('\n')
        files = filter(None, files)
        # for item in files:
        #     self.fileListWidgetUSB.addItem(item)
        self.fileListWidgetUSB.addItems(files)
        self.fileListWidgetUSB.setCurrentRow(0)

    def printSelectedLocal(self):

        '''
        gets information about the selected file from octoprint server,
        as well as sets the current page to the print selected page.
        This function also selects the file to print from octoprint
        '''
        try:
            self.fileSelected.setText(self.fileListWidget.currentItem().text())
            self.stackedWidget.setCurrentWidget(self.printSelectedLocalPage)
            file = octopiclient.retrieveFileInformation(self.fileListWidget.currentItem().text())
            try:
                self.fileSizeSelected.setText(size(file['size']))
            except KeyError:
                self.fileSizeSelected.setText('-')
            try:
                self.fileDateSelected.setText(datetime.fromtimestamp(file['date']).strftime('%d/%m/%Y %H:%M:%S'))
            except KeyError:
                self.fileDateSelected.setText('-')
            try:
                m, s = divmod(file['gcodeAnalysis']['estimatedPrintTime'], 60)
                h, m = divmod(m, 60)
                d, h = divmod(h, 24)
                self.filePrintTimeSelected.setText("%dd:%dh:%02dm:%02ds" % (d, h, m, s))
            except KeyError:
                self.filePrintTimeSelected.setText('-')
            try:
                self.filamentVolumeSelected.setText(
                    ("%.2f cm" % file['gcodeAnalysis']['filament']['tool0']['volume']) + unichr(179))
            except KeyError:
                self.filamentVolumeSelected.setText('-')

            try:
                self.filamentLengthFileSelected.setText(
                    "%.2f mm" % file['gcodeAnalysis']['filament']['tool0']['length'])
            except KeyError:
                self.filamentLengthFileSelected.setText('-')
            # uncomment to select the file when selectedd in list
            # octopiclient.selectFile(self.fileListWidget.currentItem().text(), False)
            self.stackedWidget.setCurrentWidget(self.printSelectedLocalPage)

            '''
            If image is available from server, set it, otherwise display default image
            '''
            img = octopiclient.getImage(self.fileListWidget.currentItem().text().replace(".gcode", ".png"))
            if img:
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(img)
                self.printPreviewSelected.setPixmap(pixmap)

            else:
                self.printPreviewSelected.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/thumbnail.png")))
        except:
            print "Log: Nothing Selected"
            # Set image fot print preview:
            # self.printPreviewSelected.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/fracktal.png")))
            # print self.fileListWidget.currentItem().text().replace(".gcode","")
            # self.printPreviewSelected.setPixmap(QtGui.QPixmap(_fromUtf8("/home/pi/.octoprint/uploads/{}.png".format(self.FileListWidget.currentItem().text().replace(".gcode","")))))

            # Check if the PNG file exists, and if it does display it, or diplay a default picture.

    def printSelectedUSB(self):
        '''
        Sets the screen to the print selected screen for USB, on which you can transfer to local drive and view preview image.
        :return:
        '''
        try:
            self.fileSelectedUSBName.setText(self.fileListWidgetUSB.currentItem().text())
            self.stackedWidget.setCurrentWidget(self.printSelectedUSBPage)
            file = '/media/usb0/' + str(self.fileListWidgetUSB.currentItem().text().replace(".gcode", ".png"))
            try:
                exists = os.path.exists(file)
            except:
                exists = False

            if exists:
                self.printPreviewSelectedUSB.setPixmap(QtGui.QPixmap(_fromUtf8(file)))
            else:
                self.printPreviewSelectedUSB.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/thumbnail.png")))
        except:
            print "Log: Nothing Selected"

            # Set Image from USB

    def transferToLocal(self, prnt=False):
        '''
        Transfers a file from USB mounted at /media/usb0 to octoprint's watched folder so that it gets automatically detected bu Octoprint.
        Warning: If the file is read-only, octoprint API for reading the file crashes.
        '''

        file = '/media/usb0/' + str(self.fileListWidgetUSB.currentItem().text())

        self.uploadThread = ThreadFileUpload(file, prnt=prnt)
        self.uploadThread.start()
        if prnt:
            self.stackedWidget.setCurrentWidget(self.homePage)

    def printFile(self):
        '''
        Prints the file selected from printSelected()
        '''
        octopiclient.selectFile(self.fileListWidget.currentItem().text(), True)
        # octopiclient.startPrint()
        self.stackedWidget.setCurrentWidget(self.homePage)

    def deleteItem(self):
        '''
        Deletes a gcode file, and if associates, its image file from the memory
        '''
        octopiclient.deleteFile(self.fileListWidget.currentItem().text())
        octopiclient.deleteFile(self.fileListWidget.currentItem().text().replace(".gcode", ".png"))

        # delete PNG also
        self.fileListLocal()

    ''' +++++++++++++++++++++++++++++++++Printer Status+++++++++++++++++++++++++++++++ '''

    def updateTemperature(self, temperature):
        '''
        Slot that gets a signal originating from the thread that keeps polling for printer status
        runs at 1HZ, so do things that need to be constantly updated only. This also controls the cooling fan depending on the temperatures
        :param temperature: dict containing key:value pairs with keys being the tools, bed and their values being their corresponding temperratures
        '''

        if temperature['tool0Target'] == 0:
            self.tool0TempBar.setMaximum(300)
            self.tool0TempBar.setStyleSheet(styles.bar_heater_cold)
        elif temperature['tool0Actual'] <= temperature['tool0Target']:
            self.tool0TempBar.setMaximum(temperature['tool0Target'])
            self.tool0TempBar.setStyleSheet(styles.bar_heater_heating)
        else:
            self.tool0TempBar.setMaximum(temperature['tool0Actual'])
        self.tool0TempBar.setValue(temperature['tool0Actual'])
        self.tool0ActualTemperature.setText(str(int(temperature['tool0Actual'])))  # + unichr(176)
        self.tool0TargetTemperature.setText(str(int(temperature['tool0Target'])))

        if temperature['bedTarget'] == 0:
            self.bedTempBar.setMaximum(150)
            self.bedTempBar.setStyleSheet(styles.bar_heater_cold)
        elif temperature['bedActual'] <= temperature['bedTarget']:
            self.bedTempBar.setMaximum(temperature['bedTarget'])
            self.bedTempBar.setStyleSheet(styles.bar_heater_heating)
        else:
            self.bedTempBar.setMaximum(temperature['bedActual'])
        self.bedTempBar.setValue(temperature['bedActual'])
        self.bedActualTemperatute.setText(str(int(temperature['bedActual'])))  # + unichr(176))
        self.bedTargetTemperature.setText(str(int(temperature['bedTarget'])))  # + unichr(176))

        # updates the progress bar on the change filament screen
        if self.changeFilamentHeatingFlag:
            if temperature['tool0Target'] == 0:
                self.changeFilamentProgress.setMaximum(300)
            elif temperature['tool0Target'] - temperature['tool0Actual'] > 1:
                self.changeFilamentProgress.setMaximum(temperature['tool0Target'])
            else:
                self.changeFilamentProgress.setMaximum(temperature['tool0Actual'])
                self.changeFilamentHeatingFlag = False
                if self.loadFlag:
                    self.stackedWidget.setCurrentWidget(self.changeFilamentExtrudePage)
                else:
                    self.stackedWidget.setCurrentWidget(self.changeFilamentRetractPage)
                    octopiclient.extrude(10)  # extrudes some amount of filament to prevent plugging

            self.changeFilamentProgress.setValue(temperature['tool0Actual'])

    def updatePrintStatus(self, file):
        '''
        displays infromation of a particular file on the home page,is a slot for the signal emited from the thread that keeps pooling for printer status
        runs at 1HZ, so do things that need to be constantly updated only
        :param file: dict of all the attributes of a particualr file
        '''
        if file is None:
            self.currentFile = None
            self.currentImage = None
            self.timeLeft.setText("-")
            self.fileName.setText("-")
            self.printProgressBar.setValue(0)
            self.printTime.setText("-")
            self.playPauseButton.setDisabled(True)  # if file available, make play buttom visible

        else:
            self.playPauseButton.setDisabled(False)  # if file available, make play buttom visible
            self.fileName.setText(file['job']['file']['name'])
            self.currentFile = file['job']['file']['name']
            if file['progress']['printTime'] is None:
                self.printTime.setText("-")
            else:
                m, s = divmod(file['progress']['printTime'], 60)
                h, m = divmod(m, 60)
                d, h = divmod(h, 24)
                self.printTime.setText("%d:%d:%02d:%02d" % (d, h, m, s))

            if file['progress']['printTimeLeft'] is None:
                self.timeLeft.setText("-")
            else:
                m, s = divmod(file['progress']['printTimeLeft'], 60)
                h, m = divmod(m, 60)
                d, h = divmod(h, 24)
                self.timeLeft.setText("%d:%d:%02d:%02d" % (d, h, m, s))

            if file['progress']['completion'] is None:
                self.printProgressBar.setValue(0)
            else:
                self.printProgressBar.setValue(file['progress']['completion'])

            '''
            If image is available from server, set it, otherwise display default image.
            If the image was already loaded, dont load it again.
            '''
            if self.currentImage != self.currentFile:
                self.currentImage = self.currentFile
                img = octopiclient.getImage(file['job']['file']['name'].replace(".gcode", ".png"))
                if img:
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(img)
                    self.printPreviewMain.setPixmap(pixmap)
                else:
                    self.printPreviewMain.setPixmap(QtGui.QPixmap(_fromUtf8("templates/img/thumbnail.png")))

    def updateStatus(self, status):
        '''
        Updates the status bar, is a slot for the signal emited from the thread that constantly polls for printer status
        this function updates the status bar, as well as enables/disables relavent buttons
        :param status: String of the status text
        '''

        self.printerStatusText = status
        self.printerStatus.setText(status)

        if status == "Printing":  # Green
            self.printerStatusColour.setStyleSheet(styles.printer_status_green)
        elif status == "Offline":  # Red
            self.printerStatusColour.setStyleSheet(styles.printer_status_red)
        elif status == "Paused":  # Amber
            self.printerStatusColour.setStyleSheet(styles.printer_status_amber)
        elif status == "Operational":  # Amber
            self.printerStatusColour.setStyleSheet(styles.printer_status_blue)

        '''
        Depending on Status, enable and Disable Buttons
        '''
        if status == "Printing":
            self.playPauseButton.setChecked(True)
            self.stopButton.setDisabled(False)
            self.motionTab.setDisabled(True)
            self.changeFilamentButton.setDisabled(True)
            self.menuCalibrateButton.setDisabled(True)
            self.menuPrintButton.setDisabled(True)
            if not self.__timelapse_enabled:
                octopiclient.cancelPrint()
                self.coolDownAction()

        elif status == "Paused":
            self.playPauseButton.setChecked(False)
            self.stopButton.setDisabled(False)
            self.motionTab.setDisabled(False)
            self.changeFilamentButton.setDisabled(False)
            self.menuCalibrateButton.setDisabled(True)
            self.menuPrintButton.setDisabled(True)

        else:
            self.stopButton.setDisabled(True)
            self.playPauseButton.setChecked(False)
            self.motionTab.setDisabled(False)
            self.changeFilamentButton.setDisabled(False)
            self.menuCalibrateButton.setDisabled(False)
            self.menuPrintButton.setDisabled(False)

    ''' +++++++++++++++++++++++++++++++++Control Screen+++++++++++++++++++++++++++++++ '''

    def control(self):
        self.stackedWidget.setCurrentWidget(self.controlPage)
        self.toolTempSpinBox.setProperty("value", float(self.tool0TargetTemperature.text()))
        self.bedTempSpinBox.setProperty("value", float(self.bedTargetTemperature.text()))

    def setStep(self, stepRate):
        '''
        Sets the class variable "Step" which would be needed for movement and joging
        :param step: step multiplier for movement in the move
        :return: nothing
        '''

        if stepRate == 100:
            self.step100Button.setFlat(True)
            self.step1Button.setFlat(False)
            self.step10Button.setFlat(False)
            self.step = 100
        if stepRate == 1:
            self.step100Button.setFlat(False)
            self.step1Button.setFlat(True)
            self.step10Button.setFlat(False)
            self.step = 1
        if stepRate == 10:
            self.step100Button.setFlat(False)
            self.step1Button.setFlat(False)
            self.step10Button.setFlat(True)
            self.step = 10

    def coolDownAction(self):
        ''''
        Turns all heaters and fans off
        '''
        octopiclient.gcode(command='M107')
        octopiclient.setToolTemperature({"tool0": 0})
        # octopiclient.setToolTemperature({"tool0": 0})
        octopiclient.setBedTemperature(0)
        self.toolTempSpinBox.setProperty("value", 0)
        self.bedTempSpinBox.setProperty("value", 0)

    ''' +++++++++++++++++++++++++++++++++++Calibration++++++++++++++++++++++++++++++++ '''

    def getZHomeOffset(self, offset):
        '''
        Sets the spinbox value to have the value of the Z offset from the printer.
        the value is -ve so as to be more intuitive.
        :param offset:
        :return:
        '''
        self.nozzleOffsetDoubleSpinBox.setValue(-float(offset))
        self.nozzleHomeOffset = offset  # update global value of

    def setZHomeOffset(self, offset, setOffset=False):
        '''
        Sets the home offset after the calibration wizard is done, which is a callback to
        the response of M114 that is sent at the end of the Wizard in doneStep()
        :param offset: the value off the offset to set. is a str is coming from M114, and is float if coming from the nozzleOffsetPage
        :param setOffset: Boolean, is true if the function call is from the nozzleOffsetPage, else the current Z value sets the offset
        :return:

        #TODO can make this simpler, asset the offset value to string float to begin with instead of doing confitionals
        '''

        if self.setHomeOffsetBool:  # when this is true, M114 Z value will set stored as Z offset
            octopiclient.gcode(command='M206 Z{}'.format(-float(offset)))  # Convert the string to float
            self.setHomeOffsetBool = False
            octopiclient.gcode(command='M500')
            # save in EEPROM
        if setOffset:  # When the offset needs to be set from spinbox value
            octopiclient.gcode(command='M206 Z{}'.format(-offset))
            octopiclient.gcode(command='M500')

    def nozzleOffset(self):
        '''
        Updates the value of M206 Z in the nozzle offset spinbox. Sends M503 so that the pritner returns the value as a websocket calback
        :return:
        '''
        octopiclient.gcode(command='M503')
        self.stackedWidget.setCurrentWidget(self.nozzleOffsetPage)

    def quickStep1(self, fullCalibration=False):
        '''
        Shows welcome message.
        Sets Z Home Offset = 0
        Homes to MAX
        goes to position where leveling screws can be opened
        :return:
        '''

        octopiclient.gcode(
            command='M503')  # gets the value of Z offset, that would be restored later, see getZHomeOffset()
        octopiclient.gcode(command='M420 S0')  # Dissable mesh bed leveling for good measure
        self.fullCalibration = fullCalibration
        octopiclient.gcode(command='M206 Z0')  # Sets Z home offset to 0
        octopiclient.home(['x', 'y', 'z'])
        octopiclient.jog(x=100, y=100, z=15, absolute=True, speed=1500)
        self.stackedWidget.setCurrentWidget(self.quickStep1Page)

    def quickStep2(self):
        '''
        Askes user to release all Leveling Screws
        :return:
        '''
        self.stackedWidget.setCurrentWidget(self.quickStep2Page)

    def quickStep3(self):
        '''
        leveks first position
        :return:
        '''
        self.stackedWidget.setCurrentWidget(self.quickStep3Page)
        octopiclient.jog(x=calibrationPosition['X1'], y=calibrationPosition['Y1'], absolute=True, speed=9000)
        octopiclient.jog(z=0, absolute=True, speed=1500)

    def quickStep4(self):
        '''
        levels decond leveling position
        '''
        self.stackedWidget.setCurrentWidget(self.quickStep4Page)
        octopiclient.jog(z=10, absolute=True, speed=1500)
        octopiclient.jog(x=calibrationPosition['X2'], y=calibrationPosition['Y2'], absolute=True, speed=9000)
        octopiclient.jog(z=0, absolute=True, speed=1500)

    def quickStep5(self):
        '''
        levels third leveling position
        :return:
        '''
        # sent twice for some reason
        self.stackedWidget.setCurrentWidget(self.quickStep5Page)
        octopiclient.jog(z=10, absolute=True, speed=1500)
        octopiclient.jog(x=calibrationPosition['X3'], y=calibrationPosition['Y3'], absolute=True, speed=9000)
        octopiclient.jog(z=0, absolute=True, speed=1500)

    def proceedToFull(self):
        '''
        decides weather to go to full calibration of return to calibration screen
        :return:
        '''
        if not self.fullCalibration:
            self.stackedWidget.setCurrentWidget(self.calibratePage)
            octopiclient.gcode(command='M501')  # restore eeprom settings to get Z home offset, mesh bed leveling back
            octopiclient.home(['x', 'y', 'z'])
        else:
            self.fullStep1()

    def fullStep1(self):
        '''
        levels third leveling position
        :return:
        '''
        # sent twice for some reason
        self.stackedWidget.setCurrentWidget(self.fullStep1Page)
        octopiclient.jog(z=10, absolute=True, speed=9000)
        octopiclient.jog(x=0, y=0, absolute=True, speed=9000)
        # octopiclient.home(['x', 'y', 'z'])
        self.fullLevelingCount = 0

    def fullStep2(self):
        '''
        levels third leveling position
        :return:
        '''
        self.pointLabel.setText("Point {} of 9".format(int(self.fullLevelingCount + 1)))
        if self.fullLevelingCount == 0:  # first point
            octopiclient.gcode(command='G29 S1')
            self.stackedWidget.setCurrentWidget(self.fullStep2Page)
            self.fullLevelingCount += 1

        else:
            # All other poitns
            if self.fullLevelingCount < 9:
                self.stackedWidget.setCurrentWidget(self.fullStep2Page)
                octopiclient.gcode(command='G29 S2')
                self.fullLevelingCount += 1
            else:
                octopiclient.gcode(command='G29 S2')
                self.stackedWidget.setCurrentWidget(self.calibratePage)
                octopiclient.gcode(command='M206 Z{}'.format(self.nozzleHomeOffset))  # restore Z offset
                octopiclient.gcode(command='M500')  # save mesh and restored Z offset

    def cancelStep(self):
        octopiclient.gcode(command='M501')  # restore eeprom settings
        self.stackedWidget.setCurrentWidget(self.calibratePage)

    ''' +++++++++++++++++++++++++++++++++++Keyboard++++++++++++++++++++++++++++++++ '''

    def startKeyboard(self, returnFn, onlyNumeric=False, noSpace=False, text=""):
        '''
        starts the keyboard screen for entering Password
        '''
        keyBoardobj = keyboard.Keyboard(onlyNumeric=onlyNumeric, noSpace=noSpace, text=text)
        self.connect(keyBoardobj, QtCore.SIGNAL('KEYBOARD'), returnFn)
        keyBoardobj.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        keyBoardobj.show()

    ''' ++++++++++++++++++++++++++++++Restore Defaults++++++++++++++++++++++++++++ '''

    def restoreFactoryDefaults(self):
        if dialog.WarningYesNo(self, "Are you sure you want to restore machine state to factory defaults?\nWarning: Doing so will also reset printer profiles, WiFi & Ethernet config.",
                               overlay=True):
            os.system('sudo cp -f config/dhcpcd.conf /etc/dhcpcd.conf')
            os.system('sudo cp -f config/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf')
            os.system('sudo rm -rf /home/pi/.octoprint/users.yaml')
            os.system('sudo rm -rf /home/pi/.octoprint/printerProfiles/*')
            os.system('sudo rm -rf /home/pi/.octoprint/scripts/gcode')
            os.system('sudo cp -f config/config_Julia2018ExtendedTouchUI.yaml /home/pi/.octoprint/config.yaml')
            os.system('sudo rm -rf /home/pi/.fw_logo.dat')
            self.tellAndReboot("Settings restored. Rebooting...")

    def restorePrintDefaults(self):
        if dialog.WarningYesNo(self, "Are you sure you want to restore default print settings?\nWarning: Doing so will erase offsets and bed leveling info",
                               overlay=True):
            octopiclient.gcode(command='M502')
            octopiclient.gcode(command='M500')

    ''' +++++++++++++++++++++++++++++++++++ Misc ++++++++++++++++++++++++++++++++ '''

    def tellAndReboot(self, msg="Rebooting...", overlay=True):
        if dialog.WarningOk(self, msg, overlay=overlay):
            os.system('sudo reboot now')
            return True
        return False

    def askAndReboot(self, msg="Are you sure you want to reboot?", overlay=True):
        if dialog.WarningYesNo(self, msg, overlay=overlay):
            os.system('sudo reboot now')
            return True
        return False

    def handleStartupError(self):
        print('Shutting Down. Unable to connect')
        if dialog.WarningOk(self, "Error. Contact Support. Shutting down...", overlay=True):
            os.system('sudo shutdown now')

    def pairPhoneApp(self):
        if getIP(ThreadRestartNetworking.ETH) is not None:
            qrip = getIP(ThreadRestartNetworking.ETH)
        elif getIP(ThreadRestartNetworking.WLAN) is not None:
            qrip = getIP(ThreadRestartNetworking.WLAN)
        else:
            if dialog.WarningOk(self, "Network Disconnected"):
                return
        self.QRCodeLabel.setPixmap(
            qrcode.make(json.dumps(qrip), image_factory=Image).pixmap())
        self.stackedWidget.setCurrentWidget(self.QRCodePage)


class QtWebsocket(QtCore.QThread):
    '''
    https://pypi.python.org/pypi/websocket-client
    https://wiki.python.org/moin/PyQt/Threading,_Signals_and_Slots
    '''

    def __init__(self):
        super(QtWebsocket, self).__init__()

        url = "ws://{}/sockjs/{:0>3d}/{}/websocket".format(
            ip,  # host + port + prefix, but no protocol
            random.randrange(0, stop=999),  # server_id
            uuid.uuid4()  # session_id
        )
        self.ws = websocket.WebSocketApp(url,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)

    def run(self):
        self.ws.run_forever()

    def on_message(self, ws, message):

        message_type = message[0]
        if message_type == "h":
            # "heartbeat" message
            return
        elif message_type == "o":
            # "open" message
            return
        elif message_type == "c":
            # "close" message
            return

        message_body = message[1:]
        if not message_body:
            return
        data = json.loads(message_body)[0]

        if message_type == "m":
            data = [data, ]

        if message_type == "a":
            self.process(data)

    @run_async
    def process(self, data):

        if "event" in data:
            if data["event"]["type"] == "Connected":
                self.emit(QtCore.SIGNAL('CONNECTED'))



        if "plugin" in data:
            if data["plugin"]["plugin"] == 'Julia2018FilamentSensor':
                self.emit(QtCore.SIGNAL('FILAMENT_SENSOR_TRIGGERED'), data["plugin"]["data"])

            if data["plugin"]["plugin"] == 'JuliaFirmwareUpdater':
                self.emit(QtCore.SIGNAL('FIRMWARE_UPDATER'), data["plugin"]["data"])

            elif data["plugin"]["plugin"] == 'softwareupdate':
                if data["plugin"]["data"]["type"] == "updating":
                    self.emit(QtCore.SIGNAL('UPDATE_STARTED'), data["plugin"]["data"]["data"])
                elif data["plugin"]["data"]["type"] == "loglines":
                    self.emit(QtCore.SIGNAL('UPDATE_LOG'), data["plugin"]["data"]["data"]["loglines"])
                elif data["plugin"]["data"]["type"] == "restarting":
                    self.emit(QtCore.SIGNAL('UPDATE_LOG_RESULT'), data["plugin"]["data"]["data"]["results"])
                elif data["plugin"]["data"]["type"] == "update_failed":
                    self.emit(QtCore.SIGNAL('UPDATE_FAILED'), data["plugin"]["data"]["data"])

        if "current" in data:

            if data["current"]["messages"]:
                for item in data["current"]["messages"]:
                    if 'M206' in item: #response to M503, send current Z offset value
                        self.emit(QtCore.SIGNAL('Z_HOME_OFFSET'), item[item.index('Z') + 1:].split(' ', 1)[0])
                    # if 'Count' in item:  # gets the current Z value, uses it to set Z offset
                    #     self.emit(QtCore.SIGNAL('SET_Z_HOME_OFFSET'), item[item.index('Z') + 2:].split(' ', 1)[0],
                    #               False)

            if data["current"]["state"]["text"]:
                self.emit(QtCore.SIGNAL('STATUS'), data["current"]["state"]["text"])

            fileInfo = {"job": data["current"]["job"], "progress": data["current"]["progress"]}
            if fileInfo['job']['file']['name'] is not None:
                self.emit(QtCore.SIGNAL('PRINT_STATUS'), fileInfo)
            else:
                self.emit(QtCore.SIGNAL('PRINT_STATUS'), None)

            def temp(data, tool, temp):
                try:
                    if tool in data["current"]["temps"][0]:
                        return data["current"]["temps"][0][tool][temp]
                except:
                    pass
                return 0

            if data["current"]["temps"] and len(data["current"]["temps"]) > 0:
                try:
                    temperatures = {'tool0Actual': temp(data, "tool0", "actual"),
                                    'tool0Target': temp(data, "tool0", "target"),
                                    'bedActual': temp(data, "bed", "actual"),
                                    'bedTarget': temp(data, "bed", "target")}
                    self.emit(QtCore.SIGNAL('TEMPERATURES'), temperatures)
                except KeyError:
                    # temperatures = {'tool0Actual': data["current"]["temps"][0]["tool0"]["actual"],
                    #                 'tool0Target': data["current"]["temps"][0]["tool0"]["target"],
                    #                 'bedActual': data["current"]["temps"][0]["bed"]["actual"],
                    #                 'bedTarget': data["current"]["temps"][0]["bed"]["target"]}
                    pass
                # self.emit(QtCore.SIGNAL('TEMPERATURES'), temperatures)

    def on_open(self, ws):
        pass

    def on_close(self, ws):
        pass

    def on_error(self, ws, error):
        pass


class ThreadSanityCheck(QtCore.QThread):
    def __init__(self, logger, virtual=False):
        super(ThreadSanityCheck, self).__init__()
        self.MKSPort = None
        self.virtual = virtual
        self._logger = logger

    def run(self):
        global octopiclient
        shutdown_flag = False
        # get the first value of t1 (runtime check)
        uptime = 0
        # keep trying untill octoprint connects
        while (True):
            # Start an object instance of octopiAPI
            try:
                if (uptime > 30):
                    shutdown_flag = True
                    self.emit(QtCore.SIGNAL('STARTUP_ERROR'))
                    break
                octopiclient = octoprintAPI(ip, apiKey)
                result = subprocess.Popen("dmesg | grep 'ttyUSB'", stdout=subprocess.PIPE, shell=True).communicate()[0]
                result = result.split('\n')  # each ssid and pass from an item in a list ([ssid pass,ssid paas])
                result = [s.strip() for s in result]
                if not self.virtual:
                    result = subprocess.Popen("dmesg | grep 'ttyUSB'", stdout=subprocess.PIPE, shell=True).communicate()[0]
                    result = result.split('\n')  # each ssid and pass from an item in a list ([ssid pass,ssid paas])
                    result = [s.strip() for s in result]
                    for line in result:
                        if 'FTDI' in line:
                            self.MKSPort = line[line.index('ttyUSB'):line.index('ttyUSB') + 7]
                            print self.MKSPort

                if not self.MKSPort:
                    octopiclient.connectPrinter(port="VIRTUAL", baudrate=115200)
                else:
                    octopiclient.connectPrinter(port="/dev/" + self.MKSPort, baudrate=115200)
                break
            except Exception as e:
                time.sleep(1)
                uptime = uptime + 1
                # print "Not Connected!"
                print(e.message)
                self._logger.error("ThreadSanityCheck: " + str(e.message))
        if not shutdown_flag:
            self.emit(QtCore.SIGNAL('LOADED'))


class ThreadFileUpload(QtCore.QThread):
    def __init__(self, file, prnt=False):
        super(ThreadFileUpload, self).__init__()
        self.file = file
        self.prnt = prnt

    def run(self):

        try:
            exists = os.path.exists(self.file.replace(".gcode", ".png"))
        except:
            exists = False
        if exists:
            octopiclient.uploadImage(self.file.replace(".gcode", ".png"))

        if self.prnt:
            octopiclient.uploadGcode(file=self.file, select=True, prnt=True)
        else:
            octopiclient.uploadGcode(file=self.file, select=False, prnt=False)


class ThreadRestartNetworking(QtCore.QThread):
    WLAN = "wlan0"
    ETH = "eth0"

    def __init__(self, interface, signal):
        super(ThreadRestartNetworking, self).__init__()
        self.interface = interface
        self.signal = signal

    def run(self):
        self.restart_interface()
        attempt = 0
        while attempt < 3:
            if getIP(self.interface):
                self.emit(QtCore.SIGNAL(self.signal), getIP(self.interface))
                break
            else:
                attempt += 1
                time.sleep(1)
        if attempt >= 3:
            self.emit(QtCore.SIGNAL(self.signal), None)

    def restart_interface(self):
        '''
        restars wlan0 wireless interface to use new changes in wpa_supplicant.conf file
        :return:
        '''
        subprocess.call(["ifdown", "--force", self.interface], shell=False)
        subprocess.call(["ifup", "--force", self.interface], shell=False)
        time.sleep(5)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # Intialize the library (must be called once before other functions).
    # Creates an object of type MainUiClass
    MainWindow = MainUiClass()
    MainWindow.show()
    # MainWindow.showFullScreen()
    # MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    # Create NeoPixel object with appropriate configuration.
    # charm = FlickCharm()
    # charm.activateOn(MainWindow.FileListWidget)
sys.exit(app.exec_())

