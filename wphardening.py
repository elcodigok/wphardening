#!/usr/bin/env python

import cmd
import os
from lib.autoload.wpCoreAutoload import *

currentDir = os.getcwd()

class wpCli(cmd.Cmd):
	nohelp = "No help on %s"
	ruler = "-"

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = 'WPHardening > '
	
	def do_version(self, line):
		wphardening_version = "0.1"
		
