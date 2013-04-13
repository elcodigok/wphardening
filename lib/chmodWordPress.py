#!/usr/bin/env python
"""
chmodWordPress.py

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


class chmodWordPress():
    def __init__(self, directory):
        self.directory = os.path.abspath(directory)

    def changePermisions(self):
        for r, d, f in os.walk(self.directory):
            os.chmod(r, 0755)
            for wpfile in f:
                os.chmod(os.path.join(r, wpfile), 0644)
        print colored('\nchmod on Directories', 'yellow')
        print colored('\tAll directories\t drwxr-xr-x (755)', 'green')
        print colored('\nchmod on Files', 'yellow')
        print colored('\tAll files\t -rw-r--r-- (644)', 'green')
