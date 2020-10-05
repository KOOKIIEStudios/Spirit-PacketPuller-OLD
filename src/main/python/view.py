# ViewController Module
# GUI component of the program

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import model, engine, constants, logger
from main import spirit_logger as main_logger

spirit_logger = logger.get_logger("main.view")


class MainWindow(QMainWindow):
    def __init__(self):
        # Initialise superclass; insert function calls below this line
        super(MainWindow, self).__init__()
        spirit_logger.debug("Initialising MainWindow...")
        self.setupUi(self)

        # Instantiate Input List
        try:
            self.inputListModel = model.InputListModel()
            self.loadInputList()  # Load processable files into list
            self.inputList.setModel(self.inputListModel)
        except:
            spirit_logger.error("Failed to instantiate input list!")

        # Instantiate Output List
        try:
            self.outListModel = model.OutputListModel()
            self.outputList.setModel(self.outListModel)
        except:
            spirit_logger.error("Failed to instantiate output list!")

        spirit_logger.debug("Finished setting GUI of MainWindow")

        # LISTENERS
        # toggle Debug Mode
        spirit_logger.debug("Setting event listeners...")
        self.debugModeCheckBox.stateChanged.connect(lambda: self.loggerState(self.debugModeCheckBox))
        # Manual Input List Refreshes
        self.refreshButton.pressed.connect(lambda: self.loadInputList())
        # Item in Input List selected
        self.inputList.selectionModel().selectionChanged.connect(lambda: self.addToQueue())
        # Item in Output List selected
        self.outputList.selectionModel().selectionChanged.connect(lambda: self.removeFromQueue())
        # Select All button
        self.selectAllButton.pressed.connect(lambda: self.addAllToQueue())
        # Deselect All button
        self.deselectAllButton.pressed.connect(lambda: self.removeAllFromQueue())
        # Process button
        self.processButton.pressed.connect(lambda: self.process())
        spirit_logger.debug("Event listener set")


    # initialise the UI of the main window
    # wholesale imported from Qt Designer - make changes via Qt Designer, not hard-coding
    # Note: replace Qt Designer-generated path for icons and images i.e. for all setPixmap(QtGui.QPixmap(<path>))
    def setupUi(self, MainWindow):
        spirit_logger.debug("Setting UI of MainWindow...")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 530)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(790, 530))
        MainWindow.setMaximumSize(QtCore.QSize(790, 530))
        MainWindow.setBaseSize(QtCore.QSize(-1, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(constants.ICON_PATH), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.inputList = QtWidgets.QListView(self.horizontalLayoutWidget_2)
        self.inputList.setObjectName("inputList")
        self.listLayout.addWidget(self.inputList)
        self.outputList = QtWidgets.QListView(self.horizontalLayoutWidget_2)
        self.outputList.setObjectName("outputList")
        self.listLayout.addWidget(self.outputList)
        self.selectAllButton = QtWidgets.QPushButton(self.listFrame)
        self.selectAllButton.setGeometry(QtCore.QRect(20, 460, 75, 23))
        self.selectAllButton.setObjectName("selectAllButton")
        self.statusLabel = QtWidgets.QLabel(self.listFrame)
        self.statusLabel.setGeometry(QtCore.QRect(20, 490, 450, 16))
        self.statusLabel.setObjectName("statusLabel")
        self.refreshButton = QtWidgets.QPushButton(self.listFrame)
        self.refreshButton.setGeometry(QtCore.QRect(130, 460, 75, 23))
        self.refreshButton.setObjectName("refreshButton")
        self.deselectAllButton = QtWidgets.QPushButton(self.listFrame)
        self.deselectAllButton.setGeometry(QtCore.QRect(240, 460, 75, 23))
        self.deselectAllButton.setObjectName("deselectAllButton")
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
        self.spiritLogo.setPixmap(QtGui.QPixmap(constants.IMAGE_PATH))
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
        self.toolkitLabel.setGeometry(QtCore.QRect(590, 140, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.toolkitLabel.setFont(font)
        self.toolkitLabel.setObjectName("toolkitLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Default text set on initialise - called by setupUi()
    def retranslateUi(self, MainWindow):
        spirit_logger.debug("Setting text of MainWindow...")
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spirit PacketPuller - Alpha v1.1"))
        self.inputLabel.setText(_translate("MainWindow", "Files that can be processed:"))
        self.outputLabel.setText(_translate("MainWindow", "Process queue:"))
        self.selectAllButton.setText(_translate("MainWindow", "Select All"))
        self.statusLabel.setText(_translate("MainWindow", "Status: Lorem Ipsum"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh"))
        self.deselectAllButton.setText(_translate("MainWindow", "Deselect All"))
        self.processButton.setText(_translate("MainWindow", "Process"))
        self.optionsGroupBox.setTitle(_translate("MainWindow", "Options:"))
        self.advancedLabel.setText(_translate("MainWindow", "Advanced:"))
        self.debugModeCheckBox.setText(_translate("MainWindow", "Debug Mode"))
        self.nameLabel.setText(_translate("MainWindow", "Spirit PacketPuller"))
        self.studioLabel.setText(_translate("MainWindow", "KOOKIIE Studios 2020"))
        self.toolkitLabel.setText(_translate("MainWindow", "SPIRIT SUITE TOOLKIT"))
        spirit_logger.debug("Finished setting UI of MainWindow")
        # Qt designer copy-pasta ends here
        self.advancedComboBox.addItem(constants.NONE)
        self.advancedComboBox.addItem(constants.AGRESSIVE)
        self.advancedComboBox.addItem(constants.INHEADER)
        spirit_logger.debug("Advanced options loaded")



    def turnLoggerOn(self):
        main_logger.addHandler(logger.get_console_handler())
        main_logger.addHandler(logger.get_file_handler())
        main_logger.propagate = True
        main_logger.info("Logger turned on!")

    def turnLoggeroff(self):
        main_logger.info("Turning logger off!")
        main_logger.removeHandler(logger.get_console_handler())
        main_logger.removeHandler(logger.get_file_handler())
        main_logger.propagate = False

    def loggerState(self, checkbox):
        if checkbox.isChecked():
            self.turnLoggerOn()
        else:
            self.turnLoggeroff()

    def loadInputList(self):
        """
        Method to load the list of .txt files in Input folder into the Input list GUI

        Raises:
            OS Error
            A generic error
        """

        # Initialise
        spirit_logger.debug("Clearing Input List and Loading from file...")
        self.inputListModel.files = []
        try:
            func_list = engine.get_func_list()
            for element in func_list:
                self.inputListModel.files.append(element)
            spirit_logger.debug("Input List loaded!")
            self.inputListModel.layoutChanged.emit()  # refresh the list
            spirit_logger.debug("Layout Change Emit called")
        except OSError as e:
            spirit_logger.error(f"OS Error: {e}")
        except:
            spirit_logger.error(f"Failed to load list of files from the following directory: {constants.FUNC_DIR}")

        try:
            spirit_logger.debug("attempting to re-add logo")
            spirit_logger.debug(f"Working dir: {engine.get_root_dir()}")
            self.spiritLogo.setPixmap(QtGui.QPixmap(constants.IMAGE_PATH))
        except:
            spirit_logger.error("ERROR: Could not add logo")

    def addToQueue(self):
        """
        Adds selection in Input List to Output List
        """

        indexes = self.inputList.selectedIndexes()  # read selection from Input List
        if indexes:
            spirit_logger.debug("Adding to Output List...")
            # Indexes is a list of a single item in single-select mode.
            index = indexes[0]
            # Write to Output list
            self.outListModel.addFile(self.inputListModel.files[index.row()])
            spirit_logger.debug("File Added")
            self.outListModel.layoutChanged.emit()
            spirit_logger.debug("Layout Change Emit called")
            self.inputList.clearSelection()
            spirit_logger.debug("Input List selection cleared")

    def removeFromQueue(self):
        """
        Removes selection in Output List

        WARNING: NOT THREAD SAFE
         self.outListModel.removeFile() contains self.beginRemoveRows()
         This is a necessary function because it updates the necessary UI elements before the underlying data is changed
         This prevents asynchronicity.
         However, because the listener is waiting for a selection change event,
         the updating of UI triggers removeFromQueue() recursively in an infinite loop.
         Hence, self.outListModel.updating is used as a global flag to protect this from happening.
        """

        indexes = self.outputList.selectedIndexes()  # read selection from Output List
        if indexes and not self.outListModel.updating:
            spirit_logger.debug("Removing from Output List...")
            # Indexes is a list of a single item in single-select mode.
            self.outListModel.updating = True
            spirit_logger.debug("Set Updating flag to True")
            index = indexes[0]
            spirit_logger.debug(f"{self.outListModel.files[index.row()]} will be deleted")
            # WARNING: Deletion!
            self.outListModel.removeFile(self.outListModel.files[index.row()])
            spirit_logger.debug("Item deleted from Output List")
            self.outputList.clearSelection()  # Clear the selection (as it is no longer valid).
            spirit_logger.debug("Output List selection cleared")
            self.outListModel.updating = False
            spirit_logger.debug("Reset Updating flag back to False")

    def addAllToQueue(self):
        """
        Method to load the list of .txt files in Input List into the Output List

        Raises:
            A generic error
        """

        try:
            self.outListModel.files = self.inputListModel.files
            self.outListModel.layoutChanged.emit()  # refresh the list
        except:
            spirit_logger.error(f"Failed to assign list of Input to Output List")

    def removeAllFromQueue(self):
        """
        Clears the Output List

        """
        try:
            self.outListModel.files = []
            self.outListModel.layoutChanged.emit()  # refresh the list
        except:
            spirit_logger.error(f"Failed to clear Output List")

    def process(self):
        """
        Process .txt files!

        """
        advanced = self.advancedComboBox.currentText()
        queue = self.outListModel.files
        self.statusLabel.setText(constants.PROCESSING)
        # pass files and options to engine for processing
        main_engine = engine.Analysis(queue, advanced)
        main_engine.process()
        self.statusLabel.setText(constants.COMPLETED)
