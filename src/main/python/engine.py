"""
Core Engine for PacketPuller

Partially adapted from MaplePacketPuller, with addition of utility functions.
Contains utility functions and packet structure analysis methods.
"""
import os

from src.main.python import logger, constants
spirit_logger = logger.get_logger("main.engine")


# read list of files from Functions directory
def get_func_list():
	"""
	Fetches a list of .txt files from a predetermined directory

	Returns:
		A list of strings
	Raises:
		A generic error
	"""

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
	"""
	Manually obtain the root directory via unfolded-tails recursion

	Returns:
		parent: A string representing the path to the project root
	"""

	spirit_logger.debug("Obtaining project root...")
	parent = os.path.dirname(os.getcwd())   # main
	parent = os.path.dirname(parent)   # src
	parent = os.path.dirname(parent)   # Spirit-PacketPuller
	spirit_logger.debug(f"Project root: {parent}")
	return parent


def get_io_dir(io):
	"""
	Smart concatenation of path fragments to give the desired directory

	Args:
		io: Specify 'i' for input, and 'o' for output

	Returns:
		path: A string representing the path to either the input or output folder
	Raises:
		A generic error
	"""

	spirit_logger.debug("Locating IO directories")
	path = get_root_dir()
	if io == 'i':
		try:
			path = os.path.join(path, constants.FUNC_DIR)
		except:
			spirit_logger.error("os.path.join() failed to concatenate the arguments!")
	elif io == 'o':
		try:
			path = os.path.join(path, constants.FUNC_OUTPUT_DIR)
		except:
			spirit_logger.error("os.path.join() failed to concatenate the arguments!")
	else:
		spirit_logger.error("Specify a proper input!")
	return path
