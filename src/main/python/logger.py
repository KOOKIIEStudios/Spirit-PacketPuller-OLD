# Logger Module
# Business logic obtained from https://www.toptal.com/python/in-depth-python-logging
import logging
import sys
from logging.handlers import TimedRotatingFileHandler
from src.main.python import constants
FORMATTER = logging.Formatter(constants.FORMAT)


def get_console_handler():
	console_handler = logging.StreamHandler(sys.stdout)
	console_handler.setFormatter(FORMATTER)
	return console_handler


def get_file_handler():
	file_handler = TimedRotatingFileHandler(constants.LOG_FILE, when='midnight')
	file_handler.setFormatter(FORMATTER)
	return file_handler


class NullHandler(logging.Handler):
	def emit(self, record):
		pass


def get_logger(logger_name):
	logger = logging.getLogger(logger_name)
	logger.setLevel(logging.DEBUG)  # better to have too much log than not enough
	h = NullHandler()
	logger.addHandler(h)
	# with this pattern, it's rarely necessary to propagate the error up to parent
	logger.propagate = False
	return logger


def shutdown_logger():
	spirit_logger.info("Shutting down logger...")
	logging.shutdown()
