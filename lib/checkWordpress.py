import os

class checkWordpress():
	def __init__(self, directory):
		self.content = "/wp-content"
		self.inContent = ["/plugins", "/themes"]
		
		self.admin = "/wp-admin"
		self.inAdmin = ["/css", "/images", "/includes", "/js", "/maint", "/network", "/user"]
		
		self.includes = "/wp-includes"
		self.inIncludes = ["/css", "/images", "/js", "/pomo", "/SimplePie", "/Text", "/theme-compat", "/default-filters.php"]
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
