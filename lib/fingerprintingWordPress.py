#!/usr/bin/env python
"""
fingerprintingWordPress.py

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

import fnmatch
import os
import os.path
import re
import datetime
import logging
from lib.termcolor import colored, cprint


class fingerprintingWordPress():
    def __init__(self, directory):
        self.directory = os.path.abspath(directory)
        # for files only
        self.includes = ['*.js', '*.css']
        self.includes = r'|'.join(
            [fnmatch.translate(x) for x in self.includes]
        )

    def searchStaticFile(self):
        for root, dirs, files in os.walk(self.directory):
            dirs[:] = [os.path.join(root, d) for d in dirs]

            # exclude/include files
            files = [os.path.join(root, f) for f in files]
            files = [f for f in files if re.match(self.includes, f)]

            for fname in files:
                f = open(fname, "r")
                script = f.readlines()
                f.close()
                f = open(fname, "w")
                f.writelines(self.getDateTime() + script)
                f.close()
        print colored('\nDeleted fingerprinting WordPress', 'yellow')
        logging.info("Fingerprinting: All changes implemented.")
        print colored('\tAll changes implemented.', 'green')

    def getDateTime(self):
        self.now = [
            '/* WP Hardening - ', str(datetime.datetime.now()) + '*/\n'
        ]
        return self.now
