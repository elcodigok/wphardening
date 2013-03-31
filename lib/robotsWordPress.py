import os

class robotsWordPress:
	def __init__(self, directory):
		self.directory = os.path.abspath(directory)
		self.setRobots()
	
	def setRobots(self):
		self.robots = """# Sitemap

Sitemap: http://www.tusitioweb.com/sitemap.xml

# Ficheros y directorios a des/indexar de nuestro WordPress

User-Agent: *
Allow: /wp-content/uploads/
Allow: /feed/$
Disallow: /wp-
Disallow: /wp-content/
Disallow: /trackback/
Disallow: /wp-admin/
Disallow: /feed/
Disallow: /?s=
Disallow: /search
Disallow: /archives/
Disallow: /index.php
Disallow: /*?
Disallow: /*.php$
Disallow: /*.js$
Disallow: /*.inc$
Disallow: /*.css$
Disallow: */feed/
Disallow: */trackback/
Disallow: /page/
Disallow: /tag/
Disallow: /category/

# Reglas para los bots mas conocidos

User-agent: Googlebot

User-agent: Googlebot-Image
Disallow: /wp-includes/
Allow: /wp-content/uploads/

User-agent: Mediapartners-Google*
Disallow:

User-agent: ia_archiver
Disallow: /

User-agent: duggmirror
Disallow: /

User-agent: noxtrumbot
Crawl-delay: 50

User-agent: msnbot
Crawl-delay: 30

User-agent: Slurp
Crawl-delay: 10

User-agent: MSIECrawler
Disallow: /

User-agent: WebCopier
Disallow: /

User-agent: HTTrack
Disallow: /

User-agent: Microsoft.URL.Control
Disallow: /

User-agent: libwww
Disallow: / """

	def getRobots(self):
		return self.robots
	  
	def createRobots(self):
		fpath = self.directory + "/robots.txt"
		f = open(fpath, "w")
		f.writelines(self.getRobots())
		f.close()
		print "[ C ] The robots.txt file."