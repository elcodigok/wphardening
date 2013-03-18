#!/usr/bin/env python

from optparse import OptionParser
import os
import stat
import sys

class checkWordpress():
	def __init__(self, directory):
		self.content = "/wp-content"
		self.inContent = ["/plugins", "/themes"]
		
		self.admin = "/wp-admin"
		self.inAdmin = ["/css", "/images", "/includes", "/js", "/maint", "/network", "/user"]
		
		self.includes = "/wp-includes"
		self.inIncludes = ["/css", "/images", "/js", "/pomo", "/SimplePie", "/Text", "/theme-compat"]
		self.directory = directory
	
	def existsContent(self):
		if os.path.exists(os.path.abspath(self.directory + self.content)):
			for control in self.inContent:
				if os.path.exists(os.path.abspath(self.directory + self.content + control)):
					return True
				else:
					return False
		else:
			return False
	
	def existsAdmin(self):
		if os.path.exists(os.path.abspath(self.directory + self.admin)):
			for control in self.inAdmin:
				if os.path.exists(os.path.abspath(self.directory + self.admin + control)):
					return True
				else:
					return False
		else:
			return False
	
	def existsIncludes(self):
		if os.path.exists(os.path.abspath(self.directory + self.includes)):
			for control in self.inIncludes:
				if os.path.exists(os.path.abspath(self.directory + self.includes + control)):
					return True
				else:
					return False
		else:
			return False

	def isWordPress(self):
		if self.existsContent() and self.existsAdmin() and self.existsIncludes():
			return True
		else:
			return False

class chmodWordPress():
	def __init__(self, directory):
		self.directory = os.path.abspath(directory)
	
	def changePermisions(self):
		for r, d, f in os.walk(self.directory):
			os.chmod(r, 0755)
			for wpfile in f:
				os.chmod(os.path.join(r, wpfile), 0644)
		print "Todos los cambios ejecutados."

def main():
	usage = "usage: %prog [options] arg"
	version = '\nWP Hardening v0.1 (beta)\n'
	parser = OptionParser(usage, version=version)
	parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="active verbose mode output results")
	parser.add_option("-d", "--dir", dest="path", help="**REQUIRED** - Working Directory.", metavar="DIRECTORY")
	parser.add_option("-o", "--output", action="store", type="string", dest="output", help="Specify the output directory")

	(options, args) = parser.parse_args()

	if options.path == None:
		parser.print_help()
		sys.exit()
	
	options.path = os.path.abspath(options.path)
	if os.path.exists(options.path):
		print options.path
		wordpress = checkWordpress(options.path)
		if wordpress.isWordPress():
			print "Esto es un WordPress."
			asdf = chmodWordPress(options.path)
			asdf.changePermisions()
		else:
			print "Esto NO es un WordPress."
	else:
		print "Could not find the specified directory"

if __name__ == "__main__":
	main()
