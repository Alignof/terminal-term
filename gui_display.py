import sys
import random
import PySimpleGUI as sg
	
def gui_setup():
	# window theme
	sg.theme('DarkGrey13')
	MLINE_KEY = '-ML-'+sg.WRITE_ONLY_KEY   # multiline element's key. Indicate it's an output only element

	# Define the window's contents
	layout = [	[sg.Multiline(size=(150,25), key=MLINE_KEY)],
				[sg.Input(size=(150,1), key='-INPUT-')],
				[sg.Button('Ok', bind_return_key=True), sg.Button('Quit')]]

	# Create the window
	window = sg.Window('Terminal-term', layout, resizable=True, size=(800,500))

	# set display color
	output_key = MLINE_KEY
	sg.cprint_set_output_destination(window, output_key)

	return window

def gui_get_command(window):
	event, values = window.read()
	sg.cprint(">>>  " + values['-INPUT-'], text_color="green")

	# See if user wants to quit or window was closed
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		sys.exit(1)

	# clear input field
	window['-INPUT-']('')

	return values['-INPUT-'].strip()

def gui_display_result(result, pattern_key):
	display_pattern = [	gui_display_normal,
						gui_display_rev]
	display_pattern[pattern_key](result)

def gui_display_normal(result):
	if result.returncode == 0 :
		stdout = str(result.stdout, encoding='utf-8', errors='replace')
		sg.cprint(stdout, text_color="white")
	else:
		stderr = str(result.stderr, encoding='utf-8', errors='replace')
		sg.cprint(stderr, text_color="red")

def gui_display_rev(result):
	if result.returncode == 0 :
		stdout = str(result.stdout[::-1], encoding='utf-8', errors='replace')
		sg.cprint(stdout, text_color="white")
	else:
		stderr = str(result.stderr[::-1], encoding='utf-8', errors='replace')
		sg.cprint(stderr, text_color="red")


