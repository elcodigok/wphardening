#!/usr/bin/env python

import cmd
import os
from lib.autoload.wpCoreAutoload import *
from lib.command.wpCommandColor import *

currentDir = os.getcwd()
os.chdir(currentDir)

class wpCli(cmd.Cmd):
	nohelp = "No help on %s"
	ruler = "-"

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = 'WPHardening > '
		self.color = wpCommandColor()

	def do_version(self, line):
		wphardening_version = wpCoreAutoload()
		print wphardening_version.getClassPath('wpHardeningName')
		print "Version: " + wphardening_version.getClassPath('wpHardeningVersion')
		print "Author: " + wphardening_version.getClassPath('wpHardeningAuthor')

	def help_version(self):
		print "Show WPHardening version information."

	def do_exit(self, line):
		return True

	def do_quit(self, line):
		return True

	def postloop(self):
		print "Bye."

	def default(self, line):
		"""Called on an input line when the command prefix is not recognized.
		If this method is not overridden, it prints an error message and
		returns.
		"""
		#self.stdout.write(chr(27) + "[1;41m" + "  Task [ %s ] is not defined.  \n" % line + chr(27) + "[0m")
		self.stdout.write(self.color.getError() + "  Task < %s > is not defined.  " % line + self.color.end() + "\n")

	def do_command(self, line):
		output = os.popen(line).read()
		print output


if __name__ == '__main__':
	wphardening = wpCli()
	wphardening.cmdloop()