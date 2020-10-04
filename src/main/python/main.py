# @author KOOKIIE Studios
# A GUI Implementation of MaplePacketPuller by Brandon Nguyen
#
# This program uses the MVC variant: Model View architecture
# main.py handles the GUI and controller aspect of the program (aka ViewController or View)

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os
import qdarkstyle


# Constants - Resources Paths
ICON_PATH = "../icons/base/spirit.ico"
IMAGE_PATH = "../resources/spirit.png"
# Fonts
BAUH_PATH = "../resources/BAUHS93.TTF"
FORTE_PATH = "../resources/FORTE.TTF"
GARA_PATH = "../resources/GARA.TTF"
GARABD_PATH = "../resources/GARABD.TTF"



class MainWindow(QMainWindow):
    def __init__(self):
        # Initialise superclass; insert function calls below this line
        super(MainWindow, self).__init__()
        self.setupUi(self)

    # define function calls here
    # initialise the UI of the main window
    # wholesale imported from Qt Designer - make changes via Qt Designer, not hard-coding
    # Note: replace Qt Designer-generated path for icons and images i.e. for all setPixmap(QtGui.QPixmap(<path>))
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 542)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 542))
        MainWindow.setMaximumSize(QtCore.QSize(800, 542))
        MainWindow.setBaseSize(QtCore.QSize(-1, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ICON_PATH), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listFrame = QtWidgets.QFrame(self.centralwidget)
        self.listFrame.setGeometry(QtCore.QRect(0, 10, 481, 511))
        self.listFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listFrame.setObjectName("listFrame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.listFrame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 441, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.listLabelLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.listLabelLayout.setContentsMargins(0, 0, 0, 0)
        self.listLabelLayout.setObjectName("listLabelLayout")
        self.inputLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.inputLabel.setObjectName("inputLabel")
        self.listLabelLayout.addWidget(self.inputLabel)
        self.outputLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.outputLabel.setObjectName("outputLabel")
        self.listLabelLayout.addWidget(self.outputLabel)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.listFrame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 441, 421))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.listLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.listLayout.setContentsMargins(0, 0, 0, 0)
        self.listLayout.setObjectName("listLayout")
        self.inputList = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.inputList.setObjectName("inputList")
        self.listLayout.addWidget(self.inputList)
        self.outputList = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.outputList.setObjectName("outputList")
        self.listLayout.addWidget(self.outputList)
        self.selectAllButton = QtWidgets.QPushButton(self.listFrame)
        self.selectAllButton.setGeometry(QtCore.QRect(20, 460, 71, 23))
        self.selectAllButton.setObjectName("selectAllButton")
        self.statusLabel = QtWidgets.QLabel(self.listFrame)
        self.statusLabel.setGeometry(QtCore.QRect(20, 490, 461, 16))
        self.statusLabel.setObjectName("statusLabel")
        self.processButton = QtWidgets.QPushButton(self.centralwidget)
        self.processButton.setGeometry(QtCore.QRect(634, 480, 141, 41))
        self.processButton.setObjectName("processButton")
        self.optionsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.optionsGroupBox.setGeometry(QtCore.QRect(500, 270, 271, 181))
        self.optionsGroupBox.setObjectName("optionsGroupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.optionsGroupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 19, 251, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.optionsVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.optionsVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.optionsVerticalLayout.setObjectName("optionsVerticalLayout")
        self.advancedFormLayout = QtWidgets.QFormLayout()
        self.advancedFormLayout.setObjectName("advancedFormLayout")
        self.advancedLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.advancedLabel.setObjectName("advancedLabel")
        self.advancedFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.advancedLabel)
        self.advancedComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.advancedComboBox.setObjectName("advancedComboBox")
        self.advancedFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.advancedComboBox)
        self.debugModeCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.debugModeCheckBox.setObjectName("debugModeCheckBox")
        self.advancedFormLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.debugModeCheckBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.advancedFormLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.optionsVerticalLayout.addLayout(self.advancedFormLayout)
        self.spiritLogo = QtWidgets.QLabel(self.centralwidget)
        self.spiritLogo.setGeometry(QtCore.QRect(640, 30, 141, 81))
        self.spiritLogo.setText("")
        self.spiritLogo.setPixmap(QtGui.QPixmap(IMAGE_PATH))
        self.spiritLogo.setObjectName("spiritLogo")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(550, 110, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(20)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.studioLabel = QtWidgets.QLabel(self.centralwidget)
        self.studioLabel.setGeometry(QtCore.QRect(650, 170, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.studioLabel.setFont(font)
        self.studioLabel.setObjectName("studioLabel")
        self.toolkitLabel = QtWidgets.QLabel(self.centralwidget)
        self.toolkitLabel.setGeometry(QtCore.QRect(590, 140, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.toolkitLabel.setFont(font)
        self.toolkitLabel.setObjectName("toolkitLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spirit PacketPuller - alpha v1.0"))
        self.inputLabel.setText(_translate("MainWindow", "Files that can be processed:"))
        self.outputLabel.setText(_translate("MainWindow", "Process queue:"))
        self.selectAllButton.setText(_translate("MainWindow", "Select All"))
        self.statusLabel.setText(_translate("MainWindow", "Status: Lorem Ipsum"))
        self.processButton.setText(_translate("MainWindow", "Process"))
        self.optionsGroupBox.setTitle(_translate("MainWindow", "Options:"))
        self.advancedLabel.setText(_translate("MainWindow", "Advanced:"))
        self.debugModeCheckBox.setText(_translate("MainWindow", "Debug Mode"))
        self.nameLabel.setText(_translate("MainWindow", "Spirit PacketPuller"))
        self.studioLabel.setText(_translate("MainWindow", "KOOKIIE Studios 2020"))
        self.toolkitLabel.setText(_translate("MainWindow", "SPIRIT SUITE TOOLKIT"))


# Use custom fonts
def add_app_font():
    QtGui.QFontDatabase.addApplicationFont(BAUH_PATH)
    QtGui.QFontDatabase.addApplicationFont(FORTE_PATH)
    QtGui.QFontDatabase.addApplicationFont(GARA_PATH)
    QtGui.QFontDatabase.addApplicationFont(GARABD_PATH)


# Main script sequence
if __name__ == '__main__':
    appContext = ApplicationContext()  # 1. Instantiate ApplicationContext
    # Stylesheet is optional; title bar colour cannot be changed, and will remain white
    # appContext.app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    add_app_font()
    window = MainWindow()
    window.show()
    exit_code = appContext.app.exec_()  # 2. Invoke appContext.app.exec_()
    sys.exit(exit_code)
