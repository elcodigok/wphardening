#!/usr/bin/env python
"""
pluginsWordPress.py

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

import re
import os
import urllib2
import zipfile
import logging
from lib.termcolor import colored


class pluginsWordPress():
    """
    This list class and download the most renowned WordPress
    security plugins.

    :author: Daniel Maldonado (daniel_5502@yahoo.com.ar)
    """
    def __init__(self, directory, proxy):
        """
        :param directory: Absolute path of the directory to check.
        :param proxy: String connection proxy.
        """
        self.yes = set(['yes', 'y', 'ye'])
        self.directory = os.path.abspath(directory)
        self.list_plugins = [
            [
                'AntiVirus',
                'Useful plugin that will scan your theme templates for' +
                ' malicious injections. Automatically. Every day.' +
                ' For more blog security.',
                'http://wordpress.org/extend/plugins/antivirus/'
            ],
            [
                'Bad Behavior',
                'Bad Behavior prevents spammers from ever delivering' +
                ' their junk, and in many cases, from ever reading your' +
                ' site in the first place.',
                'http://wordpress.org/extend/plugins/bad-behavior/'
            ],
            [
                'Block Bad Queries',
                'Block Bad Queries (BBQ) helps protect WordPress against' +
                ' malicious URL requests.',
                'http://wordpress.org/extend/plugins/block-bad-queries/'
            ],
            [
                'Exploit Scanner',
                'Search the files and database of your WordPress install' +
                ' for signs that may indicate that it has fallen victim' +
                ' to malicious hackers.',
                'http://wordpress.org/extend/plugins/exploit-scanner/'
            ],
            [
                'Latch',
                'This Plugin allows developers to integrate Latch on' +
                ' his/her WordPress service.',
                'http://wordpress.org/plugins/latch/'
            ],
            [
                'Limit Login Attempts',
                'Limit rate of login attempts, including by way of cookies,' +
                ' for each IP. Fully customizable.',
                'http://wordpress.org/extend/plugins/limit-login-attempts/'
            ],
            [
                'One-Time Password',
                'One-time password system conform RFC 2289 to protect your' +
                ' weblog in less trustworthy environments, like internet' +
                ' cafes.',
                'http://wordpress.org/extend/plugins/one-time-password/'
            ],
            [
                'UPDATE NOTIFICATIONS',
                'Check if your installation of wordpress updates are' +
                ' (core wordpress, themes and plugins). If so send an email.',
                'http://wordpress.org/extend/plugins/update-notifications/'
            ],
            [
                'User Locker',
                'This plugin locks user account after given number' +
                ' of incorrect login attempts. This makes brute force' +
                ' and dictionary attacks nearly impossible.',
                'http://wordpress.org/extend/plugins/user-locker/'
            ],
            [
                'WordPress File Monitor Plus',
                'Monitor files under your WP installation for changes.' +
                ' When a change occurs, be notified via email.' +
                ' This plugin is a fork of WordPress File Monitor.',
                'http://wordpress.org/extend/plugins/' +
                'wordpress-file-monitor-plus/'
            ],
            [
                'WP Login Security 2',
                'Whitelist User IP addresses. If a user logs in from an' +
                ' unknown IP the plugin sends an email to the user and' +
                ' optionally the admin with a one-time key.',
                'http://wordpress.org/extend/plugins/wp-login-security-2/'
            ],
            [
                'WP Security Scan',
                'Scans your WordPress installation for security' +
                ' vulnerabilities.',
                'http://wordpress.org/extend/plugins/wp-security-scan/'
            ],
            [
                'WP-DBManager',
                'Allows you to optimize database, repair database,' +
                ' backup database, restore database, delete backup database,' +
                ' drop/empty tables and run selected queries. Supports' +
                ' automatic scheduling of backing up, optimizing and' +
                ' repairing of database.',
                'http://wordpress.org/extend/plugins/wp-dbmanager/'
            ],
        ]
        if proxy is not None:
            conexion_proxy = {}
            conexion_proxy["http"] = proxy
            proxy_handler = urllib2.ProxyHandler(conexion_proxy)
            proxy_auth_handler = urllib2.ProxyBasicAuthHandler()
            proxy_auth_handler.add_password('', '', '', '')
            self.opener = urllib2.build_opener(
                proxy_handler,
                proxy_auth_handler
            )
            urllib2.install_opener(self.opener)
        else:
            self.opener = urllib2.build_opener(urllib2.HTTPHandler)

    def download(self, url):
        """
        :param url: URL Plugin.
        :return: None
        """
        self.url = url[0]
        file_name = self.url.split('/')[-1]
        try:
            u = urllib2.urlopen(self.url)
            f = open(file_name, 'wb')
            f.write(u.read())
            f.close()
            zip_file = zipfile.ZipFile(os.path.abspath(file_name), 'r')
            zip_file.extractall(self.directory + '/wp-content/plugins')
            if os.path.exists(os.path.abspath(file_name)):
                os.remove(os.path.abspath(file_name))
        except urllib2.URLError:
            print colored('\tYou can not download this plugins.', 'red')

    def questions(self):
        """
        :return: None
        """
        for plugin in self.list_plugins:
            print colored('\n' + plugin[0], 'yellow')
            print colored('\t' + plugin[1], 'green')
            print colored('\t' + plugin[2], 'green')
            q = raw_input('\tYou want to download [y/n] > ').lower()
            if q in self.yes:
                request = urllib2.Request(plugin[2])
                try:
                    resp = self.opener.open(request)
                    html = resp.read()
                    patron = re.compile(
                        "http://downloads.wordpress.org/plugin/" +
                        "[a-zA-Z0-9$-_@.&#+]+\.[zip|rar|gzip|tar.gz|tgz]+"
                    )
                    self.download(patron.findall(html))
                    logging.info(
                        "Download plugins " + plugin[0] +
                        " in " + self.directory + "/wp-contet/plugins")
                except urllib2.URLError, e:
                    print colored(
                        '\tPlease check your Internet connection,' +
                        ' you may have a problem.',
                        'red'
                    )
