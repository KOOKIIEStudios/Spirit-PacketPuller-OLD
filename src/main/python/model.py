# Model Module
# Interface between data store and ViewController

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from src.main.python import logger, view, engine, constants
spirit_logger = logger.get_logger("main.model")


class InputListModel(QtCore.QAbstractListModel):
	def __init__(self, *args, files=None, **kwargs):
		super(InputListModel, self).__init__(*args, **kwargs)
		self.files = files or []  # defaults to empty list

	def data(self, index, role):  # required method for models
		if role == Qt.DisplayRole:
			text = self.files[index.row()]
			return text

	def rowCount(self, index):  # required method for models
		return len(self.files)



