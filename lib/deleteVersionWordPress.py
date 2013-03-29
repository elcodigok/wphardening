import os

class deleteVersionWordPress():
	def __init__(self, directory):
		self.directory = os.path.abspath(directory)
		self.filters = self.directory + "/wp-includes/default-filters.php"
		self.function = "\nfunction delete_version_wp() {\n\treturn '';\n}\nadd_filter('the_generator', 'delete_version_wp');"
		self.setFilters()
	
	def setFilters(self):
		self.f = open(self.filters, "r")
		self.script = self.f.readlines()
		self.f.close()
	
	def getFilters(self):
		return self.script
	
	def delete(self):
		#self.text = self.getFilters() + self.function
		f = open(self.filters, "w")
		f.writelines(self.script)
		f.writelines(self.function)
		f.close()
		print "Ya se agrego la libreria."