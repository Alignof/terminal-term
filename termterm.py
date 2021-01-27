# -*- coding: utf-8 -*-
import sys
import unittest
import subprocess

# unittest
class Testing(unittest.TestCase):
	"""
    def test_entered(self):
        self.assertEqual(check_entered("1234"), True)

    def test_hit_and_blow(self):
        self.assertEqual(hit_and_blow([1,2,3,4],[1,2,3,4]), (4,0))
	"""
	pass

# ====================================================================================================
# ****************************************************************************************************
# ====================================================================================================

def get_command():
	prompt_style = ">>> "
	command = input(prompt_style)

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
		result = get_command()

		# display ot stdout or stderr
		display_result(result)


if __name__ == "__main__":
    main()


