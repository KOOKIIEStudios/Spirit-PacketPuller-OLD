"""
Core Engine for PacketPuller

Partially adapted from MaplePacketPuller, with addition of utility functions.
Contains utility functions and packet structure analysis methods.
Refer to the flowchart in MaplePacketPuller for idea of the analysis flow.
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


# Main Engine
class Analysis:
	GET_ALL_DECODES = False


	@staticmethod
	def get_func_name(txt_file_name):
		path = get_io_dir('i')
		try:
			path = os.path.join(path, txt_file_name)
			with open(path) as file:
				func_name = file.readline()
			return path, func_name
		except:
			spirit_logger.error("Failed to get function name from txt file!")

	def check_keyword_and_return(self, word):
		spirit_logger.debug("Checking for keywords...")
		for key in KEYWORDS:
			if key in word.lower():
				if key != "if" and key != "else":
					return KEYWORDS_PRINT[KEYWORDS.index(key)]
			elif key not in word.lower() and "decode" in word.lower() and self.GET_ALL_DECODES:
				return word # just in case our keywords array doesn't already have that Decode saved
		return ""

	@staticmethod
	def is_decode_func(func_name):
		for key in KEYWORDS:
			if key in func_name:
				return True
		return False

	@staticmethod
	def add_decode_to_list(keyword_list, word):
		for key in KEYWORDS:
			if key in word.lower():
				if key != "if" and key != "else":
					keyword_list.append(KEYWORDS_PRINT[KEYWORDS.index(key)])
		return keyword_list

	def check_keyword_and_print(self, word):
		for key in KEYWORDS:
			if key in word.lower():
				if key != "if" and key != "else":
					spirit_logger.debug(f"{KEYWORDS_PRINT[KEYWORDS.index(key)]}")
			# just incase our keywords array doesn't have that decode already set:
			elif key not in word.lower() and "decode" in word.lower() and self.GET_ALL_DECODES:
				spirit_logger.debug(word)
			return True
		return False

	def analyse_packet_structure(self, function):
		"""
			Pulls key words from the given function and writes them only showing Decodes in order
			function : String
		"""
		packet_struct = ""
		start_time = time.time()
		path, func_name = self.get_func_name(function)
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
				if KEYWORDS[5] in line or KEYWORDS[6] in line:
					# ^check if we are at an if / else statement
					if KEYWORDS[5] in line:
						if_or_else += "if " + self.check_keyword_and_return(line) + ":"
					if KEYWORDS[6] in line:
						if_or_else += "else:"
					check_next_line = file[arr_index + 1] == "  {\n"
					# ^check if its a non nested if
					if self.is_decode_func(file[arr_index + 1]):
						# if the if statement is a one liner condition, we have to check if that one line is a decode
						spirit_logger.debug(self.check_keyword_and_return(file[arr_index + 1]))
					if check_next_line:
						# if we are in the scope of an if, find when it ends
						i = 1
						while file[arr_index + i] != "  }\n":
							decodes_in_if = self.add_decode_to_list(decodes_in_if, file[arr_index + i])
							i += 1
					in_if_statement = check_next_line

				if len(decodes_in_if) > 0 and in_if_statement:
					spirit_logger.debug(if_or_else)
					packet_struct += if_or_else + "\n"
					for decode in decodes_in_if:
						spirit_logger.debug(f"  {decode}")
						packet_struct += "  " + decode + "\n"
				elif self.check_keyword_and_print(line):
					# if we aren't in an if statement, print out the decodes normally
					packet_struct += self.check_keyword_and_return(line) + "\n"

				arr_index += 1

			end_time = time.time()
			spirit_logger.info(f"\nFinished analysis in {end_time - start_time} seconds!")
			return packet_struct

	@staticmethod
	def write_func_output(path, packet_struct):
		"""
			Writes a txt file with the packet structure of the given IDA function
			packet_struct: String
		"""
		with open(path) as f:
			f.write(packet_struct)

	# Link to be called from ViewController
	def process(self, files, options):
		spirit_logger.info("Core analytical engine logic by Brandon Nguyen")
		spirit_logger.info("Adapted and re-implemented by: KOOKIIE Studios 2020")

		if options == constants.INHEADER:
			# do stuff
		elif options == constants.AGRESSIVE:
			self.GET_ALL_DECODES = True
		else:
			for file in files:
				packet_struct = self.analyse_packet_structure(files)
				spirit_logger.debug("Setting output path to write to...")
				path = get_io_dir('o')
				try:
					path = os.path.join(path, f"{files.upper()}out.txt")
				except:
					spirit_logger.error("os.path.join() failed to concatenate the arguments!")
				spirit_logger.debug(f"Saving down packet structure to {path} \n")
				self.write_func_output(path, packet_struct)  # write the txt file so we can beautify it
				# removes all the newlines from the txt file we just created
				packet_struct_arr = beautify(path)
