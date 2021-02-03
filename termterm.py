# -*- coding: utf-8 -*-
import sys
import subprocess
from gui_display import *


def get_command():
	prompt_style = ">>> "
	command = input(prompt_style)

	if command.strip() == "exit":
		sys.exit(1)

	return command

def display_result(result):
	if result.returncode == 0 :
		stdout = str(result.stdout, encoding='utf-8', errors='replace')
		print(stdout, end='')
	else:
		stderr = str(result.stderr, encoding='utf-8', errors='replace')
		print(stderr, end='')

#######################################################################################

pattern_key = 2
PATTERN = 4

def execute_command(command, window):
	# exit terminal
	if command == "exit":
		sys.exit(1)

	# clear command line
	if command == "clear":
		global pattern_key
		window['-ML-'+sg.WRITE_ONLY_KEY]('')
		pattern_key = random.randint(0, PATTERN - 1)
		return subprocess.run("", shell = True, capture_output=True)

	try:
		result = subprocess.run(command, shell = True, capture_output=True)
	except:
		print("command error")
		sys.exit(1)

	return result

def main(window):
	while True:
		# get user input
		command = gui_get_command(window)

		# execute user input 
		result  = execute_command(command, window)

		# display stdout or stderr
		gui_display(result, pattern_key)


if __name__ == "__main__":
	# setup gui
	window = gui_setup()

	# main loop
	main(window)

	# Finish up by removing from the screen
	window.close()


