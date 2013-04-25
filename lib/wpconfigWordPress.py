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


class wpconfigWordPress():
    def __init__(self, directory):
        self.directory = directory
        self.opener = urllib2.build_opener(urllib2.HTTPHandler)
        self.db_host = 'localhost'
    
    def wizard(self):
        self.setDbName()
        self.setDbUser()
        self.setDbPassword()
        self.db_host = raw_input('Host [localhost] > ')
        self.salt = self.getSalt()
        self.table_prefix = raw_input('Table prefix [wph_] > ')
        self.language = raw_input('Language [es_ES] > ')
        self.getCompletConfig()
    
    def setDbName(self):
        value = raw_input('Name of the database > ')
        if value == '':
            self.setDbName()
        else:
            self.db_name = value

    def setDbUser(self):
        value = raw_input('Name of the User > ')
        if value == '':
            self.setDbUser()
        else:
            self.db_user = value

    def setDbPassword(self):
        value = raw_input('Password of the user > ')
        if value == '':
            self.setDbPassword()
        else:
            self.db_password = value
    
    def getCompletConfig(self):
        self.complet = """/** WordPress absolute path to the Wordpress directory. */
if ( !defined('ABSPATH') )
        define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
"""

    def getSalt(self):
        request = urllib2.Request("http://api.wordpress.org/secret-key/1.1/salt")
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
            self.getComment('Database Charset to use in creating database tables.') +
            'define(\'DB_CHARSET\', \'utf8\');\n\n'
        )
        f.write(
            self.getComment('The Database Collate type. Don\'t change this if in doubt.') +
            'define(\'DB_COLLATE\', \'\');\n\n'
        )
        f.write(
            self.getComment('Authentication Unique Keys and Salts.') +
            self.salt + '\n'
        )
        f.write(
            self.getComment('WordPress Database Table prefix.') +
            '$table_prefix = \'' + self.table_prefix + '\';\n\n'
        )
        f.write(
            self.getComment('WordPress Localized Language, defaults to English.') +
            'define(\'WPLANG\', \'' + self.language + '\');\n\n'
        )
        f.write(
            self.getComment('For developers: WordPress debugging mode.') +
            'define(\'WP_DEBUG\', false);\n\n'
        )
        f.write(
            self.getComment('Disable the Revisions.') +
            'define(\'WP_POST_REVISIONS\', false);\n\n'
        )
        f.write(
            self.getComment('Change the Filesystem Method.') +
            'define(\'FS_METHOD\', \'direct\');\n\n'
        )
        f.write(
            self.getComment('Change the Autosave Interval.') +
            'define(\'AUTOSAVE_INTERNAL\', 240);\n\n'
        )
        f.write(
            self.getComment('Disable Editing of Plugin & Theme Files.') +
            'define(\'DISALLOW_FILE_EDIT\', true);\n\n'
        )
        f.write('define(\'DISALLOW_FILE_MODS\', true);\n\n')
        f.write(self.complet + '\n')
        f.close()
