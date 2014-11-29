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
import re
import logging
from lib.termcolor import colored


class timthumbWordPress():
    """
    This class seeks TimThumb library

    :author: Daniel Maldonado (daniel_5502@yahoo.com.ar)
    """
    def __init__(self, directory):
        """
        :param directory: Absolute path of the directory to check.
        """
        self.fileWordPress = self.loadFile()
        self.directory = directory

    def searchVersion(self, pathFile):
        """
        :return: Content witch version the librery
        """
        f = open(self.directory + "/" + pathFile, "r")
        content = f.readlines()
        f.close()
        for i in content:
            matchObj = re.search("define.*\'VERSION\'.*;", i)
            if matchObj:
                return matchObj.group()

    def loadFile(self):
        """
        :return: Content with path to search the library
        """
        f = open('data/timthumbs.txt', "r")
        content = f.readlines()
        f.close()
        return content

    def decoratorOutput(self, foundFile):
        """
        :param foundFile: Number of found files
        :return: None
        """
        if foundFile == 0:
            print colored(
                "\nNot Found file library Timthumb in " +
                self.directory + "/", 'green'
            )

    def checkTimbthumb(self):
        """
        :return: None
        """
        foundFile = 0
        for f in self.fileWordPress:
            if os.path.exists(
                os.path.abspath(self.directory + "/" + f.split("\n")[0])
            ):
                foundFile += 1
                logging.info(
                    self.directory + " Found file library in " +
                    "/" + f.split("\n")[0]
                )
                print colored(
                    self.directory +
                    "/" +
                    f.split("\n")[0], 'yellow') + ' -', \
                    colored(
                        '\n\tFound file library Timbthumb in ' +
                        "/" + f.split("\n")[0] + ' - ' +
                        self.searchVersion(f.split("\n")[0]), 'red'
                    )
        self.decoratorOutput(foundFile)
