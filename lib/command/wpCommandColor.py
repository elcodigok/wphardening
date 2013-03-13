class wpCommandColor:
	
	def begin(self):
		return chr(27)
	
	def getError(self):
		return self.begin() + "[1;41m"
	
	def end(self):
		return chr(27) + "[0m"