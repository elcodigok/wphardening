#!/usr/bin/env python
"""
wpconfigWordpress.py

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
import urllib2
from lib.termcolor import colored
from random import choice


class wpconfigWordPress():
    """
    This class creates the file wp-config-wphardening.php

    :author: Daniel Maldonado (daniel_5502@yahoo.com.ar)
    """
    def __init__(self, directory, proxy):
        """
        :param directory: Absolute path of the directory to check.
        :param proxy: String connection proxy.
        """
        self.directory = directory
        print colored('\nCreated file wp-config-wphardening.php', 'yellow')
        self.opener = urllib2.build_opener(urllib2.HTTPHandler)
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

    def wizard(self):
        """
        :return: None
        """
        self.setDbName()
        self.setDbUser()
        self.setDbPassword()
        self.setDbHost()
        self.salt = self.getSalt()
        self.setTablePrefix()
        self.setLanguage()
        self.setWpCron()
        self.setSslCertificate()
        self.getCompletConfig()

    def setDbName(self):
        """
        :return: None
        """
        value = raw_input('\tName of the database > ')
        if value.strip() == '':
            self.setDbName()
        else:
            self.db_name = value

    def setDbUser(self):
        """
        :return: None
        """
        value = raw_input('\tName of the User > ')
        if value.lower().strip() == 'root':
            print (
                colored('\n\tThe use of the root user is not recommended.', 'red')
            )
            self.setDbUser()
        elif value.strip() == '':
            self.setDbUser()
        else:
            self.db_user = value

    def setDbPassword(self):
        """
        :return: None
        """
        value = raw_input('\tPassword of the user > ')
        if value.strip() == '':
            self.setDbPassword()
        else:
            self.db_password = value

    def setDbHost(self):
        """
        :return: None
        """
        value = raw_input('\tHost [localhost] > ')
        if value.strip() == '':
            self.db_host = 'localhost'
        else:
            self.db_host = value

    def setTablePrefix(self):
        """
        :return: None
        """
        value = raw_input('\tTable prefix [wph_] > ')
        if value.strip() == '':
            self.table_prefix = 'wph_'
        else:
            self.table_prefix = value

    def setLanguage(self):
        """
        :return: None
        """
        value = raw_input('\tLanguage [es_ES] > ')
        if value.strip() == '':
            self.language = ''
        else:
            self.language = value

    def setWpCron(self):
        """
        :return: None
        """
        value = raw_input('\tDisable wp-cron.php? [y/n] > ').lower()
        if value == 'y':
            self.wpcron = 'true'
        elif value == 'n':
            self.wpcron = 'false'
        else:
            self.wpcron = 'false'

    def setSslCertificate(self):
        """
        :return: None
        """
        value = raw_input(
            '\tYour host provider gives you SSL certificate? [y/n] > '
        ).lower()
        if value == 'y':
            self.sslcertificate = 'true'
        elif value == 'n':
            self.sslcertificate = 'false'
        else:
            self.sslcertificate = 'false'

    def getCompletConfig(self):
        """
        :return: None
        """
        self.complet = """/** WordPress absolute path to the\
Wordpress directory. */
if ( !defined('ABSPATH') )
        define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
"""

    def generateSalt(self):
        """
        :return: Salt content generated
        """
        lenSalt = 64
        values = "0123456789abcdefghijklmnopqrstuvwxyz" + \
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
            "()*+-$/_`{}%"
        resp = ""
        resp += "define('AUTH_KEY', '" + \
            "".join([choice(values) for i in range(lenSalt)]) + "');\n"
        resp += "define('SECURE_AUTH_KEY', '" + \
            "".join([choice(values) for i in range(lenSalt)]) + "');\n"
        resp += "define('LOGGED_IN_KEY', '" + \
            "".join([choice(values) for i in range(lenSalt)]) + "');\n"
        resp += "define('NONCE_KEY', '" + \
            "".join([choice(values) for i in range(lenSalt)]) + "');\n"
        resp += "define('AUTH_SALT', '" + \
            "".join([choice(values) for i in range(lenSalt)]) + "');\n"
        resp += "define('SECURE_AUTH_SALT', '" + \
            "".join([choice(values) for i in range(lenSalt)]) + "');\n"
        resp += "define('LOGGED_IN_SALT', '" + \
            "".join([choice(values) for i in range(lenSalt)]) + "');\n"
        resp += "define('NONCE_SALT', '" + \
            "".join([choice(values) for i in range(lenSalt)]) + "');\n"
        return resp

    def getSalt(self):
        """
        :return: Salt content in web WordPress
        """
        request = urllib2.Request(
            "http://api.wordpress.org/secret-key/1.1/salt"
        )
        try:
            resp = self.opener.open(request)
            html = resp.read()
            resp.close()
        except urllib2.URLError, e:
            html = self.generateSalt()
        return html

    def getComment(self, message):
        """
        :param message: Text of a message
        :return: Message format comment
        """
        return ('/**\n' + ' * %s.\n' + ' */\n') % message

    def changeMode(self, file_name):
        """
        :param file_name: file name to wp-config-wphardening.php
        :return: None
        """
        os.chmod(self.directory + file_name, 0640)

    def createConfig(self):
        """
        :return: None
        """
        f = open(self.directory + '/wp-config-wphardening.php', 'w')
        self.wizard()
        f.write('<?php \n\n')
        f.write(
            self.getComment('The name of the database for WordPress') +
            'define(\'DB_NAME\', \'' + self.db_name + '\');\n\n'
        )
        f.write(
            self.getComment('MySQL database username') +
            'define(\'DB_USER\', \'' + self.db_user + '\');\n\n'
        )
        f.write(
            self.getComment('MySQL database password') +
            'define(\'DB_PASSWORD\', \'' + self.db_password + '\');\n\n'
        )
        f.write(
            self.getComment('MySQL hostname') +
            'define(\'DB_HOST\', \'' + self.db_host + '\');\n\n'
        )
        f.write(
            self.getComment(
                'Database Charset to use in creating database tables'
            ) +
            'define(\'DB_CHARSET\', \'utf8\');\n\n'
        )
        f.write(
            self.getComment(
                'The Database Collate type. Don\'t change this if in doubt'
            ) +
            'define(\'DB_COLLATE\', \'\');\n\n'
        )
        f.write(
            self.getComment('Authentication Unique Keys and Salts') +
            self.salt + '\n'
        )
        f.write(
            self.getComment('WordPress Database Table prefix') +
            '$table_prefix = \'' + self.table_prefix + '\';\n\n'
        )
        f.write(
            self.getComment(
                'WordPress Localized Language, defaults to English'
            ) +
            'define(\'WPLANG\', \'' + self.language + '\');\n\n'
        )
	f.write(self.getComment('Disable reporting error.') + 'error_reporting(0);\n\n')
        if self.wpcron == 'true':
            f.write(
                self.getComment(
                    'Disable the function of wp-cron.php\n' +
                    ' * We recommend creating this scheduled task' +
                    ' on your server\n' +
                    ' * Minute: 0\n' +
                    ' * Hour: Every 2 hours\n' +
                    ' * Day: *\n' +
                    ' * Moth: *\n' +
                    ' * Weekday: *\n' +
                    ' *\twget -O /dev/null http://yoursite.com/' +
                    'wp-cron.php?doing_wp_cron'
                ) +
                'define(\'DISABLE_WP_CRON\', ' + self.wpcron + ');\n\n'
            )
        else:
            f.write(
                self.getComment('Enable the function of wp-cron.php') +
                'define(\'DISABLE_WP_CRON\', ' + self.wpcron + ');\n\n'
            )
        f.write(
            self.getComment('SSL certificate for Adminstration WordPress') +
            'define(\'FORCE_SSL_LOGIN\', ' + self.sslcertificate + ');\n' +
            'define(\'FORCE_SSL_ADMIN\', ' + self.sslcertificate + ');\n\n'
        )
        f.write(
            self.getComment('For developers: WordPress debugging mode') +
            'define(\'WP_DEBUG\', false);\n\n'
        )
        f.write(
            self.getComment('Disable the Revisions') +
            'define(\'WP_POST_REVISIONS\', false);\n\n'
        )
        f.write(
            self.getComment('Change the Filesystem Method') +
            'define(\'FS_METHOD\', \'direct\');\n\n'
        )
        f.write(
            self.getComment('Change the Autosave Interval') +
            'define(\'AUTOSAVE_INTERNAL\', 240);\n\n'
        )
        f.write(
            self.getComment('Disable Editing of Plugin & Theme Files') +
            'define(\'DISALLOW_FILE_EDIT\', true);\n\n'
        )
        f.write('define(\'DISALLOW_FILE_MODS\', true);\n\n')
        f.write('define(\'DISALLOW_UNFILTERED_HTML\', true);\n\n')
        f.write(self.complet + '\n')
        f.close()
        self.changeMode('/wp-config-wphardening.php')
