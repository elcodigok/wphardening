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
    """
    This class is to check that the specified directory is a project of
    WordPress.

    :author: Daniel Maldonado (daniel_5502@yahoo.com.ar)
    """
    def __init__(self, directory, verbose):
        """
        :param directory: Absolute path of the directory to check.
        :param verbose: Mode verbose.
        """
        self.fileWordPress = self.loadFile()
        self.directory = directory
        self.mode_verbose = verbose

    def loadFile(self):
        """
        :return: The list of all files in a project in WordPress.
        """
        f = open('data/wordpress.fuzz.txt', "r")
        content = f.readlines()
        f.close()
        return content

    def existsFiles(self):
        """
        :return: Number of files found
        """
        foundFile = 0
        for f in self.fileWordPress:
            if os.path.exists(
                os.path.abspath(self.directory + "/" + f.split("\n")[0])
            ):
                if self.mode_verbose:
                    print colored(
                        "\t[OK]\t" + self.directory + "/" + f.split("\n")[0],
                        'green',
                    )
                    logging.info(
                        self.directory + "/" + f.split("\n")[0]
                    )
                foundFile += 1
            elif self.mode_verbose:
                print colored(
                    "\t[FAIL]\t" + self.directory + "/" + f.split("\n")[0],
                    'red',
                )
                logging.error(
                    self.directory + "/" + f.split("\n")[0]
                )
        return foundFile

    def resumen(self, number):
        """
        :param number: Number of files found
        :return: None
        """
        print colored(
            "\t%s of the %s files are WordPress Project."
        ) % (str(number), str(len(self.fileWordPress)))

    def isWordPress(self):
        """
        :return: True if successful, False otherwise.
        """
        value = self.existsFiles()
        if ((value * 100) / len(self.fileWordPress) > 60):
            logging.info(
                self.directory + " This project directory is a WordPress."
            )
            print colored(self.directory, 'yellow') + ' -', \
                colored(
                    '\n\tThis project directory is a WordPress.', 'green'
                )
            if self.mode_verbose:
                self.resumen(value)
            return True
        else:
            logging.error(
                self.directory + " This Project directory is not a WordPress."
            )
            print colored(self.directory, 'yellow') + ' -', \
                colored(
                    '\n\tThis Project directory is not a WordPress.', 'red'
                )
            if self.mode_verbose:
                self.resumen(value)
            return False
