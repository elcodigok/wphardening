#!/usr/bin/env python
"""
chownWordPress.py

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

import grp
import pwd
import os
import logging
from lib.termcolor import colored


class chownWordPress():
    def __init__(self, directory, value, verbose=False):
        """
        :param directory: Absolute path of the directory to check.
        :param value: Value to user and group
        :param verbose: Mode verbose.
        """
        self.directory = os.path.abspath(directory)
        self.value = value
        self.mode_verbose = verbose

    def isValid(self):
        if self.value == "":
            return False
        else:
            value_check = self.value.split(":")
            if len(value_check) == 2:
                #uid = pwd.getpwnam(value_check[0]).pw_uid
                try:
                    uid = pwd.getpwnam(value_check[0]).pw_uid
                    gid = grp.getgrnam(value_check[1]).gr_gid
                    print uid, gid
                except KeyError:
                    print "The user or group does not exist on this system."
                    return False
                
            elif len(value_check) == 1:
                uid = pwd.getpwnam(value_check[0]).pw_uid
                gid = grp.getgrnam(value_check[0]).gr_gid
                print uid, gid
            return True