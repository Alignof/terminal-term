# -*- coding: utf-8 -*-
from termterm import *
from unittest import TestCase

# unittest
class Testing(TestCase):
	def get_result(self, command):
		result  = execute_command(command, window)
		stdout  = str(result.stdout, encoding='utf-8', errors='replace')
		return stdout
	
	def get_exit_code(self, command):
		result  = execute_command(command, window)
		return result.returncode

	def test_exe(self):
		self.assertEqual(self.get_exit_code("ls"), 0)
		self.assertEqual(self.get_exit_code("ls -l"), 0)
		self.assertEqual(self.get_exit_code("echo 0"), 0)
		self.assertEqual(self.get_exit_code("pwd"), 0)
		self.assertEqual(self.get_exit_code("whoami"), 0)
		self.assertNotEqual(self.get_exit_code("ll"), 0)
		self.assertNotEqual(self.get_exit_code("No_such_command"), 0)

	def test_parse(self):
		self.assertEqual(self.get_result("echo 'hello'"), "hello\n")
		self.assertEqual(self.get_result("echo 'hello world'"), "hello world\n")
		self.assertEqual(self.get_result("echo 0"), "0\n")
		self.assertEqual(self.get_result("perl -E 'say 5+6*11'"), "71\n")
		#self.assertEqual(self.get_result("echo $SHELL"), "/bin/zsh\n")


