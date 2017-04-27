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
                'AntiVirus for WordPress is a easy-to-use, safe tool to' +
                ' harden your WordPress site against exploits, malware' +
                ' and spam injections.',
                'https://wordpress.org/plugins/antivirus/'
            ],
            [
                'Bad Behavior',
                'Bad Behavior complements other link spam solutions by' +
                ' acting as a gatekeeper, preventing spammers from ever' +
                ' delivering their junk, and in many cases, from ever' +
                ' reading your site in the first place. This keeps your' +
                ' site\'s load down, makes your site logs cleaner, and can' +
                ' help prevent denial of service conditions caused by' +
                ' spammers.',
                'https://wordpress.org/plugins/bad-behavior/'
            ],
            [
                'Block Bad Queries',
                'Block Bad Queries (BBQ) is a simple, super-fast plugin that' +
                ' protects your site against malicious URL requests. BBQ' +
                ' checks all incoming traffic and quietly blocks bad' +
                ' requests containing nasty stuff like eval(, base64_,' +
                ' and excessively long request-strings. This is a simple' +
                ' yet solid solution for sites that are unable to use a' +
                ' strong .htaccess firewall.',
                'https://wordpress.org/plugins/block-bad-queries/'
            ],
            [
                'Exploit Scanner',
                'This plugin searches the files on your website, and the' +
                ' posts and comments tables of your database for anything' +
                ' suspicious. It also examines your list of active plugins' +
                ' for unusual filenames.',
                'https://wordpress.org/plugins/exploit-scanner/'
            ],
            [
                'Latch',
                'This Plugin allows developers to integrate Latch on his/her' +
                ' WordPress service. Latch is a service that lets end-users' +
                ' add an extra level of security to their online accounts' +
                ' and services.',
                'https://wordpress.org/plugins/latch/'
            ],
            [
                'NinjaFirewall (WP Edition)',
                'NinjaFirewall (WP Edition) is a true Web Application' +
                ' Firewall. Although it can be installed and configured just' +
                ' like a plugin, it is a stand-alone firewall that sits in' +
                ' front of WordPress.',
                'https://wordpress.org/plugins/ninjafirewall/'
            ],
            [
                'Simple History',
                'Simple History shows recent changes made within' +
                ' WordPress, directly on your dashboard or on a separate' +
                ' page.',
                'https://wordpress.org/plugins/simple-history/'
            ],
            [
                'Stream',
                'With Stream, you\'re never left in the dark about WordPress' +
                ' Admin activity. Every logged-in user action is displayed' +
                ' in an activity stream and organised for easy filtering by' +
                ' User, Role, Context, Action or IP address.',
                'https://wordpress.org/plugins/stream/'
            ],
            [
                'WP Security Scan',
                'Acunetix WP Security plugin is a free and comprehensive' +
                ' security tool that helps you secure your WordPress' +
                ' installation and suggests corrective measures for:' +
                ' securing file permissions, security of the database,' +
                ' version hiding, WordPress admin protection and lots more.',
                'https://wordpress.org/plugins/wp-security-scan/'
            ],
            [
                'WP-DBManager',
                'Allows you to optimize database, repair database,' +
                ' backup database, restore database, delete backup database,' +
                ' drop/empty tables and run selected queries. Supports' +
                ' automatic scheduling of backing up, optimizing and' +
                ' repairing of database.',
                'https://wordpress.org/plugins/wp-dbmanager/'
            ],
            [
                'WPS Hide Login',
                'WPS Hide Login is a very light plugin that lets you easily' +
                ' and safely change the url of the login form page to' +
                ' anything you want. It doesn\'t literally rename or change' +
                ' files in core, nor does it add rewrite rules. It simply' +
                ' intercepts page requests and works on any WordPress' +
                ' website. The wp-admin directory and wp-login.php page' +
                ' become inaccessible, so you should bookmark or remember' +
                ' the url. Deactivating this plugin brings your site back' +
                ' exactly to the state it was before.',
                'https://wordpress.org/plugins/wps-hide-login/'
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
        idx = 1
        for plugin in self.list_plugins:
            print colored('\n%s) ' + plugin[0], 'yellow') % (idx)
            print colored('\t' + plugin[1], 'green')
            print colored('\t' + plugin[2], 'green')
            q = raw_input('\tYou want to download [y/n] > ').lower()
            idx += 1
            if q in self.yes:
                request = urllib2.Request(plugin[2])
                try:
                    resp = self.opener.open(request)
                    html = resp.read()
                    patron = re.compile(
                        "https://downloads.wordpress.org/plugin/" +
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
