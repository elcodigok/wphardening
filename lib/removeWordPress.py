import os

class removeWordPress():
	def __init__(self, directory):
		self.directory = os.path.abspath(directory)
		self.readme = "/readme.html"
		self.license = ["/licencia.txt", "/license.txt"]
	
	def deleteReadme(self):
		if os.path.exists(self.directory + self.readme):
			os.remove(self.directory + self.readme)
			print "[ D ] readme.html"
	
	def deleteLicense(self):
		for pathLicese in self.license:
			if os.path.exists(self.directory + pathLicese):
				os.remove(self.directory + pathLicese)
				print "[ D ] %s" % (pathLicese)
