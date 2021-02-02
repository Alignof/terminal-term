import sys
import PySimpleGUI as sg
	
window = 0

def gui_setup():
	global window

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

def gui_get_command():
	event, values = window.read()
	sg.cprint(">>>  " + values['-INPUT-'], text_color="green")

	# See if user wants to quit or window was closed
	if values['-INPUT-'].strip() == "exit" or event == sg.WINDOW_CLOSED or event == 'Quit':
		sys.exit(1)

	# clear command
	if values['-INPUT-'].strip() == "clear":
		window['-ML-'+sg.WRITE_ONLY_KEY]('')
		values['-INPUT-'] = ""

	window['-INPUT-']('')
	return values['-INPUT-']

def gui_display_result(result):

	if result.returncode == 0 :
		stdout = str(result.stdout, encoding='utf-8', errors='replace')
		sg.cprint(stdout, text_color="white")
	else:
		stderr = str(result.stderr, encoding='utf-8', errors='replace')
		sg.cprint(stderr, text_color="red")

