# -*- coding: utf-8 -*-
import sys
import subprocess
import gui

def get_command():
	prompt_style = ">>> "
	command = input(prompt_style)

	if command.strip() == "exit":
		sys.exit(1)

	return command

def execute_command(command):
	try:
		result = subprocess.run(command, shell = True, capture_output=True)
	except:
		print("command error")
		sys.exit(1)

	return result

def display_result(result):
	if result.returncode == 0 :
		stdout = str(result.stdout, encoding='utf-8', errors='replace')
		print(stdout, end='')
	else:
		stderr = str(result.stderr, encoding='utf-8', errors='replace')
		print(stderr, end='')


def main():
	while True:
		# get user input
		command = get_command()

		# execute user input 
		result  = execute_command(command)

		# display stdout or stderr
		display_result(result)


if __name__ == "__main__":
	# setup gui
	gui_setup()

	# main loop
	main()

	# Finish up by removing from the screen
	window.close()


