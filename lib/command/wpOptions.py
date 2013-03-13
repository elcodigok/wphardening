import optparse

class wpOptions(optparse.OptionParser):
	def __init__(self, *args):
		optparse.OptionParser.__init__(self, 
                           description='Cross Site "Scripter" is an automatic -framework- to detect, exploit and\nreport XSS vulnerabilities in web-based applications.',
                           prog='XSSer.py',
			   version='\nXSSer v1.6 (beta): "Grey Swarm!" - 2011/2012 - (GPLv3.0) -> by psy\n',
                           usage= '\n\nxsser [OPTIONS] [-u <url> |-i <file> |-d <dork>] [-g <get> |-p <post> |-c <crawl>] [Request(s)] [Vector(s)] [Bypasser(s)] [Technique(s)] [Final Injection(s)]')

		self.set_defaults(verbose=False, threads=5, retries=1, delay=0, timeout=30,
                          silent=False)
		self.disable_interspersed_args()

		self.add_option("-s", "--statistics",  action="store_true", dest="statistics", help="show advanced statistics output results")
		self.add_option("-v", "--verbose", action="store_true", dest="verbose", help="active verbose mode output results")
		self.add_option("--gtk", action="store_true", dest="xsser_gtk", help="launch XSSer GTK Interface (Wizard included!)")