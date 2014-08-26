#!/usr/bin/env python
"""
updateWPHardening.py

Copyright 2014 Daniel Maldonado

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

import sys
try:
    import git
except ImportError:
    print "You need to install on your system python-git"
    sys.exit()


class updateWPHardening():
    """
    This class updates the core WPHardening

    :author: Daniel Maldonado (daniel_5502@yahoo.com.ar)
    """
    def __init__(self, directory):
        """
        :param directory: Absolute path of the directory to check.
        """
        self.work_directory = directory

    def update(self):
        """
        :return: None
        """
        try:
            git.cmd.Git(self.work_directory).pull()
        except git.GitCommandError, e:
            print e
