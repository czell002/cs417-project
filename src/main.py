#! /usr/bin/env python3

import sys

from importlib import resources
from parse_temps import parse_raw_temps


def get_input_data() -> tuple[list[float], list[list[float]]]:
	"""
	Take an input file provided via the command line and parse the data into a more useful structure.
	
	Returns:
		A tuple containing the parsed time data and core temperature data.
	"""
	

	input_temps = sys.argv[1]
	
	# Begin quoted code from T. Kennedy at
	# https://github.com/cstkennedy/cs417-examples/tree/master/SemesterProject-CPU-Temps/python3
	with open(input_temps, "r") as temps_file:
		# ----------------------------------------------------------------------
		# Split Data, but Better!
		# ----------------------------------------------------------------------
		times = []
		core_data = [[] for _ in range(0, 4)]
	
		for time, raw_core_data in parse_raw_temps(temps_file):
			times.append(time)
			for core_idx, reading in enumerate(raw_core_data):
				core_data[core_idx].append(reading)
		# End quoted code
		return times, core_data


def main():
	"""
	Main function to demonstrate the use of the parse_raw_temps function and the get_input_data function.
	"""
	times, core_data = get_input_data()
	for time, *temps in list(zip(times, *core_data))[4:]:
		print(f"{time=} {temps=}")


if __name__ == "__main__":
	main()