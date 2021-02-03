import sys
import random
import PySimpleGUI as sg
	
window = 0
MLINE_KEY = 0

def gui_setup():
	global window
	global MLINE_KEY

	# window theme
	sg.theme('DarkGrey13')
	MLINE_KEY = '-ML-'+sg.WRITE_ONLY_KEY   # multiline element's key. Indicate it's an output only element

	# Define the window's contents
	layout = [	[sg.Multiline(size=(250,30), key=MLINE_KEY)],
				[sg.Input(size=(250,1), key='-INPUT-')],
				[sg.Button('Ok', bind_return_key=True), sg.Button('Quit')]]

	# Create the window
	window = sg.Window('Terminal-term', layout, resizable=True, size=(1200,800))

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

def gui_display(result, pattern_key):
	display_pattern = [	gui_display_normal,
						gui_display_colorful,
						gui_display_AA,
						gui_display_rev]
	print(pattern_key)
	display_pattern[pattern_key](result)

def gui_display_normal(result):
	if result.returncode == 0 :
		stdout = str(result.stdout, encoding='utf-8', errors='replace')
		sg.cprint(stdout, text_color="white")
	else:
		stderr = str(result.stderr, encoding='utf-8', errors='replace')
		sg.cprint(stderr, text_color="red")

def gui_display_AA(result):
	if result.returncode == 0 :
		out = str(result.stdout, encoding='utf-8', errors='replace').splitlines()
	else:
		out = str(result.stderr, encoding='utf-8', errors='replace').splitlines()

	AA =[	"    ／ﾌﾌ              ム｀ヽ        \t\t\t",
			"   / ノ)                    ）  ヽ  \t\t\t",
			" ﾞ/ ｜    ( ´・ω・）ノ⌒（ゝ._,ノ  < \t\t\t",
			" /  ﾉ⌒7⌒ヽーく   ＼  ／             \t\t\t",
			" 丶＿ ノ ｡     ノ､    ｡|/           \t\t\t",
			"     `ヽ `ー-'´_人`ー'ﾉ             \t\t\t",
			"        丶 ￣ _人'彡ﾉ               \t\t\t",
			"         ﾉ    r'十ヽ/               \t\t\t",
			"     ／｀ヽ_/  十∨､                 \t\t\t",
			"                                    \t\t\t"]

	sg.cprint(AA[0])
	sg.cprint(AA[1])
	for num, line in enumerate(out):
		if num+2 < len(AA):
			sg.cprint(AA[num+2] + line)
		else:
			sg.cprint(AA[-1] + line)
	
	print(len(out))
	print(len(AA))
	if len(out)+2 < len(AA):
		for index in range(len(out)+2, len(AA)):
			sg.cprint(AA[index])

	

def gui_display_colorful(result):
	bg_color = random.choice(['red', 'blue', 'green', 'black', 'gray', 'brown', 'purple'])
	window[MLINE_KEY].Widget.config(background = bg_color)
	gui_display_normal(result)

def gui_display_rev(result):
	if result.returncode == 0 :
		stdout = str(result.stdout[::-1], encoding='utf-8', errors='replace')
		sg.cprint(stdout, text_color="white")
	else:
		stderr = str(result.stderr[::-1], encoding='utf-8', errors='replace')
		sg.cprint(stderr, text_color="red")


