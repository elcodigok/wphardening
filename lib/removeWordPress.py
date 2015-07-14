#!/usr/bin/env python
"""
removeWordPress.py

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
import shutil
from lib.termcolor import colored


class removeWordPress():
    """
    This class removes all unnecessary files including WordPress.

    :author: Daniel Maldonado (daniel_5502@yahoo.com.ar)
    """
    def __init__(self, directory):
        """
        :param directory: Absolute path of the directory to check.
        """
        self.directory = os.path.abspath(directory)
        self.readme = "/readme.html"
        self.license = ["/licencia.txt", "/license.txt"]
        self.themes = [
            "/wp-content/themes/twentytwelve/",
            "/wp-content/themes/twentythirteen/",
            "/wp-content/themes/twentyfourteen/"
        ]
        self.static_file = [
            "/wp-includes/images/crystal/license.txt",
            "/wp-includes/images/crystal/license.txt",
            "/wp-includes/js/plupload/license.txt",
            "/wp-includes/js/plupload/changelog.txt",
            "/wp-includes/js/tinymce/license.txt",
            "/wp-includes/js/tinymce/plugins/spellchecker/changelog.txt",
            "/wp-includes/js/swfupload/license.txt",
            "/wp-includes/ID3/license.txt",
            "/wp-includes/ID3/readme.txt",
            "/wp-includes/ID3/license.commercial.txt"
        ]
        self.plugins = [
            "/wp-content/plugins/hello.php"
        ]

    def deleteThemes(self):
        """
        :return: None
        """
        for pathThemes in self.themes:
            if os.path.exists(self.directory + pathThemes):
                shutil.rmtree(self.directory + pathThemes)
                logging.info("Delete: Theme " + pathThemes)
                print colored('\tdelete:\ttheme ' + pathThemes, 'red')

    def deleteReadme(self):
        """
        :return: None
        """
        if os.path.exists(self.directory + self.readme):
            os.remove(self.directory + self.readme)
            logging.info("Delete: file readmes.")
            print colored('\tdelete:\tfile /readme.html', 'red')

    def deleteLicense(self):
        """
        :return: None
        """
        for pathLicese in self.license:
            if os.path.exists(self.directory + pathLicese):
                os.remove(self.directory + pathLicese)
                logging.info("Delete: file " + pathLicese)
                print colored('\tdelete:\tfile ' + pathLicese, 'red')

    def deleteStaticFile(self):
        """
        :return: None
        """
        for pathFile in self.static_file:
            if os.path.exists(self.directory + pathFile):
                os.remove(self.directory + pathFile)
                logging.info("Delete: file " + pathFile)
                print colored('\tdelete:\tfile ' + pathFile, 'red')

    def delete(self):
        """
        :return: None
        """
        print colored('\nRemove files by defaults', 'yellow')
        self.deleteReadme()
        self.deleteLicense()
        self.deleteThemes()
        self.deleteStaticFile()
