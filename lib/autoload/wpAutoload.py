class wpAutoload:
	__instance = None

	def __init__(self):
		pass

	def getInstance(self):
		if (wpAutoload.__instance == None):
			wpAutoload.__instance = wpAutoload()
		return self.__instance
