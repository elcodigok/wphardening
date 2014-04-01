#!/usr/bin/env python
"""
checkWordpress.py

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
from lib.termcolor import colored


class checkWordpress():
    def __init__(self, directory):
        self.fileWordPress = self.loadFile()
        self.directory = directory

    def loadFile(self):
        f = open('data/wordpress.fuzz.txt', "r")
        content = f.readlines()
        f.close()
        return content

    def existsFiles(self):
        foundFile = 0
        for f in self.fileWordPress:
            if os.path.exists(
                os.path.abspath(self.directory + "/" + f.split("\n")[0])
            ):
                foundFile += 1
        return foundFile

    def isWordPress(self):
        if ((self.existsFiles() * 100) / len(self.fileWordPress) > 60):
            logging.info(
                self.directory + " This project directory is a WordPress."
            )
            print colored(self.directory, 'yellow') + ' -', \
                colored(
                    '\n\tThis project directory is a WordPress.', 'green'
                )
            return True
        else:
            logging.info(
                self.directory + " This Project directory is not a WordPress."
            )
            print colored(self.directory, 'yellow') + ' -', \
                colored(
                    '\n\tThis Project directory is not a WordPress.\n', 'red'
                )
            return False
