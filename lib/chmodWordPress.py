import os
from lib.termcolor import colored, cprint

class chmodWordPress():
	def __init__(self, directory):
		self.directory = os.path.abspath(directory)
	
	def changePermisions(self):
		for r, d, f in os.walk(self.directory):
			os.chmod(r, 0755)
			for wpfile in f:
				os.chmod(os.path.join(r, wpfile), 0644)
		print colored('\nchmod on Directories', 'yellow')
		print colored('\tAll directories\t drwxr-xr-x (755)', 'green')
		print colored('\nchmod on Files', 'yellow')
		print colored('\tAll files\t -rw-r--r-- (644)', 'green')
