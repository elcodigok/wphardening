#!/usr/bin/env python
"""
deleteVersionWordPress.py

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


class deleteVersionWordPress():
    def __init__(self, directory):
        self.directory = os.path.abspath(directory)
        self.filters = self.directory + "/wp-includes/default-filters.php"
        self.setFunction()
        self.setFilters()

    def setFilters(self):
        self.f = open(self.filters, "r")
        self.script = self.f.readlines()
        self.f.close()

    def getFilters(self):
        return self.script

    def setFunction(self):
        self.function = [
            '\n',
            '// This is a function that removes versions of WordPress.\n',
            'function delete_version_wp() {', '\n', '\treturn "";', '\n}',
            '\nadd_filter(\'the_generator\', \'delete_version_wp\');',
        ]

    def getFunction(self):
        return self.function

    def delete(self):
        f = open(self.filters, "w")
        f.writelines(self.getFilters() + self.getFunction())
        f.close()
        print colored('\nDeleted WordPress versions', 'yellow')
        print colored(
            '\tModified:\twp-includes/default-filters.php',
            'red'
        )
        print colored(
            '\t// This is a function that removes versions of WordPress.\n' +
            '\tfunction delete_version_wp() {\n' +
            '\t\treturn "";\n' +
            '\t}\n' +
            '\tadd_filter(\'the_generator\', \'delete_version_wp\');',
            'green'
        )
        logging.info("Modified: wp-includes/default-filters.php")
