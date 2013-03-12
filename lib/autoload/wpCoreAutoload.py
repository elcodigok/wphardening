import os

class wpCoreAutoload:
	__instance = None

	def __init__(self):
		
		#self.baseDir = os.path.dirname(os.path.realpath(__file__+"../"))
		#self.baseDir = os.path.dirname(os.path.realpath(__file__+'../../../'))
		self.baseDir = os.getcwd()
		self.baseDirProject = os.getcwd() + "/project"
		self.classes = {'wpHardeningName': 'newthon Framework TUI', 'wpHardeningVersion': '1.0', 'wpHardeningAuthor': 'Daniel M. Maldonado','wpAutoload': 'lib.autoload.wpAutoload','wpCoreAutoload': 'lib.autoload.wpCoreAutoload','wpFinder': 'lib.util.wpFinder'}

	def getInstance(self):
		if (wpCoreAutoload.__instance is None):
			wpCoreAutoload.__instance = wptCoreAutoload()
		return self.__instance

	def getBaseDir(self):
		return self.baseDir

	def getBaseDirProject(self):
		return self.baseDirProject

	def getBaseDirApp(self):
		return self.baseDirProject+'/apps'

	def getClasses(self):
		return self.classes

	def getClassPath(self, name_classes):
		if (name_classes in self.classes):
			return self.classes[name_classes]
		else:
			return None

