import os
from lib.termcolor import colored, cprint


class indexesWordPress():
    def __init__(self, directory):
        self.directory = os.path.abspath(directory)
        self.directory_create = [
            '/wp-admin', '/wp-content', '/wp-content/plugins', '/wp-uploads'
        ]
        self.htaccess = [
            '\n', '# Avoid the browser access to a folder without index.\n',
            'Options All -Indexes',
        ]

    def writeHtaccess(self):
        if os.path.exists(self.directory + '/.htaccess'):
            f = open(self.directory + '/.htaccess', 'r')
            self.script = f.readlines()
            f.close()
            f = open(self.directory + '/.htaccess', 'w')
            f.writelines(self.script + self.htaccess)
            f.close()
            print colored('\tAdd options to ', 'green') + \
                self.directory + '/.htaccess'
        else:
            f = open(self.directory + '/.htaccess', 'w')
            f.writelines(self.htaccess)
            f.close()
            print colored('\tCreate Htaccess file ', 'green') + \
                self.directory + '/.htaccess'

    def createIndexes(self):
        for index in self.directory_create:
            if not os.path.exists(self.directory + index):
                os.makedirs(self.directory + index)
            f = open(self.directory + index + '/index.php', "w")
            f.close()
            # mode verbose
            # print "[ C ] index.php in " + \
            # self.directory + index + '/index.php'
        print colored('\nCreate Indexes Files', 'yellow')
        print colored('\tAll index.php files were created.', 'green')
        self.writeHtaccess()
