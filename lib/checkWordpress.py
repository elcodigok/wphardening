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


class checkWordpress():
    def __init__(self, directory):
        self.content = "/wp-content"
        self.inContent = ["/plugins", "/themes"]

        self.admin = "/wp-admin"
        self.inAdmin = [
            "/css", "/images", "/includes", "/js",
            "/maint", "/network", "/user"
        ]

        self.includes = "/wp-includes"
        self.inIncludes = [
            "/css", "/images", "/js", "/pomo",
            "/SimplePie", "/Text", "/theme-compat", "/default-filters.php"
        ]
        self.directory = directory

    def existsContent(self):
        if os.path.exists(os.path.abspath(self.directory + self.content)):
            for control in self.inContent:
                if os.path.exists(
                    os.path.abspath(self.directory + self.content + control)
                ):
                    return True
                else:
                    return False
        else:
            return False

    def existsAdmin(self):
        if os.path.exists(os.path.abspath(self.directory + self.admin)):
            for control in self.inAdmin:
                if os.path.exists(
                    os.path.abspath(self.directory + self.admin + control)
                ):
                    return True
                else:
                    return False
        else:
            return False

    def existsIncludes(self):
        if os.path.exists(os.path.abspath(self.directory + self.includes)):
            for control in self.inIncludes:
                if os.path.exists(
                    os.path.abspath(self.directory + self.includes + control)
                ):
                    return True
                else:
                    return False
        else:
            return False

    def isWordPress(self):
        if (
            self.existsContent() and self.existsAdmin() and
            self.existsIncludes()
        ):
            return True
        else:
            return False
