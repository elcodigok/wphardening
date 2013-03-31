import os

class deleteVersionWordPress():
	def __init__(self, directory):
		self.directory = os.path.abspath(directory)
		self.filters = self.directory + "/wp-includes/default-filters.php"
		self.setFunction()
		self.setFilters()
	
	def setFilters(self):
		self.f = open(self.filters, "r")
		self.script = self.f.readlines()
		self.f.close()
	
	def getFilters(self):
		return self.script
	
	def setFunction(self):
		self.function = ['\n', '// This is a function that removes versions of WordPress.\n', 'function delete_version_wp() {', '\n', '\treturn "";', '\n}', '\nadd_filter(\'the_generator\', \'delete_version_wp\');']
	
	def getFunction(self):
		return self.function
	
	def delete(self):
		f = open(self.filters, "w")
		f.writelines(self.getFilters() + self.getFunction())
		f.close()
		print "[ D ] WordPress versions."