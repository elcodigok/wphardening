import os

class wizardWordPress:
	def __init__(self):
		self.directory = None
	
	def setDirectory(self):
		directorio = raw_input("Ingresa el Path: ")
		if os.path.exists(os.path.abspath(directorio)):
			self.directory = directorio
	
	def getDirectory(self):
		return self.directory