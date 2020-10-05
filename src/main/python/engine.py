"""
Core Engine for PacketPuller

Partially adapted from MaplePacketPuller, with addition of utility functions.
Contains utility functions and packet structure analysis methods.
"""
import os
import time

from src.main.python import logger, constants
from src.main.python.keywords import *
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

def get_func_name(txt_file_name):
	path = get_io_dir('i')
	try:
		path = os.path.join(path, txt_file_name)
		with open(path) as file:
			func_name = file.readline()
		return path, func_name
	except:
		spirit_logger.error("Failed to get function name from txt file!")

def analyse_packet_structure(function):
	"""
		Pulls key words from the given function and writes them only showing Decodes in order
		function : String
	"""
	packet_struct = ""
	start_time = time.time()
	path, func_name = get_func_name(function)
	spirit_logger.debug(f"Function Name: {func_name}")
	spirit_logger.debug(f"Obtained from: {path}")

	in_if_statement = False
	spirit_logger.debug(f"Instantiate in_if_statement as: False")

	arr_index = 0 # file starts at 0 cause its an array
	packet_struct += func_name
	with open(path) as f:
		file = f.readlines()
		for line in file:
			decodes_in_if = []
			if_or_else = ""
			# It would prob be easier to print the line like it is in the txt file as it is already spaced
			if KEYWORDS[5] in line or KEYWORDS[6] in line: # check if we are at an if / else statement
				if KEYWORDS[5] in line:
					if_or_else += "if " + check_keyword_and_return(line) + ":"
				if KEYWORDS[6] in line:
					if_or_else += "else:"
				check_next_line = file[arr_index + 1] == "  {\n" # check if its a non nested if
				if is_decode_func(file[arr_index + 1]): # if the if statement is a one liner condition, we have to check if that one line is a decode
					spirit_logger.debug(check_keyword_and_return(file[arr_index + 1]))
				if check_next_line: # if we are in the scope of an if, find when it ends
					i = 1
					while file[arr_index + i] != "  }\n":
						decodes_in_if = add_decode_to_list(decodes_in_if, file[arr_index + i])
						i += 1
				in_if_statement = check_next_line

			if len(decodes_in_if) > 0 and in_if_statement:
				spirit_logger.debug(if_or_else)
				packet_struct += if_or_else + "\n"
				for decode in decodes_in_if:
					spirit_logger.debug(f"  {decode}")
					packet_struct += "  " + decode + "\n"
			elif check_keyword_and_print(line): # if we aren't in an if statement print out the decodes normally
				packet_struct += check_keyword_and_return(line) + "\n"

			arr_index += 1

# Main script sequence for engine
def main(files, options):
	spirit_logger.info("Core analytical engine logic by Brandon Nguyen")
	spirit_logger.info("Adapted and re-implemented by: KOOKIIE Studios 2020")
	if options == constants.INHEADER:
		# do stuff
	elif options == constants.AGRESSIVE:
		# do stuff
	else:
		for file in files:
			packet_struct = analyse_packet_structure(files)
			# do stuff
