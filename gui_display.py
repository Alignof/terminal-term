import sys
import PySimpleGUI as sg
	
window = 0

def gui_setup():
	global window

	# window theme
	sg.theme('DarkGrey13')

	# Define the window's contents
	layout = [	[sg.Text(size=(150,25), key='-OUTPUT-')],
				[sg.Input(size=(150,1), key='-INPUT-')],
				[sg.Button('Ok', bind_return_key=True), sg.Button('Quit')]]

	# Create the window
	window = sg.Window('Terminal-term', layout, resizable=True, size=(800,500))

def gui_get_command():
	event, values = window.read()
	# See if user wants to quit or window was closed
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		sys.exit(1)

	return values['-INPUT-']

def gui_display_result(result):
	if result.returncode == 0 :
		stdout = str(result.stdout, encoding='utf-8', errors='replace')
		window['-OUTPUT-'].update(stdout)
	else:
		stderr = str(result.stderr, encoding='utf-8', errors='replace')
		window['-OUTPUT-'].update(stderr)

