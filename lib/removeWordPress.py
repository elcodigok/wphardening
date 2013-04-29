#!/usr/bin/env python
"""
removeWordPress.py

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
import logging
from lib.termcolor import colored, cprint


class removeWordPress():
    def __init__(self, directory):
        self.directory = os.path.abspath(directory)
        self.readme = "/readme.html"
        self.license = ["/licencia.txt", "/license.txt"]

    def deleteReadme(self):
        if os.path.exists(self.directory + self.readme):
            os.remove(self.directory + self.readme)
            logging.info("delete: file readmes.")
            print colored('\tdelete:\tfile /readme.html', 'red')

    def deleteLicense(self):
        for pathLicese in self.license:
            if os.path.exists(self.directory + pathLicese):
                os.remove(self.directory + pathLicese)
                logging.info("delete: file " + pathLicese)
                print colored('\tdelete:\tfile ' + pathLicese, 'red')

    def delete(self):
        print colored('\nRemove files by defaults', 'yellow')
        self.deleteReadme()
        self.deleteLicense()
