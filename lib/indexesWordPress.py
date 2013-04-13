#!/usr/bin/env python
"""
indexesWordPress.py

Copyright 2013 Daniel Maldonado

This file is part of WPHardening project.

WPHardening is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

WPHardening is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with WPHardening.  If not, see <http://www.gnu.org/licenses/>.

"""

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
            '\n','<Files .htaccess>',
            '\n', '\torder allow,deny',
            '\n', '\tdeny from all',
            '\n', '</Files>', '\n'
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
