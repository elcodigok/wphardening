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
from lib.termcolor import colored, cprint


class wpconfigWordPress():
    def __init__(self, directory, proxy):
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
        self.setDbName()
        self.setDbUser()
        self.setDbPassword()
        self.setDbHost()
        self.salt = self.getSalt()
        self.setTablePrefix()
        self.setLanguage()
        self.setWpCron()
        self.getCompletConfig()

    def setDbName(self):
        value = raw_input('\tName of the database > ')
        if value == '':
            self.setDbName()
        else:
            self.db_name = value

    def setDbUser(self):
        value = raw_input('\tName of the User > ')
        if value == '':
            self.setDbUser()
        else:
            self.db_user = value

    def setDbPassword(self):
        value = raw_input('\tPassword of the user > ')
        if value == '':
            self.setDbPassword()
        else:
            self.db_password = value

    def setDbHost(self):
        value = raw_input('\tHost [localhost] > ')
        if value == '':
            self.db_host = 'localhost'
        else:
            self.db_host = value

    def setTablePrefix(self):
        value = raw_input('\tTable prefix [wph_] > ')
        if value == '':
            self.table_prefix = 'wph_'
        else:
            self.table_prefix = value

    def setLanguage(self):
        value = raw_input('\tLanguage [es_ES] > ')
        if value == '':
            self.language = ''
        else:
            self.language = value

    def setWpCron(self):
        value = raw_input('\tDisable wp-cron.php? [y/n] > ').lower()
        if value == 'y':
            self.wpcron = 'true'
        elif value == 'n':
            self.wpcron = 'false'
        else:
            self.wpcron = 'false'

    def getCompletConfig(self):
        self.complet = """/** WordPress absolute path to the\
Wordpress directory. */
if ( !defined('ABSPATH') )
        define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
"""

    def getSalt(self):
        request = urllib2.Request(
            "http://api.wordpress.org/secret-key/1.1/salt"
        )
        resp = self.opener.open(request)
        html = resp.read()
        return html

    def getComment(self, message):
        return ('/**\n' + ' * %s.\n'+' */\n') % message

    def createConfig(self):
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
        if self.wpcron == 'true':
            f.write(
                self.getComment(
                    'Disable the function of wp-cron.php\n' +
                    ' * We recommend creating this scheduled task on your server\n' +
                    ' * Minute: 0\n' + 
                    ' * Hour: Every 2 hours\n' +
                    ' * Day: *\n' +
                    ' * Moth: *\n' +
                    ' * Weekday: *\n' +
                    ' *\twget -O /dev/null http://yoursite.com/wp-cron.php?doing_wp_cron'
                ) + 
                'define(\'DISABLE_WP_CRON\', ' + self.wpcron + ');\n\n'
            )
        else:
            f.write(
                self.getComment('Enable the function of wp-cron.php') +
                'define(\'DISABLE_WP_CRON\', ' + self.wpcron + ');\n\n'
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
        f.write(self.complet + '\n')
        f.close()
