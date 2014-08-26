#!/usr/bin/env python
"""
robotsWordPress.py

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


class robotsWordPress:
    """
    This class create file robots.txt
    """
    def __init__(self, directory):
        """
        :param directory: Absolute path of the directory to check.
        """
        self.directory = os.path.abspath(directory)
        print colored('\nCreated file robots.txt', 'yellow')
        self.setUrl()
        self.setRobots()

    def setUrl(self):
        """
        :return: None
        """
        value = raw_input('\tURL your site > ')
        if value == '':
            self.setUrl()
        else:
            self.url = value

    def getSitemap(self):
        """
        :return: URL complete eith /sitemap.xml
        """
        return self.url + "/sitemap.xml"

    def setRobots(self):
        """
        :return: None
        """
        self.robots = "# Sitemap\n"
        self.robots += "Sitemap: " + self.getSitemap() + '\n\n'
        self.robots += """# Files and Directories to not\
indexing of our WordPress

User-Agent: *
Allow: /wp-content/uploads/
Allow: /feed/$
Disallow: /wp-
Disallow: /wp-content/
Disallow: /trackback/
Disallow: /wp-admin/
Disallow: /feed/
Disallow: /?s=
Disallow: /search
Disallow: /archives/
Disallow: /index.php
Disallow: /*?
Disallow: /*.php$
Disallow: /*.js$
Disallow: /*.inc$
Disallow: /*.css$
Disallow: */feed/
Disallow: */trackback/
Disallow: /page/
Disallow: /tag/
Disallow: /category/

# Rules for most known bots

User-agent: Googlebot

User-agent: Googlebot-Image
Disallow: /wp-includes/
Allow: /wp-content/uploads/

User-agent: Mediapartners-Google*
Disallow:

User-agent: ia_archiver
Disallow: /

User-agent: duggmirror
Disallow: /

User-agent: noxtrumbot
Crawl-delay: 50

User-agent: msnbot
Crawl-delay: 30

User-agent: Slurp
Crawl-delay: 10

User-agent: MSIECrawler
Disallow: /

User-agent: WebCopier
Disallow: /

User-agent: HTTrack
Disallow: /

User-agent: Microsoft.URL.Control
Disallow: /

User-agent: libwww
Disallow: / """

    def getRobots(self):
        """
        :return: Contents of robots.txt file
        """
        return self.robots

    def createRobots(self):
        """
        :return: None
        """
        fpath = self.directory + "/robots.txt"
        f = open(fpath, "w")
        f.writelines(self.getRobots())
        f.close()
        logging.info("Create file robots.txt in " + self.directory)
        print colored('\tCreate:\tCreate robots.txt file ' + fpath, 'green')
