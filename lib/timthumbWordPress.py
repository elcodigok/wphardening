#!/usr/bin/env python
"""
timthumbWordPress.py

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


class timthumbWordPress():
    def __init__(self, directory):
        self.fileWordPress = self.loadFile()
        self.directory = directory

    def loadFile(self):
        f = open('data/timthumbs.txt', "r")
        content = f.readlines()
        f.close()
        return content

    def decoratorOutput(self, foundFile):
        if foundFile == 0:
            print colored(
                "Not Found file library Timthumb in " +
                self.directory + "/", 'green'
            )

    def checkTimbthumb(self):
        foundFile = 0
        for f in self.fileWordPress:
            #print self.directory + "/" + f.split("\n")[0]
            if os.path.exists(
                os.path.abspath(self.directory + "/" + f.split("\n")[0])
            ):
                foundFile += 1
                logging.info(
                    self.directory + " Found file library Timthumb.php"
                )
                print colored(
                    self.directory +
                    "/" +
                    f.split("\n")[0], 'yellow') + ' -', \
                    colored('\n\tFound file library Timthumb.php', 'red')
        #print foundFile
        self.decoratorOutput(foundFile)
