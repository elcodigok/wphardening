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
from lib.termcolor import colored, cprint


class robotsWordPress:
    def __init__(self, directory):
        self.directory = os.path.abspath(directory)
        self.setRobots()

    def setRobots(self):
        self.robots = """# Sitemap

Sitemap: http://www.tusitioweb.com/sitemap.xml

# Ficheros y directorios a des/indexar de nuestro WordPress

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

# Reglas para los bots mas conocidos

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
        return self.robots

    def createRobots(self):
        print colored('\nCreated file robots.txt', 'yellow')
        fpath = self.directory + "/robots.txt"
        f = open(fpath, "w")
        f.writelines(self.getRobots())
        f.close()
        print colored('\tcreate:\tCreate robots.txt file ' + fpath, 'green')
