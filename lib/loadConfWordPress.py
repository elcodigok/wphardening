#!/usr/bin/env python
"""
loadConfWordPress.py

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
import ConfigParser
from lib.termcolor import colored


class loadConfWordPress():
    def __init__(self, pathFile):
        self.pathFile = pathFile
        self.Config = ConfigParser.ConfigParser()
        self.Config.read(pathFile)

    def getSections(self):
        return self.Config.sections()

    def getDirectory(self):
        return self.Config.get('wphardening', 'directory')

    def getVerbose(self):
        if self.Config.get('wphardening', 'verbose').lower() == 'yes':
            return True
        else:
            return None

    def getChmod(self):
        if self.Config.get('wphardening', 'chmod').lower() == 'yes':
            return True
        else:
            return None

    def getRemove(self):
        if self.Config.get('wphardening', 'remove').lower() == 'yes':
            return True
        else:
            return None

    def getRobots(self):
        if self.Config.get('wphardening', 'robots').lower() == 'yes':
            return True
        else:
            return None

    def getFingerprinting(self):
        if self.Config.get('wphardening', 'fingerprinting').lower() == 'yes':
            return True
        else:
            return None

    def getTimthumb(self):
        if self.Config.get('wphardening', 'timthumb').lower() == 'yes':
            return True
        else:
            return None

    def getWpConfig(self):
        if self.Config.get('wphardening', 'wp_config').lower() == 'yes':
            return True
        else:
            return None

    def getDeleteVersion(self):
        if self.Config.get('wphardening', 'delete_version').lower() == 'yes':
            return True
        else:
            return None

    def getIndexes(self):
        if self.Config.get('wphardening', 'indexes').lower() == 'yes':
            return True
        else:
            return None

    def getMalwareScan(self):
        if self.Config.get('wphardening', 'malware_scan').lower() == 'yes':
            return True
        else:
            return None

    def getOutput(self):
        if self.Config.get('wphardening', 'output').lower() == 'yes':
            return True
        else:
            return None
