# Core Engine for PacketPuller
# Adapted from MaplePacketPuller
import os

from src.main.python import logger, constants
spirit_logger = logger.get_logger("main.engine")


# read list of files from Functions directory
def get_func_list():
	try:
		directory = get_io_dir('i')
	except:
		spirit_logger.error("Unknown error while getting IO directory!")
	spirit_logger.debug(f"Fetching list of files in following directory: {directory}")
	list_of_entries = []  # read contents of dir using os.scandir() from Python 3.6
	for num, entry in enumerate(sorted(os.scandir(directory), key=lambda e: e.name), start=1):
		# print all entries that are files
		if entry.is_file() and entry.name[-3:] == "txt":
			list_of_entries.append(entry.name[:-4])  # strip file extension via string splice
			spirit_logger.debug(f"{num}. {list_of_entries[num-1]}")
	return list_of_entries


def get_root_dir():
	parent = os.path.dirname(os.getcwd())   # main
	parent = os.path.dirname(parent)   # src
	parent = os.path.dirname(parent)   # Spirit-PacketPuller
	return parent


def get_io_dir(io):
	spirit_logger.debug("Locating IO directories")
	path = get_root_dir()
	if io == 'i':
		path = os.path.join(path, constants.FUNC_DIR)
	elif io == 'o':
		path = os.path.join(path, constants.FUNC_OUTPUT_DIR)
	else:
		spirit_logger.error("Path not found!")
	return path
