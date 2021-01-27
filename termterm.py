# -*- coding: utf-8 -*-
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

def main():
	prompt_style = ">>> "

	command = input(prompt_style)

	try:
		result = subprocess.run(command, shell = True, check = True)
	except:
		print("command error")

	print(result)

if __name__ == "__main__":
    main()


