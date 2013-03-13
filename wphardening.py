#!/usr/bin/env python

from optparse import OptionParser
import os
import sys

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
	else:
		print "Could not find the specified directory"

if __name__ == "__main__":
	main()
