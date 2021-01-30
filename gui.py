import PySimpleGUI as sg
def gui_setup:
	# Define the window's contents
	layout = [[sg.Text("terminal terminal")],
			  [sg.Text(size=(40,1), key='-OUTPUT-')],
			  [sg.Input(key='-INPUT-')],
			  [sg.Button('Ok'), sg.Button('Quit')]]

	# Create the window
	window = sg.Window('Window Title', layout)

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

