# Model Module
# Interface between data store and ViewController

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal
import logger
spirit_logger = logger.get_logger("main.model")


class InputListModel(QtCore.QAbstractListModel):
	# Override selectionChanged to be more like itemSelectionChanged in QListWidget
	itemSelectionChanged = pyqtSignal()

	def selectionChanged(self, selected, deselected):
		super(InputListModel, self).selectionChanged(selected, deselected)
		self.itemSelectionChanged.emit()

	def __init__(self, *args, files=None, **kwargs):
		super(InputListModel, self).__init__(*args, **kwargs)
		self.files = files or []  # defaults to empty list

	def data(self, index, role):  # required method for models
		if role == Qt.DisplayRole:
			text = self.files[index.row()]
			return text

	def rowCount(self, index):  # required method for models
		return len(self.files)


class OutputListModel(QtCore.QAbstractListModel):
	# Override selectionChanged to be more like itemSelectionChanged in QListWidget
	itemSelectionChanged = pyqtSignal()

	def selectionChanged(self, selected, deselected):
		super(OutputListModel, self).selectionChanged(selected, deselected)

	def __init__(self, *args, files=None, **kwargs):
		super(OutputListModel, self).__init__(*args, **kwargs)
		self.files = files or []  # defaults to empty list
		self.updating = False

	def data(self, index, role):  # required method for models
		if role == Qt.DisplayRole:
			text = self.files[index.row()]
			return text

	def rowCount(self, index):  # required method for models
		return len(self.files)

	def addFile(self, file):  # Add single file to list
		if file not in self.files:
			index = len(self.files)
			self.beginInsertRows(QtCore.QModelIndex(), index, index)
			self.files.append(file)
			spirit_logger.debug(f"Item {file} added to the Input List")
			self.files.sort()
			spirit_logger.debug("Input List sorted")
			self.endInsertRows()
		else:
			spirit_logger.debug(f"Duplicate found. {file} not added.")

	def removeFile(self, file):  # Remove single file from list
		size = len(self.files)
		spirit_logger.debug(f"Size is {size}")
		for row in range(0, size):
			spirit_logger.debug(f"Row is {row}")
			if self.files[row] == file:
				spirit_logger.debug(f"files[row]: {self.files[row]} , File: {file}")
				self.beginRemoveRows(QtCore.QModelIndex(), row, row)
				spirit_logger.debug("Begin remove...")
				self.files.pop(row)
				spirit_logger.debug("Removed!!")
				self.endRemoveRows()
				break
