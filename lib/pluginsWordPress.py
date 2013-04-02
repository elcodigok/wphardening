import os
import urllib2
import zipfile

class pluginsWordPress():
	def __init__(self, directory):
		self.directory = os.path.abspath(directory)
	
	def download(self):
		self.url = "http://downloads.wordpress.org/plugin/wp-login-security-2.1.0.2.zip"
		file_name = self.url.split('/')[-1]
		u = urllib2.urlopen(self.url)
		f = open(file_name, 'wb')
		f.write(u.read())
		f.close()
		
		zip_file = zipfile.ZipFile(os.path.abspath(file_name), 'r')
		zip_file.extractall(self.directory + '/wp-content/plugins')
		
		if os.path.exists(os.path.abspath(file_name)):
			os.remove(os.path.abspath(file_name))