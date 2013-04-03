import os

class indexesWordPress():
	def __init__(self, directory):
		self.directory = os.path.abspath(directory)
		self.directory_create = ['/wp-admin', '/wp-content', '/wp-content/plugins', '/wp-uploads']
	
	def createIndexes(self):
		for index in self.directory_create:
			if not os.path.exists(self.directory + index):
				os.makedirs(self.directory + index)
			f = open(self.directory + index + '/index.php', "w")
			f.close()
			print "[ C ] index.php in " + self.directory + index + '/index.php'