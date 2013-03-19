import os

class chmodWordPress():
	def __init__(self, directory):
		self.directory = os.path.abspath(directory)
	
	def changePermisions(self):
		for r, d, f in os.walk(self.directory):
			os.chmod(r, 0755)
			for wpfile in f:
				os.chmod(os.path.join(r, wpfile), 0644)
		print "Todos los cambios ejecutados."
