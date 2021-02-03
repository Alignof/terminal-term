# -*- coding: utf-8 -*-
from termterm import *
from unittest import TestCase

# unittest
class Testing(TestCase):
	def get_result(self, command):
		result  = execute_command(command)
		stdout  = str(result.stdout, encoding='utf-8', errors='replace')
		return stdout

	def test_parse(self):
		self.assertEqual(self.get_result("echo 'hello'"), "hello\n")
		self.assertEqual(self.get_result("echo 'hello world'"), "hello world\n")
		#self.assertEqual(self.get_result("echo $SHELL"), "/bin/zsh\n")


