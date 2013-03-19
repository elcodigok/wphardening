#!/usr/bin/env python

from optparse import OptionParser
from lib.checkWordpress import checkWordpress
from lib.chmodWordPress import chmodWordPress
from lib.removeWordPress import removeWordPress
import os
import sys

def main():
	usage = "usage: %prog [options] arg"
	version = '\nWP Hardening v0.1 (beta)\n'
	parser = OptionParser(usage, version=version)
	parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="active verbose mode output results")
	parser.add_option("-d", "--dir", dest="path", help="**REQUIRED** - Working Directory.", metavar="DIRECTORY")
	parser.add_option("-c", "--chmod-directory", action="store_true", dest="chmod", help="Chmod 755 in directory and 644 in files.")
	parser.add_option("-r", "--remove", action="store_true", dest="remove", help="Remove files and directory.")

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
			if options.chmod <> None:
				asdf = chmodWordPress(options.path)
				asdf.changePermisions()
			if options.remove <> None:
				qwer = removeWordPress(options.path)
				qwer.deleteReadme()
				qwer.deleteLicense()
		else:
			print "Esto NO es un WordPress."
	else:
		print "Could not find the specified directory"

if __name__ == "__main__":
	main()
