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
        """
        :return: True if successful, False otherwise.
        """
        if self.value == "":
            return False
        else:
            value_check = self.value.split(":")
            if len(value_check) == 2:
                try:
                    self.uid = pwd.getpwnam(value_check[0]).pw_uid
                    self.gid = grp.getgrnam(value_check[1]).gr_gid
                    return True
                except KeyError:
                    print "The user or group does not exist on this system."
                    return False

            elif len(value_check) == 1:
                self.uid = pwd.getpwnam(value_check[0]).pw_uid
                self.gid = grp.getgrnam(value_check[0]).gr_gid
                return True
            else:
                return False
            return False

    def changeOwner(self):
        """
        :return: None
        """
        for r, d, f in os.walk(self.directory):
            os.chown(r, self.uid, self.gid)
            if self.mode_verbose:
                print colored('\tchown %s:%s ' + r, 'green') % (
                    pwd.getpwuid(self.uid).pw_name,
                    pwd.getpwuid(self.gid).pw_name)
                logging.info(
                    "chown " + pwd.getpwuid(self.uid).pw_name +
                    ":" + pwd.getpwuid(self.gid).pw_name + " " + r
                )
            for wpfile in f:
                os.chown(os.path.join(r, wpfile), self.uid, self.gid)
                if self.mode_verbose:
                    print colored('\t\tchown %s:%s ' + wpfile, 'green') % (
                        pwd.getpwuid(self.uid).pw_name,
                        pwd.getpwuid(self.gid).pw_name)
                    logging.info(
                        "chown " + pwd.getpwuid(self.uid).pw_name +
                        ":" + pwd.getpwuid(self.gid).pw_name + " " + r + wpfile
                    )
        print colored('\nchown on Directories', 'yellow')
        print colored('\tAll directories\t %s:%s', 'green') % (
            pwd.getpwuid(self.uid).pw_name,
            pwd.getpwuid(self.gid).pw_name)
        logging.info(
            "All directories " + pwd.getpwuid(self.uid).pw_name +
            ":" + pwd.getpwuid(self.gid).pw_name
        )
        print colored('\nchown on Files', 'yellow')
        print colored('\tAll files\t %s:%s', 'green') % (
            pwd.getpwuid(self.uid).pw_name,
            pwd.getpwuid(self.gid).pw_name)
        logging.info(
            "All files " + pwd.getpwuid(self.uid).pw_name +
            ":" + pwd.getpwuid(self.gid).pw_name
        )
