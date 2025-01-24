#!/usr/bin/env python3

import os
import sys
import psutil
import math
import argparse
from typing import List, Union, Tuple
from pathlib import Path
import concurrent.futures
from functools import partial, wraps
from enum import Enum

import copy
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List
import re

import json



pixelFont = {
	'blocks' : [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':' ],
	'spaces' : [ 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?' ],
}

# This is the version of the script
scriptVersion = '1.0'

PES_MAX_LENGTH = 2028

minimum_milliseconds_between_lines = 24
subtitle_maximum_display_milliseconds = 15 * 1000


# THESE FUNCTIONS ARE COPIED FROM VCRLIBRARY.PY
# THESE FUNCTIONS ARE COPIED FROM VCRLIBRARY.PY

# Colors to use for the text output
class colors:
	black		=	"\033[0;30m"
	darkRed		=	"\033[0;31m"
	darkGreen	=	"\033[0;32m"
	brown		=	"\033[0;33m"
	darkBlue	=	"\033[0;34m"
	purple		=	"\033[0;35m"
	darkCyan	=	"\033[0;36m"
	lightGray	=	"\033[0;37m"
	darkGray	=	"\033[1;30m"
	red			=	"\033[1;31m"
	green		=	"\033[1;32m"
	yellow		=	"\033[1;33m"
	blue		=	"\033[1;34m"
	pink		=	"\033[1;35m"
	cyan		=	"\033[1;36m"
	white		=	"\033[1;37m"
	none		=	"\033[0m"
	bold		=	'\033[1m'
	underline	=	'\033[4m'

# Used to differentiate different errors and different steps in the debug trace
debugColors = [
	colors.red,
	colors.blue,
	colors.brown,
	colors.cyan,
	colors.yellow,
	colors.purple,
	colors.green
]

sizeColors = [
	colors.purple,
	colors.green,
	colors.blue,
	colors.yellow,
	colors.red,
	colors.darkRed,
	colors.white
]

# Special strings to use for cursor control
class cursorControl:
	up = '\033[1A'
	eraseLine = "\r" + '\033[K'
	eraseRemaining = '\033[K'
	erasePreviousLine = '\033[1A' + "\r" + '\033[K' + '\033[1A'
	eraseNextLine = "\r" + '\033[K' + '\033[1A'
def clamp(value, input2, input3):
	if input2 > input3:
		inputMax = input2
		inputMin = input3
	else:
		inputMax = input3
		inputMin = input2

	if value > inputMax:
		return inputMax
	if value < inputMin:
		return inputMin
	return value

def printDebug(*args):
	global debugColors

	messages = args
	i = 0
	while i < len(messages):
		print(debugColors[i % len(debugColors)])
		print(messages[i])
		print(colors.none)
		i += 1

def printAndLog(inputStuff = '', logFile = ''):
	for item in inputStuff:
		print(item)

def prepCommandToPrint(command):
	output = ''

	temp = copy.deepcopy(command)

	triggerQuotes = [ ' ', '|', '[', ']' ]

	for i in range(len(temp)):
		for trigger in triggerQuotes:
			match = False
			if temp[i].find(trigger) >= 0:
				match = True
				temp[i] = '"' + temp[i].replace('"', '\\' + trigger) + '"'
				break

	output = ' '.join(temp)

	return output

def printCommand(command):
	output = ''
	printDebug(prepCommandToPrint(command))

palettePrintCount = 0
paletteColors = [ colors.white, colors.yellow, colors.blue, colors.green, colors.red ]
def printPalette(palette):
	global palettePrintCount

	temp = []
	for i in range(len(palette)):
		if type(palette[i]) is dict:
			temp.append(normalizedRgbToHex(palette[i]))
		else:
			temp.append(palette[i])
	print(paletteColors[palettePrintCount % len(paletteColors)], temp, colors.none)
	palettePrintCount += 1

def printSubtitleToConsole(imageData):
	# This function is used to debug the image arrays after decoding

	colors = []

	print()
	for y in range(len(imageData)):
		if type(imageData[y]) is int:
			print()
			continue
		row = ''
		for x in range(len(imageData[y])):
			if type(imageData[y][x]) is int:
				row += ' '
				continue
			match = -1
			for c in range(len(colors)):
				if areColorsTheSame(imageData[y][x], colors[c]):
					match = c
					break
			if match == -1:
				match = 0
				colors.append(imageData[y][x])
			row += str(match)
		print(row)
	print()

def displayProgress(percentComplete, pass_number = 1, pos = 0, total = -1):
	totalPasses = 2

	offset = 100 / totalPasses * (pass_number - 1)

	percentComplete = float(round((percentComplete / totalPasses + offset), 1))

	index = ''
	if total > 0:
		numLength = len(str(total)) + 2 # Add space, this helps with parsing colors
		index = colors.yellow + leadingSpaces(pos, numLength) + colors.none + '  /' + colors.red + leadingSpaces(total, numLength)
	sys.stdout.flush()
	print(cursorControl.up + cursorControl.eraseRemaining + colors.blue + 'Pass: ' + colors.yellow + str(pass_number) + colors.none + ' / ' + colors.red + str(totalPasses) + '  ' + colors.white + '  ' + leadingSpaces(percentComplete, 4) + '%    ' + index + colors.none)
	sys.stdout.flush()

def padHexColor(hexColor):
	while 2 - len(hexColor) > 0:
		hexColor = '0' + hexColor
	return hexColor

def leadingSpaces(inputNumber, places):
	output = str(inputNumber)
	if isinstance(inputNumber, str):
		placesToAdd = places - len(str(inputNumber))
	else:
		placesToAdd = places - len(str(math.floor(inputNumber)))

	if placesToAdd > 0:
		return ' ' * placesToAdd + output
	else:
		return output

def readFile(filename):
	with open(filename, 'r') as f:
		contents = f.read()
	return contents

def readJSONFile(filename):
	final = {}
	with open(filename, 'r') as f:
		data = f.read()
		final = json.loads(data)
	return final

def setDuration(inputData):
	return [
		# This value is given in microseconds. The ENTIRE VIDEO must be analyzed
#		'-analyzeduration', str(int(inputData['maxDuration'] * 1000000)),
		'-analyzeduration', str(99999999 * 1000000),	# Duration has a chance of being reported wrong. Force an insane value here, make FFmpeg check *everything*

		# This value is given in bytes
		'-probesize', str(int(inputData['fileSize']))
	]

def idxToRGB(color):
	# Apparently IDX files are calculated wrong and are neither RGB nor YUV. What a shock, another bug.
	return YUVStringToRGBString(vobsub_rgb_to_yuv(int(color, 16)))

def av_clip_uint8(value):
	return max(0, min(255, value))

def vobsub_rgb_to_yuv(rgb):
	# This function was modeled after mplayer's source code. Apparently IDX files are calculated wrong
	# and are neither RGB nor YUV. What a shock, another bug.

	r = (rgb >> 16) & 0xff
	g = (rgb >> 8) & 0xff
	b = rgb & 0xff

	y = (0.299 * r + 0.587 * g + 0.114 * b) * 219 / 255 + 16.5
	u = (-0.16874 * r - 0.33126 * g + 0.5 * b) * 224 / 255 + 128.5
	v = (0.5 * r - 0.41869 * g - 0.08131 * b) * 224 / 255 + 128.5

	return intColorToHexColor(int(y) << 16 | int(u) << 8 | int(v))

def normalizedColorToHexColor(color):
	return intColorToHexColor(int(color * 255))

def intColorToHexColor(color):
	output = intToHex(color)
	if len(output) < 2:
		output = '0' + output
	return output

def intColorToAssColor(colorList):
	outputColors = []

	while len(colorList) < 4:
		colorList.append(255)

	for i in range(3):
		outputColors.append(intColorToHexColor(colorList[i]).upper())

	# Alphas are inverted!
	outputColors.append(intColorToHexColor(255-colorList[3]).upper())

	outputColors.reverse()

	if len(colorList) == 4:
		# AABBGGRR
		return '&H' + ''.join(outputColors)
	else:
		# BBGGRR
		return '&H' + ''.join(outputColors)

def intToHex(intValue):
	return hex(intValue).split('x').pop()

def YUVStringToRGBString(inputString):
	# This function takes a 6-digit hexadecimal value for YUV color and converts it to RGB
	output = ''
	tempColors = YUVToRGB(int(inputString[0:2], 16), int(inputString[2:4], 16), int(inputString[4:6], 16))

	i = 0
	while i < len(tempColors):
		tempColors[i] = hex(tempColors[i])
		tempColors[i] = tempColors[i].split('0x')[1]
		j = 2 - len(tempColors[i])
		while j > 0:
			tempColors[i] = '0' + tempColors[i]
			j -= 1
		i += 1

	return ''.join(tempColors)

def RGBStringToYUVString(inputString):
	# This function takes a 6-digit hexadecimal value for RGB color and converts it to YUV
	output = ''
	tempColors = RGBToYUV(int(inputString[0:2], 16), int(inputString[2:4], 16), int(inputString[4:6], 16))

	i = 0
	while i < len(tempColors):
		tempColors[i] = hex(tempColors[i])
		tempColors[i] = tempColors[i].split('0x')[1]
		j = 2 - len(tempColors[i])
		while j > 0:
			tempColors[i] = '0' + tempColors[i]
			j -= 1
		i += 1

	return ''.join(tempColors)

def YUVToRGB(y, u, v):
	r = y + 1.402 * (v - 128)
	g = y - 0.344136 * (u - 128) - 0.714136 * (v - 128)
	b = y + 1.772 * (u - 128)

	# Clamp values to the range [0, 255] and convert to integers
	r = max(0, min(255, int(r)))
	g = max(0, min(255, int(g)))
	b = max(0, min(255, int(b)))

	return [ r, g, b ]

def timeToSeconds(inputString, delimiter = ':'):
	time = 0

	if type(inputString) is str:
		inputString = inputString.strip()
		if len(inputString) > 0:
			inputString = inputString.split(delimiter)

			# Add seconds
			time += float(inputString.pop().strip())

			if len(inputString) > 0:
				# Add minutes
				time += int(inputString.pop().strip()) * 60

				if len(inputString) > 0:
					# Add hours
					time += int(inputString.pop().strip()) * 3600

					if len(inputString) > 0:
						# Add days
						time += int(inputString.pop().strip()) * 3600 * 24

						if len(inputString) > 0:
							# Add weeks
							time += int(inputString.pop().strip()) * 3600 * 24 * 7

							if len(inputString) > 0:
								# User is crazy. Ignore anything that remains.
								pass
	return time

def leadingZeroes(inputNumber, places):
	output = str(inputNumber)
	placesToAdd = places - len(str(math.floor(inputNumber)))
	if placesToAdd > 0:
		return '0' * placesToAdd + output
	else:
		return output

def secondsToTime(inputTime, decimalPrecision = 2):
	hours = str(math.floor(inputTime / 3600))
	minutes = leadingZeroes(math.floor(inputTime % 3600 / 60), 2)
	seconds = leadingZeroes(math.floor(inputTime % 60), 2)
	milliseconds = str(inputTime % 1) + '0'

	return hours + ':' + minutes + ':' + seconds + '.' + milliseconds[2:4]

def alignTimesToDecimalPoint(time):
	# time must be a STRING formatted as:  hh:mm:ss:ms

	time = time.strip()		# Eliminate trailing spaces, we won't need those here

	minLength = 12	# Number of characters to use for the time
	if ':' in time:
		tempTime = time.split(':')
		tempTime[0] = str(int(tempTime[0])) 	# Make sure any leading zeroes on the first number are gone, it's easier to read this way
		time = ':'.join(tempTime)
	else:
		time = str(float(time)) 	# Make sure any leading zeroes on the first number are gone, it's easier to read this way

	if '.' in time:
		tempTime = time.split('.')
		tempTime[1] = tempTime[1] + (' ' * (3 - len(tempTime[1])))
		time = '.'.join(tempTime)
	else:
		time += '    '	# No decimal point. Add 4 spaces

	time = (' ' * (minLength - len(time))) + time
	return time

# THESE FUNCTIONS ARE COPIED FROM VCRLIBRARY.PY
# THESE FUNCTIONS ARE COPIED FROM VCRLIBRARY.PY


@dataclass
class Rectangle:
	x: int = 0
	y: int = 0
	width: int = 0
	height: int = 0

@dataclass
class IdxParagraph:
	start_time: datetime
	file_position: int

def wrapper(method):
	@wraps(method)
	def wrapped(*args, **kwargs):
		r = method(*args, **kwargs)
		return r
		if isinstance(r, timedelta):
			return r
		else:
			return r
	return wrapped

class TimeDeltaMetaClass(type):
	def __new__(meta, classname, bases, class_dict):
		class_ = super().__new__(meta, classname, bases, class_dict)
		new_class_dict = {}
		for attribute_name in dir(class_):
			if attribute_name in ['__init__', '__new__', '__class__', '__dict__']:
				continue
			# if hasattr(attribute, '__call__'):
			# if type(attribute) == FunctionType:
				# attribute = wrapper(attribute)
			attribute = getattr(class_, attribute_name)
			setattr(class_, attribute_name,  wrapper(attribute))
			# new_class_dict[attributeName] = attribute
		# return super().__new__(meta, classname, bases, new_class_dict)
		return class_

def generateImageList(width, height, colorCount = 4):
	testOutput = colors.white + str(width) + '   ' +  str(height)

	output = []

	color = []
	while len(color) < colorCount:
		color.append(0)

	while len(output) < height:
		row = []
		while len(row) < width:
			row.append(color)
		output.append(row)

	return output

class SubPicture:
# Subtitle Picture - see http:#www.mpucoder.com/DVD/spu.html for more info
# http://sam.zoy.org/writings/dvd/subtitles/

	class DisplayControlCommand(Enum):
		ForcedStartDisplay = 0
		StartDisplay = 1
		StopDisplay = 2
		SetColor = 3
		SetContrast = 4
		SetDisplayArea = 5
		SetPixelDataAddress = 6
		ChangeColorAndContrast = 7
		End = 0xFF

	def __init__(
		self, data: bytes,
		start_display_control_sequence_table_address: int = None,
		pixel_data_address_offset: int = 0
	):
		"""
		For SP packet with DVD sub pictures
		:param: data: bytes content of the sub pack
		:param: start_display_control_sequence_table_address: Adress of the first control sequence in data
		:param: pixel_data_address_offset: Bitmap pixel data address offset
		"""
		self._data = data
		self.forced = False
		self.delay = timedelta()
		self.duration = 0
		self.sub_picture_data_size = get_endian_word(self._data, 0)
		self._pixel_data_address_offset = pixel_data_address_offset
		if start_display_control_sequence_table_address is None and pixel_data_address_offset is None:
			self._start_display_control_sequence_table_address = start_display_control_sequence_table_address
		else:
			self._start_display_control_sequence_table_address = get_endian_word(self._data, 2)
			self.sub_picture_data_size = len(self._data)
		self.parse_display_control_commands(False, None, None, False, False)

	def get_bitmap(
		self,
		color_lookup_table: list[list],
		background: list,
		pattern: list,
		emphasis1: list,
		emphasis2: list,
		use_custom_colors: bool,
		crop: bool = True
	):
		"""
		Generates the current subtitle image
		:param: color_lookup_table: The Color LookUp Table (CLUT), if null then only the four colors are used (should contain 16 elements if not null)
		:param: background: Background color
		:param: pattern: Color
		:param: emphasis1: Color
		:param: emphasis2: Color
		:param: use_custom_colors: Use custom colors instead of lookup table
		:param: crop: Crop result image

		:return: Subtitle image
		"""
		four_colors = [background, pattern, emphasis1, emphasis2]

		return self.parse_display_control_commands(True, color_lookup_table, copy.deepcopy(four_colors), use_custom_colors, crop)

	def parse_display_control_commands(
		self,
		create_bitmap: bool,
		color_look_up_table: list[list],
		four_colors: list[list],
		use_custom_colors: bool,
		crop: bool
	):
		self.image_display_area = Rectangle()
		bmp = None
		display_control_sequence_table_addresses = []
		image_top_field_data_address = 0
		image_bottom_field_data_address = 1
		bitmap_generated = False
		largest_delay = -999999
		display_control_sequence_table_address = self._start_display_control_sequence_table_address - self._pixel_data_address_offset
		last_display_control_sequence_table_address = 0
		display_control_sequence_table_addresses.append(display_control_sequence_table_address)
		command_index = 0

		delay = 0

		while (display_control_sequence_table_address > last_display_control_sequence_table_address
			and display_control_sequence_table_address + 1 < len(self._data) and command_index < len(self._data)):

			delay_before_execute = get_endian_word(self._data, display_control_sequence_table_address + self._pixel_data_address_offset)
			command_index = display_control_sequence_table_address + 4 + self._pixel_data_address_offset
			if (command_index >= len(self._data)):
				break ## invalid index

			command = self._data[command_index]
			number_of_commands = 0
			while command != SubPicture.DisplayControlCommand.End.value and number_of_commands < 1000 and command_index < len(self._data):
				number_of_commands += 1
				if command == SubPicture.DisplayControlCommand.ForcedStartDisplay.value: # 0
					self.forced = True
					command_index+=1
				elif command == SubPicture.DisplayControlCommand.StartDisplay.value: # 1
					command_index+=1
				elif command == SubPicture.DisplayControlCommand.StopDisplay.value: # 2
					self.delay = timedelta(milliseconds=(delay_before_execute << 10) / 90.0)
					# OLD CODE HERE
					#if create_bitmap and self.delay.total_seconds() / 1000 > largest_delay: # in case of more than one image, just use the one with the largest display time
					#	largest_delay = self.delay.total_seconds() / 1000
					if create_bitmap and self.delay.total_seconds() > largest_delay: # in case of more than one image, just use the one with the largest display time
						largest_delay = self.delay.total_seconds()
						# bmp?.Dispose() # Release the image memory
						bmp = self.generate_bitmap(self.image_display_area, image_top_field_data_address, image_bottom_field_data_address, four_colors, crop)
						bitmap_generated = True
					command_index+=1
				elif command == SubPicture.DisplayControlCommand.SetColor.value: # 3
					if color_look_up_table != None and type(four_colors) is list:
						imageColor = [self._data[command_index + 1], self._data[command_index + 2]]
						if not use_custom_colors:
							four_colors = SubPicture.set_color(four_colors, 3, imageColor[0] >> 4, color_look_up_table)
							four_colors = SubPicture.set_color(four_colors, 2, imageColor[0] & 0b00001111, color_look_up_table)
							four_colors = SubPicture.set_color(four_colors, 1, imageColor[1] >> 4, color_look_up_table)
							four_colors = SubPicture.set_color(four_colors, 0, imageColor[1] & 0b00001111, color_look_up_table)
					command_index += 3
				elif command == SubPicture.DisplayControlCommand.SetContrast.value: # 4
					if color_look_up_table != None and type(four_colors) is list:
						imageContrast = [self._data[command_index + 1], self._data[command_index + 2]]
						if imageContrast[0] + imageContrast[1] > 0:
							# Get an alpha value, normalized from 0 to 255
							alpha_colors = [ 255, 255, 255, 255 ]
							
							alpha_colors[3] = (((imageContrast[0] & 0xF0) >> 4) * 17)
							alpha_colors[2] = ((imageContrast[0] & 0b00001111) * 17)
							alpha_colors[1] = (((imageContrast[1] & 0xF0) >> 4) * 17)
							alpha_colors[0] = ((imageContrast[1] & 0b00001111) * 17)

							for c in range(len(alpha_colors)):
								if len(four_colors[c]) < 4:
									four_colors[c].append(alpha_colors[c])
								else:
									four_colors[c][3] = alpha_colors[c]
					command_index += 3
				elif command == SubPicture.DisplayControlCommand.SetDisplayArea.value: # 5
					if len(self._data) > command_index + 6 and self.image_display_area.width == 0 and self.image_display_area.height == 0:

						# Original code
						# THIS IS HERE JUST IN CASE MY CORRECTION IS WRONG. THIS METHOD IS BROKEN ON RANDOM SUBTITLES
						# ~ starting_x = (self._data[command_index + 1] << 8 | self._data[command_index + 2]) >> 4
						# ~ ending_x = (self._data[command_index + 2] & 0b00001111) << 8 | self._data[command_index + 3] + 1
						# ~ starting_y = (self._data[command_index + 4] << 8 | self._data[command_index + 5]) >> 4
						# ~ ending_y = (self._data[command_index + 5] & 0b00001111) << 8 | self._data[command_index + 6] + 1

						# My code
						# WHY WAS THERE A BITWISE_OR IN THE ORIGINAL CODE, IT MAKES NO SENSE, THESE ARE UNSIGNED INTs THAT NEED ADDED TOGETHER?????????
						starting_x = (int(self._data[command_index + 1] << 8) + int(self._data[command_index + 2])) >> 4
						ending_x = int((self._data[command_index + 2] & 0b00001111) << 8) + int(self._data[command_index + 3]) + 1
						starting_y = (int(self._data[command_index + 4] << 8) + int(self._data[command_index + 5])) >> 4
						ending_y = int((self._data[command_index + 5] & 0b00001111) << 8) + int(self._data[command_index + 6]) + 1

						self.image_display_area = Rectangle(starting_x, starting_y, ending_x - starting_x, ending_y - starting_y)
					command_index += 7
				elif command == SubPicture.DisplayControlCommand.SetPixelDataAddress.value: # 6
					image_top_field_data_address = get_endian_word(self._data, command_index + 1) + self._pixel_data_address_offset
					image_bottom_field_data_address = get_endian_word(self._data, command_index + 3) + self._pixel_data_address_offset
					command_index += 5
				elif command == SubPicture.DisplayControlCommand.ChangeColorAndContrast.value: # 7
					command_index += 1
					#int parameterAreaSize = (int)Helper.GetEndian(_data, command_index, 2)
					if command_index + 1 < len(self._data):
						parameter_area_size = self._data[command_index + 1] # this should be enough??? (no larger than 255 bytes)
						if (color_look_up_table is not None):
							# TODO: Set four_colors
							pass
						command_index += parameter_area_size
					else:
						command_index+=1
				else:
					command_index+=1
				if command_index >= len(self._data): # in case of bad files...
					break

				command = self._data[command_index]

			last_display_control_sequence_table_address = display_control_sequence_table_address
			if self._pixel_data_address_offset == -4:
				display_control_sequence_table_address = get_endian_word(self._data, command_index + 3)
			else:
				display_control_sequence_table_address = get_endian_word(self._data, display_control_sequence_table_address + 2)

		if create_bitmap and not bitmap_generated: # StopDisplay not needed (delay will be zero - should be just before start of next subtitle)
			bmp = self.generate_bitmap(self.image_display_area, image_top_field_data_address, image_bottom_field_data_address, four_colors, crop)

		# This is commented out because it interferes with some stuff. No idea how, don't care to figure it out right now
		# if bmp is not None:
			# bmp['duration'] = self.duration

		return bmp

	@staticmethod
	def set_color(
		four_colors: list[list],
		four_color_index: int,
		clut_index: int,
		color_look_up_table: list[list]
	) -> None:

		if clut_index >= 0 and clut_index < len(color_look_up_table) and four_color_index >= 0:
			four_colors[four_color_index] = copy.deepcopy(color_look_up_table[clut_index])
		return four_colors

	def generate_bitmap(
		self,
		image_display_area: Rectangle,
		image_top_field_data_address: int,
		image_bottom_field_data_address: int,
		four_colors: list[list],
		crop: bool
	):

		global alphaThreshold

		if image_display_area.width <= 0 and image_display_area.height <= 0:
			return False

		for c in range(len(four_colors)):
			if len(four_colors[c]) < 4:
				# No transparency value! Just give it 255
				four_colors[c].append(255)


		img = generateImageList(image_display_area.width, image_display_area.height, 4)	# This is a bit broken, some subtitles don't work right!


		img = self.generate_fast_bitmap(self._data, img, 0, image_top_field_data_address, four_colors)
		img = self.generate_fast_bitmap(self._data, img, 1, image_bottom_field_data_address, four_colors)


		# Start these in reverse! We'll correct them later.
		minY = len(img)
		maxY = 0
		minX = len(img[0])
		maxX = 0

		newImage = []

		# Reprocess and copy image to new array
		for y in range(len(img)):
			row = []
			# Rows
			hasContent = False
			for x in range(len(img[y])):
				# Columns
				if img[y][x][3] <= alphaThreshold:
					# Color is alpha! Knock it out.
					row.append(0)
					continue
				else:
					hasContent = True
					# Adjust X crop data
					if x < minX:
						minX = x
					if x > maxX:
						maxX = x
				row.append(img[y][x])
			if hasContent == False:
				newImage.append(0)
				continue
			else:
				newImage.append(copy.deepcopy(row))

				# Adjust Y crop data
				if y < minY:
					minY = y
				if y > maxY:
					maxY = y

		if crop == True:
			# Crop the image data
			newImage = newImage[minY:maxY + 1]

			for y in range(len(newImage)):
				if type(newImage[y]) is not list:
					# Line is alpha, do not change
					continue
				newImage[y] = newImage[y][minX:maxX + 1]

		xWidth = 0
		for row in newImage:
			if row == 0:
				continue
			if len(row) > xWidth:
				xWidth = len(row)

		parsedImage = {
			'imageData'		: newImage,
			'startTime'		: -1,
			'duration'		: round(self.delay.total_seconds(), 3), # Seconds
			'endTime'		: -1,
			'width'			: xWidth,
			'height'		: len(newImage),
			'marginTop'		: self.image_display_area.y + minY,
			'marginLeft'	: self.image_display_area.x + minX,
#			'marginRight'	: -1,
#			'marginBottom'	: -1,
		}

		return parsedImage

	@staticmethod
	def generate_fast_bitmap(
		data: bytes,
		img: list,
		startY: int,
		data_address: int,
		four_colors: list[list],
	) -> None:
		index = 0
		only_half = False
		y = startY
		x = 0
		img_height = len(img)
		img_width = len(img[0])

		while y < img_height and data_address + index + 2 < len(data):
			sup_index, run_length, color, only_half, rest_of_line = SubPicture.decode_rle(data_address + index, data, only_half)
			index += sup_index
			if rest_of_line:
				run_length = img_width - x

			for i in range(run_length):
				if x >= img_width - 1:
					# Last pixel in the row
					if y < img_height and x < img_width:
						img[y][x] = four_colors[color]

					if only_half:
						only_half = False
						index+=1
					x = 0
					y += 2	# Images are interlaced, so do every other line
					break
				if y < img_height:
					# All but the last pixel
					img[y][x] = four_colors[color]
				x += 1

		return img

	@staticmethod
	def decode_rle(
		index: int,
		data: bytes,
		only_half: bool
	) -> int:
		#Value	  Bits   n=length, c=color
		#1-3		4	  nncc			   (half a byte)
		#4-15	   8	  00nnnncc		   (one byte)
		#16-63	 12	  0000nnnnnncc	   (one and a half byte)
		#64-255	16	  000000nnnnnnnncc   (two bytes)
		# When reaching EndOfLine, index is byte aligned (skip 4 bits if necessary)
		rest_of_line = False
		b1 = data[index]
		b2 = data[index + 1]

		if only_half:
			b3 = data[index + 2]
			b1 = ((b1 & 0b00001111) << 4) | ((b2 & 0b11110000) >> 4)
			b2 = ((b2 & 0b00001111) << 4) | ((b3 & 0b11110000) >> 4)

		if b1 >> 2 == 0:
			run_length = (b1 << 6) | (b2 >> 2)
			color = b2 & 0b00000011
			if run_length == 0:
				# rest of line + skip 4 bits if Only half
				rest_of_line = True
				if only_half:
					only_half = False
					return 3, run_length, color, only_half, rest_of_line
			return 2, run_length, color, only_half, rest_of_line

		if b1 >> 4 == 0:
			run_length = (b1 << 2) | (b2 >> 6)
			color = (b2 & 0b00110000) >> 4
			if only_half:
				only_half = False
				return 2, run_length, color, only_half, rest_of_line
			only_half = True
			return 1, run_length, color, only_half, rest_of_line

		if b1 >> 6 == 0:
			run_length = b1 >> 2
			color = b1 & 0b00000011
			return 1, run_length, color, only_half, rest_of_line

		run_length = b1 >> 6
		color = (b1 & 0b00110000) >> 4

		if only_half:
			only_half = False
			return 1, run_length, color, only_half, rest_of_line
		only_half = True
		return 0, run_length, color, only_half, rest_of_line

class VobSubMergedPack: #IBinaryParagraphWithPosition
	global use_sub_timestamps

	def __init__(self, sub_picture_data: bytearray, presentation_time_stamp: timedelta, stream_id: int = False, idx_line = False):
		self.sub_picture = SubPicture(sub_picture_data)
		self.end_time = timedelta()

		if use_sub_timestamps == False or presentation_time_stamp == False:
			self.start_time = idx_line.start_time
		else:
			self.start_time = presentation_time_stamp

		self.stream_id = stream_id
		self.idx_line = idx_line

	def is_forced(self):
		return self.sub_picture.forced

	def get_bitmap(self):
#		print('-----------------------------')
#		print(self.idx_line.start_time)
#		print(self.presentation_time_stamp)
#		print('-----------------------------')
#
#		return self.sub_picture.get_bitmap(self.palette, Color("red"), Color("black"), Color("white"), Color("black"), False, True)

#		return self.sub_picture.get_bitmap(self.palette, Color("cyan"), Color("green"), Color("white"), Color("black"), False, True)
		return self.sub_picture.get_bitmap(self.palette, [0, 255, 255 ], [ 0, 255, 0 ], [ 255, 255, 255 ], [ 0, 0, 0 ], False, True)

#		return self.sub_picture.get_bitmap(self.palette, Color.Transparent, Color("black"), Color("white"), Color("black"), False, True)

	def get_position(self) -> Tuple:
		return self.sub_picture.image_display_area.x, self.sub_picture.image_display_area.y

def process_pack(id_pack: int, pack: VobSubMergedPack, folder_path: Path, palette: List[str]) -> Tuple[Path, str]:
	img = extract_subtitle_image_from_pack(pack, palette)

	img['startTime'] = round(timeToSeconds(str(pack.start_time)), 3)
	img['endTime'] = round(img['startTime'] + img['duration'], 3)

	return img

def create_subfile_text(pack_id, pack: VobSubMergedPack, image_path: Path):
	return f"{pack_id + 1}\n" + \
		f"{timeToSeconds(pack.start_time)} --> {timeToSeconds(pack.end_time)}\n" + \
		f"{image_path}\n\n"

def areColorsTheSame(color1, color2):
	# This function is intended to compare colors in the format of a list
	# [ r, g, b, a ]
	# Values are 0 to 255

	if len(color1) != len(color2):
		return False

	for i in range(len(color1)):
		if color1 != color2:
			return False

	return True

def convertPalette(palette):
	# Strip out unnecessary characters...
	for i in range(len(palette)):
		palette[i] = palette[i].strip('#').strip()
		palette[i] = [ int(palette[i][0:2], 16), int(palette[i][2:4], 16), int(palette[i][4:6], 16) ]

	return palette

def extract_subtitle_image_from_pack(pack: VobSubMergedPack, palette: List[str]):
	pack.palette = palette

	img = pack.get_bitmap()

	return img

def ssaSubpictureHeader(videoCroppedWidth, videoCroppedHeight):
	global scriptVersion
	return """[Script Info]
; Script generated by Sub2Ass.py version """ + scriptVersion + """
ScriptType: v4.00+
PlayResX: """ + str(videoCroppedWidth) + """
PlayResY: """ + str(videoCroppedHeight) + """
ScaledBorderAndShadow: no
YCbCr Matrix: None"""

def checkPixels(pixel1, pixel2):
	if type(pixel1) is list and type(pixel2) is list:
		if len(pixel1) != len(pixel2):
			return False
		for i in range(len(pixel1)):
			if pixel1[i] != pixel2[i]:
				return False
	return True

def getRepeatPixelCount(pixelRow, start, charList):
	# charList is the list of 'blocks' or 'spaces' in pixelFont we are using
	count = 1
	pos = start
	while pos < len(pixelRow) and count <= len(charList):
		if type(pixelRow[pos]) is not type(pixelRow[start]):
			break
		if type(pixelRow[pos]) is list:
			if not areSubpictureColorsTheSame(pixelRow[start], pixelRow[pos]):
				break

		count += 1
		pos += 1
	return count - 1

def areSubpictureColorsTheSame(color1, color2):
	if type(color1) != type(color2):
		return False
	if type(color1) is not list:
		return False
	for i in range(3):
		if color1[i] != color2[i]:
			return False
	return True

def findColor(colorList, foundColor):
	i = 0
	while i < len(colorList):
		if areSubpictureColorsTheSame(colorList[i], foundColor):
			return i
		i += 1
	colorList.append(foundColor)
	return i

def imageToass(imageData, colorList):
	currentColor = []
	emptyLines = 0	# Using this keeps gaps to a minimum, and also knocks out tailing empty lines

	# This is just used as a pointer to make a few things cleaner below
	charList = pixelFont['spaces']

	foundData = False

	output = ''
	if type(imageData) is not list:
		return ''
	for y in range(len(imageData)):
		if type(imageData[y]) is not list:
			if foundData == False:
				# We haven't even found a single pixel yet, there's no point in having blank lines at the start!
				continue
			# Row is empty, skip
			if maxEmptyLines < 0 or emptyLines < maxEmptyLines:
				emptyLines += 1
			continue

		if foundData == True:
			# Add a newline to all but the first line
			output += '\\N'
			emptyLines = max(0, emptyLines - 1)
		if emptyLines > 0:
			while emptyLines > 0:
				output += pixelFont['spaces'][0] + '\\N'
				emptyLines -= 1

		foundData = True
		emptyLines = 0

		x = 0
		while x < len(imageData[y]):
			currentPixel = imageData[y][x]
			if type(currentPixel) is not list or currentPixel[3] < alphaThreshold:
				# Transparent pixel(s)
				charList = pixelFont['spaces']
			else:
				# Visible pixel(s)
				charList = pixelFont['blocks']

				# Check to see if we need to change color
				if len(currentColor) == 0 or not areSubpictureColorsTheSame(currentColor, currentPixel):
					# Need to add color info!
					styleIndex = findColor(colorList, currentPixel)
					if styleIndex == 0:
						if len(currentColor) == 0 and areSubpictureColorsTheSame(colorList[0], currentPixel):
							# This is the first color. Leave it blank, it will be the default style color anyway
							pass
						else:
							# New color is just the default color
							output += '{\\r}'
					else:
						output += '{\\r' + intToHex(styleIndex) + '}'
#						output += '{\\c&H' + intColorToHexColor(currentPixel[2]) + intColorToHexColor(currentPixel[1]) + intColorToHexColor(currentPixel[0]) + '&,\\3c&H' + intColorToHexColor(currentPixel[2]) + intColorToHexColor(currentPixel[1]) + intColorToHexColor(currentPixel[0]) + '&}'
					currentColor = copy.deepcopy(currentPixel[0:3])

			repetitions = getRepeatPixelCount(imageData[y], x, charList)
			output += charList[repetitions - 1]
			x += repetitions

	return { 'colorList' : colorList, 'imageData' : output }

def areImageBitmapsTheSame(image1, image2):
	if len(image1) != len(image2):
		return False

	for y in range(len(image1)):

		if type(image1[y]) is not type(image2[y]):
			return False
		if type(image1[y]) is not list:
			if type(image2[y]) is not list:
				continue
			else:
				return False

		if len(image1[y]) != len(image2[y]):
			return False
		for x in range(len(image1)):

			if type(image1[y][x]) is not type(image2[y][x]):
				return False
			if type(image1[y][x]) is not list:
				if type(image2[y][x]) is not list:
					continue
				else:
					return False

			if len(image1[y][x]) != len(image2[y][x]):
				return False
			for c in range(len(image1[y][x])):
				if image1[y][x][c] != image2[y][x][c]:
					return False

	return True

def multiprocess(_vob_sub_merged_pack_list, outputFilePath, _palette, n_jobs, timeAdjustmentFactor, timeOffset, videoWidth, videoHeight, videoCropData):
	global alignmentThreshold
	global alpha_threshold

	global maxSubtitleDuration
	global imageHeightThreshold
	global imageWidthThreshold

	global resolutionScale
	global fontHeight
	global minMargin

	image_paths = []
	subfile_texts = []
	multi_process_pack = partial(process_pack, folder_path=outputFilePath, palette=_palette)
	num_packs = len(_vob_sub_merged_pack_list)


	# Parse the crop data into something useful!
	videoCropData = videoCropData.split(':')
	for c in range(len(videoCropData)):
		videoCropData[c] = int(videoCropData[c])

	# videoCropData[0] = total width
	# videoCropData[1] = total height
	# videoCropData[2] = x position
	# videoCropData[3] = y position

	cropLeft = videoCropData[2]
	cropRight = videoWidth - videoCropData[2] - videoCropData[0]
	cropTop = videoCropData[3]
	cropBottom = videoHeight - videoCropData[3] - videoCropData[1]

	alignmentTotals = {
		'1' : 0,
		'2' : 0,
		'3' : 0,
		'4' : 0,
		'5' : 0,
		'6' : 0,
		'7' : 0,
		'8' : 0,
		'9' : 0
	}

	mostCommonAlignment = 2	# Placeholder value, we will fix it later

	colorList = []

	outputSubtitles = []

	# If there is already a .ass file, delete it
	if os.path.exists(outputFilePath):
		os.remove(outputFilePath)

	with open(outputFilePath, 'w') as subFile:
		subFile.write(ssaSubpictureHeader(int(videoCropData[0] * resolutionScale), int(videoCropData[1] * resolutionScale)))

		pixelHeightsPerLine = []

		finishedCount = 0
		previousPercentage = 0

		with concurrent.futures.ProcessPoolExecutor(n_jobs) as executor:
			subtitleList = []
			print()
			displayProgress(0, 1, 0, len(range(num_packs)))

			results = []
			for result in executor.map(
					multi_process_pack, range(num_packs), _vob_sub_merged_pack_list
				):

				results.append(result)

				finishedCount += 1
				percentage = round(finishedCount / num_packs * 100, 1)
				if percentage != previousPercentage:
					displayProgress(percentage, 1, finishedCount, len(range(num_packs)))
					previousPercentage = percentage

			previousPercentage = 0
			maxHeight = 0
			maxWidth = 0

			results.sort(key=lambda results: results['startTime'])

			displayProgress(0, 2, 0, len(range(num_packs)))

			i = -1
			while i + 1 < len(results):
				i += 1

				percentage = round(i / len(results) * 100, 1)
				if percentage != previousPercentage:
					displayProgress(percentage, 2, i, len(results))
					previousPercentage = percentage

				result = results[i]

				if result == False:
					# For some reason, the image was blank. Continue on, nothing to see here!
					continue

				# Finish calculating the remaining data we need
				result['frameWidth']	= videoWidth
				result['frameHeight']	= videoHeight
				result['marginRight']	= videoWidth - result['marginLeft'] - result['width']
				result['marginBottom']	= videoHeight - result['marginTop'] - result['height']

				result['alignment'] = 5
				if result['marginBottom'] / videoHeight < alignmentThreshold or result['marginTop'] - result['marginBottom'] > alignmentThreshold * videoHeight:
					result['alignment'] -= 3
				elif result['marginTop'] / videoHeight < alignmentThreshold or result['marginTop'] - result['marginBottom'] < alignmentThreshold * videoHeight * -1:
					result['alignment'] += 3
				if result['marginLeft'] / videoWidth < alignmentThreshold and result['marginLeft'] - result['marginRight'] > alignmentThreshold * videoWidth:
					result['alignment'] -= 1
				elif result['marginRight'] / videoWidth  < alignmentThreshold and result['marginLeft'] - result['marginRight'] < alignmentThreshold * videoWidth * -1:
					result['alignment'] += 1

				if result['alignment'] > 3 and result['alignment'] < 7:
					# If the subtitle is in the vertical center row, drop it down to the bottom row. We don't need it in the middle of the video!
					result['alignment'] = result['alignment'] - 3

				alignmentTotals[str(result['alignment'])] += 1

				addSubtitle = True

				if result['startTime'] == -1 or result['endTime'] == -1:
					# -1 means the time is invalid. Skip on ahead, there's no way to use this subtitle
					addSubtitle = False

					match = False
					while i + 1 < len(results) and result['endTime'] + 0.1 > results[i + 1]['startTime'] and areImageBitmapsTheSame(result['imageData'], results[i + 1]['imageData']):
						# Subtitle is followed by one or more duplicates! Increase the index to ignore the duplicates
						match = True
						i += 1
					if match == True:
						result['endTime'] = results[i]['endTime']

				if result['startTime'] + 0.075 >= result['endTime']:
					# Duration is too short or invalid!
					if i < len(results) - 1:
						# If there is no duration data, use the next subtitle start time and hope it works well enough
						result['endTime'] = results[i + 1]['startTime']
					else:
						# This is the last subtitle in the video. Just make it maxSubtitleDuration seconds long, since we have no idea otherwise
						result['endTime'] = result['startTime'] + maxSubtitleDuration

				subWidth = 0
				for a in range(len(result['imageData'])):
					if type(result['imageData'][a]) is list:
						subWidth = max(subWidth, len(result['imageData'][a]))
						break
				if len(result['imageData']) < imageHeightThreshold and subWidth < imageWidthThreshold:
					# Image is too small. Probably just a placeholder for removing a subtitle. Ignore it
					continue

				if result['startTime'] + maxSubtitleDuration < result['endTime']:
					# Restrict maximum subtitle length to maxSubtitleDuration seconds, nothing should be longer than that
					result['endTime'] = result['startTime'] + maxSubtitleDuration

				if i < len(results) - 1:
					# If this subtitle overlaps the next one, terminate it at that time
					if result['endTime'] >= results[i + 1]['startTime']:
						result['endTime'] = results[i + 1]['startTime']

				if addSubtitle == True:
					# Do some extra calculating to use for dynamic sizing
					currentLineHeight = 0
					foundLine = False
					for image in result['imageData']:
						if type(image) is list:
							maxWidth = max(maxWidth, len(image))	# Get the width to use in maxWidth
							if foundLine == True:
								currentLineHeight += 1
							else:
								foundLine = True
								currentLineHeight = 1
						else:
							if foundLine == True:
								if currentLineHeight >= imageHeightThreshold:	# MAKE SURE to use imageHeightThreshold to discard anything too small
									pixelHeightsPerLine.append(currentLineHeight)
								foundLine = False
					if foundLine == True and currentLineHeight >= imageHeightThreshold:
						pixelHeightsPerLine.append(currentLineHeight)
					pixelHeightsPerLine.append(currentLineHeight)


					alignment = ''
					if keepPosition == True:
						if result['alignment'] != mostCommonAlignment:
							alignment = '{\\an' + str(result['alignment']) + '}'

					position = ''
					parsedEntry = imageToass(result['imageData'], colorList)

					colorList = parsedEntry['colorList']

					outputSubtitles.append({
						'startTime'	: secondsToTime(max(0, (result['startTime'] * timeAdjustmentFactor) + (timeOffset))),
						'endTime'	: secondsToTime(max(0, (result['endTime']  *  timeAdjustmentFactor) + (timeOffset))),
						'text'		: alignment + position + parsedEntry['imageData'],
					})

					# This has to be done here, because we cut out dead space between lines
					maxHeight = max(maxHeight, parsedEntry['imageData'].count('\\N') + 1)

			displayProgress(100, 2, len(results), len(results))

		# Calculate the font size! Try to get as close to the user's desired value without truncating anything
		averageLineHeight = 0
		for l in range(len(pixelHeightsPerLine)):
			averageLineHeight += pixelHeightsPerLine[l]
		averageLineHeight /= len(pixelHeightsPerLine)

		# Truncate this to one decimal point
		averageLineHeight = int(averageLineHeight * 10) / 10

		fontSize = fontHeight / averageLineHeight

		# Set the maximum font size to a size that stays within the video boundaries
		fontSize = min((videoCropData[0] - (minMargin * 2)) / maxWidth, fontSize)	# Remember to include Right/Left margins
		fontSize = min((videoCropData[1] - minMargin) / maxHeight, fontSize)	# Remember to include bottom margin, there is no top margin

		# Truncate to three decimal points
		fontSize = int(fontSize * 1000) / 1000

		# Add the color styles
		subFile.write('\n\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding')
		for c in range(len(colorList)):
			newStyle = []

			newStyle.append(str(c))	# Style name
			newStyle.append(fontName)	# Font name
			newStyle.append(str(fontSize * resolutionScale))	# Font size
			newStyle.append(intColorToAssColor(colorList[c]))	# Primary Color
			newStyle.append(intColorToAssColor(colorList[c]))	# Secondary Color
			newStyle.append(intColorToAssColor(colorList[c]))	# Outline Color
#			newStyle.append(intColorToAssColor([ 0, 0, 0, 207 ]))	# Back Color	# I THINK THE SLIGHT TRANSPARENCY IS CAUSING SOME LAG ON MOBILE DEVICES
			newStyle.append(intColorToAssColor([ 0, 0, 0, 255 ]))	# Back Color
			newStyle.append('0')	# Bold
			newStyle.append('0')	# Italic
			newStyle.append('0')	# Underline
			newStyle.append('0')	# Strikeout
			newStyle.append('100')	# Scale X
			newStyle.append('100')	# Scale Y
			newStyle.append('0')	# Spacing
			newStyle.append('0')	# Angle
			newStyle.append('1')	# Border Style
			newStyle.append('0.05')	# Outline -- This value prevents lines from showing up between pixels, DO NOT REMOVE
			newStyle.append(str(shadowSize))	# Shadow
			newStyle.append(str(mostCommonAlignment))	# Alignment
			newStyle.append(str(minMargin))	# MarginL
			newStyle.append(str(minMargin))	# Margin R
			newStyle.append(str(minMargin))	# Margin V
			newStyle.append('1')	# Encoding

			subFile.write('\nStyle: ' + ','.join(newStyle))

		# Add the events
		subFile.write('\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text')
		for entry in outputSubtitles:
			subFile.write('\nDialogue: 0,' + entry['startTime'] + ',' + entry['endTime'] + ',0,,0,0,0,,' + entry['text'])

	print(cursorControl.up + cursorControl.eraseRemaining + colors.white + 'Finished!\n\n' + colors.none + 'Wrote: ' + colors.blue + outputFilePath + '\n\n' + colors.red + 'Remember to attach the font file for ' + colors.white + fontName + colors.red + ' inside your final MKV file!\n' + colors.none)

	return True

def is_mpeg2_pack_header(buffer: bytearray) -> bool:
	return len(buffer) >= 4 \
			and buffer[0] == 0 \
			and buffer[1] == 0 \
			and buffer[2] == 1 \
			and buffer[3] == 0xba; # 0xba == 186 - MPEG-2 Pack Header

def is_private_stream1(buffer: bytearray, index: int) -> bool:
	return len(buffer) >= index + 4 \
			and buffer[index + 0] == 0 \
			and buffer[index + 1] == 0 \
			and buffer[index + 2] == 1 \
			and buffer[index + 3] == 0xbd; # 0xbd == 189 - MPEG-2 Private stream 1 (non MPEG audio, subpictures)

def is_private_stream2(buffer: bytearray, index: int) -> bool:
	return len(buffer) >= index + 4 \
			and buffer[index + 0] == 0 \
			and buffer[index + 1] == 0 \
			and buffer[index + 2] == 1 \
			and buffer[index + 3] == 0xbf; # 0xbf == 191 - MPEG-2 Private stream 2

def is_subtitle_pack(buffer: bytearray) -> bool:
	if is_mpeg2_pack_header(buffer) and is_private_stream1(buffer, Mpeg2Header.LENGTH):
		pesHeader_data_length = buffer[Mpeg2Header.LENGTH + 8]
		streamId = buffer[Mpeg2Header.LENGTH + 8 + 1 + pesHeader_data_length]

		return streamId >= 0x20 and streamId <= 0x3f # Subtitle IDs allowed (or x3f to x40?)
	return False

class Mpeg2Header:
	#  <summary>
	#  http://www.mpucoder.com/DVD/packhdr.html
	#  </summary>
	LENGTH = 14

	def __init__(self, buffer: bytes):

		self.start_code = get_endian(buffer, 0, 3)
		self.pack_identifier = buffer[3]
		self.program_mux_rate = get_endian(buffer, 10, 3) >> 2
		self.pack_stuffing_length = buffer[13] & 0b00000111

class PacketizedElementaryStream:
	HEADER_LENGTH: int = 6

	def __init__(self, buffer: bytearray, index: int):
		self.buffer = buffer
		self.start_code = get_endian(buffer, index, 3)
		self.stream_id = buffer[index + 3]
		self.length = get_endian_word(buffer, index + 4)

		self.scrambling_control = (buffer[index + 6] >> 4) & 0b00000011
		self.priority = buffer[index + 6] & 0b00001000
		self.data_alignment_indicator = buffer[index + 6] & 0b00000100
		self.copyright = buffer[index + 6] & 0b00000010
		self.original_or_copy = buffer[index + 6] & 0b00000001
		self.presentation_timestamp_decode_timestamp_flags = buffer[index + 7] >> 6
		self.elementary_stream_clock_reference_flag = buffer[index + 7] & 0b00100000
		self.es_rate_flag = buffer[index + 7] & 0b00010000
		self.dsm_trick_mode_flag = buffer[index + 7] & 0b00001000
		self.additional_copy_info_flag = buffer[index + 7] & 0b00000100
		self.crc_flag = buffer[index + 7] & 0b00001000
		self.extension_flag = buffer[index + 7] & 0b00000010

		self.header_data_length = buffer[index + 8]

		if self.stream_id == 0xBD:
			id = buffer[index + 9 + self.header_data_length]
			if id >= 0x20 and id <= 0x40: # x3f 0r x40 ?
				self.sub_picture_stream_id = id

		temp_index = index + 9
		if self.presentation_timestamp_decode_timestamp_flags == 0b00000010 or \
			self.presentation_timestamp_decode_timestamp_flags == 0b00000011:

			self.presentation_timestamp = buffer[temp_index + 4] >> 1 #ulong
			self.presentation_timestamp += buffer[temp_index + 3] << 7
			self.presentation_timestamp += (buffer[temp_index + 2] & 0b11111110) << 14
			self.presentation_timestamp += buffer[temp_index + 1] << 22
			self.presentation_timestamp += (buffer[temp_index + 0] & 0b00001110) << 29

			temp_index += 5
		if self.presentation_timestamp_decode_timestamp_flags == 0b00000011:
			self.decode_timestamp = buffer[temp_index + 4] >> 1
			self.decode_timestamp += buffer[temp_index + 3] << 7
			self.decode_timestamp += (buffer[temp_index + 2] & 0b11111110) << 14
			self.decode_timestamp += buffer[temp_index + 1] << 22
			self.decode_timestamp += (buffer[temp_index + 0] & 0b00001110) << 29

		data_index = index + self.header_data_length + 24 - Mpeg2Header.LENGTH

		data_size = self.length - (4 + self.header_data_length)

		if data_size < 0 or (data_size + data_index > len(buffer)): #// to fix bad subs...
			self.data_size = len(buffer) - data_index
			if (self.data_size < 0):
				return

		self._data_buffer = buffer[data_index:data_index+data_size]

	def write_to_stream(self, stream: bytes):
		return stream + self._data_buffer

def getFileExtension(inputFile):
	if not '.' in inputFile:
		return inputFile
	temp = inputFile.rsplit('.', 1)
	return temp[-1]

def removeFileExtension(inputFile):
	if not '.' in inputFile:
		return inputFile
	temp = inputFile.rsplit('.', 1)
	return temp[0]

class VobSubParser:
	def __init__(self, is_pal: bool):
		self.is_pal = is_pal
		self.vob_sub_packs: list[VobSubPack] = []
#		self.settings = SettingsArgs()

	def open_file(self, filename: str) -> None:
		with open(filename, mode='rb') as file:
			return file

	# /// <summary>
	# /// Can be used with e.g. MemoryStream or FileStream
	# /// </summary>
	# /// <param name="ms"></param>
	def open(self, ms: bytes):
		ms.Position = 0
		# var buffer = new byte[0x800] // 2048
		position = 0
		while (position < len(ms)):
			self.vob_sub_packs = []
			ms.seek(position, 0)
			buffer = ms.read(0x0800)
			if (is_subtitle_pack(buffer)):
				self.vob_sub_packs.append(VobSubPack(buffer, None))

			position += 0x800

	def open_json_subs(self, jsonData):
		subtitles = jsonData['subpictures']

		list_vob_sub_merge_pack = []

		for x in range(len(subtitles)):
			subtitles[x]['data'] = bytes.fromhex(subtitles[x]['data'])

			list_vob_sub_merge_pack.append(VobSubMergedPack(subtitles[x]['data'], timedelta(seconds=subtitles[x]['startTime'])))

		# Fix subs with no duration (completely normal) or negative duration or duration > 10 seconds
		for i in range(len(list_vob_sub_merge_pack)):
			pack = list_vob_sub_merge_pack[i]

			if pack.sub_picture.delay.total_seconds() * 1000 > 0:
				pack.end_time = pack.start_time + pack.sub_picture.delay

			if pack.end_time < pack.start_time \
				or pack.end_time.total_seconds() * 1000 - pack.start_time.total_seconds() * 1000 \
					> subtitle_maximum_display_milliseconds:

				if i + 1 < len(list_vob_sub_merge_pack):

					pack.end_time = timedelta(
						seconds=((list_vob_sub_merge_pack[i + 1].start_time.total_seconds() * 1000 \
						- minimum_milliseconds_between_lines) / 1000)
					)

					if pack.end_time.total_seconds() * 1000 - pack.start_time.total_seconds() * 1000 \
						> subtitle_maximum_display_milliseconds:

						pack.end_time = timedelta(seconds=((pack.start_time.total_seconds() * 1000 \
							+ subtitle_maximum_display_milliseconds) / 1000)
						)
					else:
						pack.end_time = timedelta(seconds=((pack.start_time.total_seconds() * 1000 + 3000) / 1000))

			self.vob_sub_packs.append(list_vob_sub_merge_pack[i])

		return self.vob_sub_packs

	def open_sub_idx(self, vob_sub_filename: str,  idx_filename: str):
		self.vob_sub_packs = []
		if not os.path.exists(idx_filename):
			# // No valid idx file found - just open like vob file
			self.open_file(vob_sub_filename)
			use_sub_timestamps = True
			return
		idx = Idx(idx_filename)
		self.idx_palette = idx.palette
		self.idx_languages = idx.languages
		if len(idx.idx_paragraphs) > 0:
			with open(vob_sub_filename, mode='rb') as fs:
				file = fs.read()
				for p in idx.idx_paragraphs:
					if p.file_position + 100 < len(file):
						position = p.file_position
						# fs.seek(p.file_position, 0)
						buffer = file[position: position + 0x0800]
						if is_subtitle_pack(buffer) or is_private_stream1(buffer, 0):
							vsp = VobSubPack(buffer, p)
							self.vob_sub_packs.append(vsp)
							if is_private_stream1(buffer, 0):
								position += vsp.packetized_elementary_stream.length + 6
							else:
								position += 0x800

							current_sub_picture_stream_id = 0
							if vsp.packetized_elementary_stream.sub_picture_stream_id != None:
								current_sub_picture_stream_id = vsp.packetized_elementary_stream.sub_picture_stream_id #.Value ?

							while vsp.packetized_elementary_stream != None \
								and hasattr(vsp.packetized_elementary_stream, 'sub_picture_stream_id') \
								and (vsp.packetized_elementary_stream.length == PES_MAX_LENGTH \
									or current_sub_picture_stream_id != vsp.packetized_elementary_stream.sub_picture_stream_id) \
								and position < len(file):

								# fs.seek(position, 0)
								# buffer = fs.read(0x800)
								buffer = file[position: position + 0x0800]
								vsp = VobSubPack(buffer, p) # idx position?

								if vsp.packetized_elementary_stream is not None \
									and hasattr(vsp.packetized_elementary_stream, 'sub_picture_stream_id') \
									and current_sub_picture_stream_id == vsp.packetized_elementary_stream.sub_picture_stream_id:
									self.vob_sub_packs.append(vsp)

									if is_private_stream1(buffer, 0):
										position += vsp.packetized_elementary_stream.length + 6
									else:
										position += 0x800
								else:
									position += 0x800
									fs.seek(position, 0)
			return

	def merge_vob_sub_packs(self) -> List[VobSubMergedPack]:
		"""
		Demultiplex multiplexed packs together each stream_id at a time + removing bad packs + fixing displaytimes
		:return: List of complete packs each with a complete sub image
		"""
		list_vob_sub_merge_pack: List[VobSubMergedPack] = []
		ms = bytearray()

		ticks_per_millisecond = 90.000
		if not self.is_pal:
			ticks_per_millisecond = 90.090 * (23.976 / 24)

		# get unique stream_ids
		unique_stream_ids = []
		for p in self.vob_sub_packs:
			if p.packetized_elementary_stream is not None \
				and hasattr(p.packetized_elementary_stream, "sub_picture_stream_id") \
				and p.packetized_elementary_stream.sub_picture_stream_id not in unique_stream_ids:

				unique_stream_ids.append(p.packetized_elementary_stream.sub_picture_stream_id)

		last_idx_paragraph: IdxParagraph = None
		for unique_stream_id in unique_stream_ids: # packets must be merged in stream_id order (so they don't get mixed)
			for p in self.vob_sub_packs:
				if (p.packetized_elementary_stream is not None  \
					and hasattr(p.packetized_elementary_stream, "sub_picture_stream_id") \
					and p.packetized_elementary_stream.sub_picture_stream_id == unique_stream_id):

					if p.packetized_elementary_stream.presentation_timestamp_decode_timestamp_flags > 0:
						if last_idx_paragraph is None or p.idx_line.file_position != last_idx_paragraph.file_position:
							if len(ms) > 0:
								list_vob_sub_merge_pack.append(VobSubMergedPack(ms, pts, stream_id, last_idx_paragraph))

							ms = bytearray()
							pts = timedelta(seconds = float(p.packetized_elementary_stream.presentation_timestamp / ticks_per_millisecond) / 1000) # 90000F * 1000)); (PAL)
							stream_id = p.packetized_elementary_stream.sub_picture_stream_id
					last_idx_paragraph = p.idx_line
					ms = p.packetized_elementary_stream.write_to_stream(ms)
			if len(ms) > 0:
				list_vob_sub_merge_pack.append(VobSubMergedPack(ms, pts, stream_id, last_idx_paragraph))
				ms = bytearray()

		# Remove any bad packs
		for i in range(len(list_vob_sub_merge_pack))[::-1]:
			pack = list_vob_sub_merge_pack[i]
			if pack.sub_picture == None \
				or pack.sub_picture.image_display_area.width <= 3 \
				or pack.sub_picture.image_display_area.height <= 2:

				list_vob_sub_merge_pack.pop(i)

			elif pack.end_time.total_seconds() - pack.start_time.total_seconds() < 0.1 \
				and pack.sub_picture.image_display_area.width <= 10 \
				and pack.sub_picture.image_display_area.height <= 10:

				list_vob_sub_merge_pack.pop(i)

		# Fix subs with no duration (completely normal) or negative duration or duration > 10 seconds
		for i in range(len(list_vob_sub_merge_pack)):
			pack = list_vob_sub_merge_pack[i]
			if pack.sub_picture.delay.total_seconds() * 1000 > 0:
				pack.end_time = pack.start_time + pack.sub_picture.delay

			if pack.end_time < pack.start_time \
				or pack.end_time.total_seconds() * 1000 - pack.start_time.total_seconds() * 1000 \
					> subtitle_maximum_display_milliseconds:

				if i + 1 < len(list_vob_sub_merge_pack):

					pack.end_time = timedelta(
						seconds=((list_vob_sub_merge_pack[i + 1].start_time.total_seconds() * 1000 \
						- minimum_milliseconds_between_lines) / 1000)
					)

					if pack.end_time.total_seconds() * 1000 - pack.start_time.total_seconds() * 1000 \
						> subtitle_maximum_display_milliseconds:

						pack.end_time = timedelta(seconds=((pack.start_time.total_seconds() * 1000 \
							+ subtitle_maximum_display_milliseconds) / 1000)
						)
					else:
						pack.end_time = timedelta(seconds=((pack.start_time.total_seconds() * 1000 + 3000) / 1000))
		return list_vob_sub_merge_pack

def extract_vob_sub_img_to_ass(vob_sub_file_name: Path, outputFilePath: Path, videoWidth: int, videoHeight: int, colorPalette = [], videoCropData: str = '', timeAdjustmentFactor: float = 1, timeOffset: float = 0) -> List[Path]:
	global use_sub_timestamps
	global args

	allowYUVConversion = False

	n_jobs = max(1, int(psutil.cpu_count(logical = False) * .75)) # Set the number of threads to a number relevant to our CPU core count

	if videoCropData == '':
		videoCropData = str(videoWidth) + ':' + str(videoHeight) + ':0:0'

	vob_sub_parser = VobSubParser(True)

	subFormat = getFileExtension(vob_sub_file_name).lower()

	if subFormat == 'json':
		if not os.path.exists(vob_sub_file_name):
			raise FileNotFoundError('Could not find "' + vob_sub_file_name + '" !')

		use_sub_timestamps = True

		try:
			jsonData = readJSONFile(vob_sub_file_name)
		except:
			raise Exception('Could not load JSON data from "' + vob_sub_file_name + '" ! Are you sure this is a JSON file?')

		if 'palette' in jsonData:
			if len(jsonData['palette']) == 16:
				colorPalette = jsonData['palette']
			else:
				print('Invalid color palette in JSON file!')
		elif len(colorPalette) != 16:
			raise Exception('Invalid color palette!')

		_vob_sub_merged_pack_list = vob_sub_parser.open_json_subs(jsonData)

	elif subFormat == 'idx' or subFormat == 'sub':
		if subFormat == 'idx':
			vob_sub_file_name = removeFileExtension(vob_sub_file_name)
			idx_file_name = vob_sub_file_name + '.idx'
			vob_sub_file_name += '.sub'
		else:
			idx_file_name = removeFileExtension(vob_sub_file_name) + '.idx'

		if not os.path.exists(vob_sub_file_name):
			raise FileNotFoundError('Could not find "' + vob_sub_file_name + '" !')
		if not os.path.exists(idx_file_name):
			raise FileNotFoundError('Could not find "' + idx_file_name + '" !')
		

		vob_sub_parser.open_sub_idx(str(vob_sub_file_name), str(idx_file_name))
		_vob_sub_merged_pack_list = vob_sub_parser.merge_vob_sub_packs()

		# If no palette was supplied, use the IDX file palette
		if len(colorPalette) != 16:
			colorPalette = vob_sub_parser.idx_palette
			for i in range(len(colorPalette)):
				colorPalette[i] = idxToRGB(colorPalette[i])
				allowYUVConversion = False

	for i in range(len(colorPalette)):
		colorPalette[i] = str(colorPalette[i]).strip()
		if args.convert_YUV == True and allowYUVConversion == True:
			colorPalette[i] = YUVStringToRGBString(colorPalette[i])

	colorPalette = convertPalette(colorPalette)

	return multiprocess(_vob_sub_merged_pack_list, outputFilePath, colorPalette, n_jobs, timeAdjustmentFactor, timeOffset, videoWidth, videoHeight, videoCropData)

class Idx:

	def __init__(self, file_name: str):
		self.idx_paragraphs: List[IdxParagraph] = []
		self.palette: List[str] = [] #Colour
		self.languages: List[str] = []
#		self.time_code_line_pattern = re.compile("^timestamp: \d+:\d+:\d+:\d+, filepos: [\dabcdefABCDEF]+$")


		with open(file_name) as file:
			lines = file.readlines()

		self.process_file(lines)


	def process_file(self, lines: List[str]):
		language_index = 0
		for line in lines:
			line = line.strip('\n')
			if line.find('timestamp: ') >= 0 and line.find(', filepos: ') >= 0:
#			if self.time_code_line_pattern.search(line) is not None:
				p: IdxParagraph = self.get_time_code_and_file_position(line)
				if p is not None:
					self.idx_paragraphs.append(p)

			elif line.startswith("palette:") and len(line) > 10:
				s =  line.strip('palette:').split(',')
				colors = [c.strip(' ') for c in s]
				for hex_str in colors:
					self.palette.append(self.hex_to_color(hex_str))

			elif line.startswith("id:") and len(line) > 4:
				# id: en, index: 1
				# id: es, index: 2
				self.language_index = line[-2].strip(' ')
				self.two_letter_language_id = line.split(',')[0][-3:].strip(' ')
				# parts = line.split(new[] { ':', ',', ' ' }, StringSplitOptions.RemoveEmptyEntries);
				# if parts.Length > 1:
					# string twoLetterLanguageId = parts[1];
					# string languageName = DvdSubtitleLanguage.GetLocalLanguageName(twoLetterLanguageId);
					# if (parts.Length > 3 && parts[2].Equals("index", StringComparison.OrdinalIgnoreCase))
					# {
					#	 int index;
					#	 if (int.TryParse(parts[3], out index))
					#	 {
					#		 languageIndex = index;
					#	 }
					# }
					# # Use U+200E (LEFT-TO-RIGHT MARK) to support right-to-left scripts
					# Languages.Add(string.Format("{0} \x200E(0x{1:x})", languageName, languageIndex + 32));
					# languageIndex++;


	def hex_to_color(self, hex_str: str):
		hex_str = hex_str.strip('#').strip()
		if (len(hex_str) == 6):
			r = int(hex_str[0: 2], 16)
			g = int(hex_str[2: 4], 16)
			b = int(hex_str[4: 6], 16)
			return padHexColor(hex(r).split('x').pop()) + padHexColor(hex(g).split('x').pop()) + padHexColor(hex(b).split('x').pop())


#			r = int(hex_str[0: 2], 16) / 255
#			g = int(hex_str[2: 4], 16) / 255
#			b = int(hex_str[4: 6], 16) / 255
#			return Color(rgb=(r, g, b))

		elif (len(hex_str) == 8):
			a = int(hex_str[0: 2], 16)
			r = int(hex_str[2: 4], 16)
			g = int(hex_str[4: 6], 16)
			b = int(hex_str[6: 8], 16)
			return hex(r).split('x').pop() + hex(g).split('x').pop() + hex(b).split('x').pop()

#			a = int(hex_str[0: 2], 16)
#			r = int(hex_str[2: 4], 16)
#			g = int(hex_str[4: 6], 16)
#			b = int(hex_str[6: 8], 16)
#			return Color(rgba=(r, g, b, a))
#		return Color("red")
		return 'ff00ff'

	def get_time_code_and_file_position(self, line: str) -> IdxParagraph:
		# timestamp: 00:00:01:401, filepos: 000000000
		timestamp, filepos = line.split(',')
		timestamp = timestamp[-12:]
		filepos = int(filepos[-9:], 16)
		if (len(timestamp.split(':')) == 4):
			hours, minutes, seconds, milliseconds = [int(o) for o in timestamp.split(':')]
			return IdxParagraph(timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds), filepos)
		return None

def get_endian_word(buffer: bytearray, index: int) -> int:
	"""
	Get two bytes word stored in endian order
	:param: buffer: bytearray
	:param: index: index in byte array

	"""
	if (index + 1 < len(buffer)):
		return (buffer[index] << 8) | buffer[index + 1]

	return 0

def get_endian(buffer: bytearray, index: int, count: int):
	result = 0
	for i in range(count):
		result = (result << 8) + buffer[index + i]

	return result

class VobSubPack:
		packetized_elementary_stream: PacketizedElementaryStream
		mpeg_2_header: Mpeg2Header

		def __init__(self, buffer: bytes, idx_line: IdxParagraph):
			self._buffer = buffer
			self.idx_line = idx_line

			if (is_mpeg2_pack_header(buffer)):

				self.mpeg_2_header = Mpeg2Header(buffer)
				self.packetized_elementary_stream = PacketizedElementaryStream(buffer, self.mpeg_2_header.LENGTH)

			elif (is_private_stream1(buffer, 0)):

				self.packetized_elementary_stream = PacketizedElementaryStream(buffer, 0)


parser = argparse.ArgumentParser("commands")
parser.add_argument("--input_file", required=True, help="The path to the .sub, .idx or .json file to convert.", type=str)
parser.add_argument("--output_file", required=True, help="The path to use for the .ass file output.", type=str)
parser.add_argument("--video_width", required=True, help="The width of the original video (Usually 720).", type=int)
parser.add_argument("--video_height", required=True, help="The height of the original video (Usually 480 or 576).", type=int)

parser.add_argument("--palette", required=False, default='', help="The color palette (16 RGB hexadecimal colors, delimited with commas).", type=str)
parser.add_argument("--convert_YUV", default=False, required=False, help="Optional - this will treat the --palette values as YUV, and convert them to RGB for you automatically.", type=bool)

parser.add_argument("--use_sub_timestamps", default=False, required=False, help="Optional - this will use the timestamps obtained from the VOB/SUB file, instead of from the IDX file.", type=float)

parser.add_argument("--crop_data", required=False, help="Optional - the parent video's crop data from FFmpeg, I.E. 720:360:0:58", type=str)

parser.add_argument("--time_scale", required=False, help="Optional - the multiplier to use on the subtitle timing.", type=float)
parser.add_argument("--time_offset", required=False, help="Optional - this will shift the subtitle timing by the specified number of seconds.", type=float)

parser.add_argument("--resolution_scale", default=2, required=False, help="Optional - this value states how much to increase the SubStation Alpha resolution. All other items are scaled to match, so this will not make any visual changes.", type=int)

parser.add_argument("--line_height", default=32, required=False, help="Optional - this value is used to scale the subtitles by the average height of each line. Other factors, like the width and height, may force this value to be less than desired, to avoid truncating on the edges. Valid range from 10 to 120.", type=int)
parser.add_argument("--margin", default=8, required=False, help="Optional - this is how many pixels (Based on the original video resolution) to use as a margin on all four sides.", type=int)

parser.add_argument("--max_line_spacing", default=-1, required=False, help="Optional - this is how many rows of transparent pixels to render before stopping. This has the effect of bringing lines of text closer together. Use -1 to disable.", type=int)
parser.add_argument("--keep_position", default=True, required=False, help="Optional - this will allow subtitles to keep their original position, whether that be top, middle, bottom, left, center, or right.", type=bool)

parser.add_argument("--alpha_threshold", default=35, required=False, help="Optional - any alpha below this intensity will be considered transparent. Range is 0 to 255.", type=int)
parser.add_argument("--alignment_threshold", default=25, required=False, help="Optional - this value is a percentage used to determine the placement of a subtitle on the screen. Higher numbers mean subtitles are more likely to be at the vertical edges and horizontal center of the screen. Valid values are 0 to 100.", type=int)

parser.add_argument("--font_name", default="PixelCaption", required=False, help="Optional - the name of the font to use. Note that this IS NOT the file name, this is the name of the font when used in a word processor or other software!", type=str)

parser.add_argument("--shadow_size", default=1.25, required=False, help="Optional - this will add a 3D shadow effect to the resulting subtitles. Default value is 1, set to 0 to disable. Keep in mind that the subtitles are far more readable with the shadows on.", type=float)

parser.add_argument("--max_duration", default=10, required=False, help="Optional - this sets the maximum duration for subtitles. This may be important in cases where the duration is controlled by the timing on the next subtitle.", type=float)
parser.add_argument("--min_height", default=5, required=False, help="Optional - this sets the minimum height for a subtitle. Anything smaller than this will be ignored. This may be important in cases where the duration is controlled by the timing on the next subtitle. Set to 0 to use all subtitles.", type=int)
parser.add_argument("--min_width", default=5, required=False, help="Optional - this sets the minimum width for a subtitle. Anything smaller than this will be ignored. This may be important in cases where the duration is controlled by the timing on the next subtitle. Set to 0 to use all subtitles.", type=int)





args = parser.parse_args()

colorPalette = []
if args.palette != '':
	colorPalette = args.palette.split(',')
	if len(colorPalette) != 16:
		if args.convert_YUV == True:
			print(colors.red + 'Incorrect palette length. Must be 16 hexadecimal YUV colors!' + colors.none)
		else:
			print(colors.red + 'Incorrect palette length. Must be 16 hexadecimal RGB colors!' + colors.none)
		raise 
	for i in range(len(colorPalette)):
		colorPalette[i] = colorPalette[i].strip()
		colorPalette[i] = colorPalette[i].replace('"', '')
		colorPalette[i] = colorPalette[i].replace("'", '')
		if len(colorPalette[i]) != 6:
			errorMessage = 'Incorrect palette color length! Each color must be 6 hexadecimal RGB digits. Was given: ' + colorPalette[i]
			if args.convert_YUV == True:
				errorMessage = 'Incorrect palette color length! Each color must be 6 hexadecimal YUV digits. Was given: ' + colorPalette[i]
			print(colors.red + errorMessage + colors.none)
			raise Exception(errorMessage)
			exit()

cropData = ''
if not args.crop_data == None:
	cropData = args.crop_data

timeScale = 1
if not args.time_scale == None:
	timeScale = args.time_scale

timeOffset = 0
if not args.time_offset == None:
	timeOffset = args.time_offset

# This gives the subtitles a pleasant 3D look
shadowSize = args.shadow_size
shadowSize = max(0, shadowSize)


resolutionScale = args.resolution_scale		# This is used to increase the canvas size for better rendering

minMargin = args.margin * resolutionScale
fontHeight = args.line_height
fontHeight = clamp(fontHeight, 10, 120)

maxEmptyLines = args.max_line_spacing

keepPosition = args.keep_position

alphaThreshold = max(0, min(255, args.alpha_threshold))
alignmentThreshold = max(0, min(100, args.alignment_threshold)) / 100

fontName = args.font_name

use_sub_timestamps = args.use_sub_timestamps

printed = False


videoWidth = args.video_width


maxSubtitleDuration = args.max_duration
imageHeightThreshold = args.min_height
imageWidthThreshold = args.min_width


print()
print(colors.blue  + '---------------------------------------------------------------------')
print(colors.white + '                         Sub2ASS Version 1.0')
print(colors.blue  + '---------------------------------------------------------------------')
print(colors.green)
print('This library converts ' + colors.white + 'vobsub' + colors.green + '/' + colors.white + 'dvdsub' + colors.green + ' subtitles to SubStation Alpha.' + colors.yellow)

if fontName.lower() == 'pixelcaption':
	print('The use of this library REQUIRES a special font called PixelCaption.' + colors.none)
	print('The font is licensed as public domain, and should be included with')
	print('this project.')
else:
	print('The font has been overriden with: ' + colors.red + fontName)

print(colors.none)



extract_vob_sub_img_to_ass(args.input_file, args.output_file, args.video_width, args.video_height, colorPalette, cropData, timeScale, timeOffset)


