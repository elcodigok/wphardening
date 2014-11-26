#!/usr/bin/env python
"""
indexesWordPress.py

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


class indexesWordPress():
    """
    This class creates and modifies the .htaccess file and
    index.php files

    :author: Daniel Maldonado (daniel_5502@yahoo.com.ar)
    """
    def __init__(self, directory, verbose=False):
        """
        :param directory: Absolute path of the directory to check.
        :param verbose: Mode verbose.
        """
        self.directory = os.path.abspath(directory)
        self.directory_create = [
            '/wp-content', '/wp-content/plugins', '/wp-content/uploads'
        ]
        self.htaccess = [
            '\n', '# Avoid Full Path Disclosure.\n',
            'php_flag display_errors off', '\n',
            '\n', '# Avoid the browser access to a folder without index.\n',
            'Options All -Indexes',
            '\n', '<Files .htaccess>',
            '\n', '\torder allow,deny',
            '\n', '\tdeny from all',
            '\n', '</Files>', '\n',
            '\n',
            '# The rise of bots, spammers, crack attacks and libwww-perl.\n',
            'RewriteCond %{HTTP_USER_AGENT} libwww-perl.*',
            '\n', 'RewriteRule .* - [F,L]',
            '\n', '# Query string Exploits.\n',
            '\n', 'RewriteCond %{QUERY_STRING} ../    [NC,OR]',
            '\n', 'RewriteCond %{QUERY_STRING} boot.ini [NC,OR]',
            '\n', 'RewriteCond %{QUERY_STRING} tag=     [NC,OR]',
            '\n', 'RewriteCond %{QUERY_STRING} ftp:     [NC,OR]',
            '\n', 'RewriteCond %{QUERY_STRING} http:    [NC,OR]',
            '\n', 'RewriteCond %{QUERY_STRING} https:   [NC,OR]',
            '\n', 'RewriteCond %{QUERY_STRING} mosConfig [NC,OR]',
            '\n', 'RewriteCond %{QUERY_STRING} ^.*([|]|(|)||\'|;|?|*).* [NC,OR]',
            '\n', 'RewriteCond %{QUERY_STRING} ^.*(%22|%27|%3C|%3E|%5C|%7B|%7C).* [NC,OR]',
            '\n', 'RewriteCond %{QUERY_STRING} ^.*(%0|%A|%B|%C|%D|%E|%F|127.0).* [NC,OR]',
            '\n', 'RewriteCond %{QUERY_STRING} ^.*(globals|encode|config|loopback).* [NC,OR]',
            '\n', 'RewriteCond %{QUERY_STRING} ^.*(request|select|insert|union|declare|drop).* [NC]',
            '\n', 'RewriteRule ^(.*)$ - [F,L]'            
        ]
        self.mode_verbose = verbose

    def writeHtaccess(self):
        """
        :return: None
        """
        if os.path.exists(self.directory + '/.htaccess'):
            f = open(self.directory + '/.htaccess', 'r')
            self.script = f.readlines()
            f.close()
            f = open(self.directory + '/.htaccess', 'w')
            f.writelines(self.script + self.htaccess)
            f.close()
            if self.mode_verbose:
                logging.info("Add options to " + self.directory + '/.htaccess')
                print colored('\tAdd options to ', 'green') + \
                    self.directory + '/.htaccess'
        else:
            f = open(self.directory + '/.htaccess', 'w')
            f.writelines(self.htaccess)
            f.close()
            if self.mode_verbose:
                logging.info("Create .htaccess file.")
                print colored('\tCreate Htaccess file ', 'green') + \
                    self.directory + '/.htaccess'

    def createIndexes(self):
        """
        :return: None
        """
        for index in self.directory_create:
            if not os.path.exists(self.directory + index):
                os.makedirs(self.directory + index)
            f = open(self.directory + index + '/index.php', "w")
            f.close()
            if self.mode_verbose:
                print colored(
                    '\nCreate Indexes Files in %s%s%s' % (
                        self.directory, index, '/index.php'
                    ),
                    'yellow'
                )
            logging.info(self.directory + index + "/index.php create.")
        print colored('\nCreate Indexes Files', 'yellow')
        print colored('\tAll index.php files were created.', 'green')
        self.writeHtaccess()
