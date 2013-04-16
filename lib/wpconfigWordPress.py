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
    
    def wizard(self):
        self.db_name = raw_input('Name of the database > ')
        self.db_user = raw_input('Name of the User > ')
        self.db_password = raw_input('Password of the user > ')
        self.db_host = raw_input('Host [localhost] > ')
        self.salt = self.getSalt()
        self.table_prefix = raw_input('Table prefix [wp_] > ')
        self.language = raw_input('Language [es_ES] > ')
        self.getCompletConfig()
    
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

    def createConfig(self):
        f = open(self.directory + '/wp-config-wphardening.php', 'w')
        self.wizard()
        f.write('<?php \n\n')
        f.write('define(\'DB_NAME\', \'' + self.db_name + '\');\n\n')
        f.write('define(\'DB_USER\', \'' + self.db_user + '\');\n\n')
        f.write('define(\'DB_PASSWORD\', \'' + self.db_password + '\');\n\n')
        f.write('define(\'DB_HOST\', \'' + self.db_host + '\');\n\n')
        f.write('define(\'DB_CHARSET\', \'utf8\');\n\n')
        f.write('define(\'DB_COLLATE\', \'\');\n\n')
        f.write(self.salt + '\n')
        f.write('$table_prefix = \'' + self.table_prefix + '\';\n\n')
        f.write('define(\'WPLANG\', \'' + self.language + '\');\n\n')
        f.write('define(\'WP_DEBUG\', false);\n\n')
        f.write('define(\'WP_POST_REVISIONS\', false);\n\n')
        f.write('define(\'COOKIE_DOMAIN\', \'www.yourwebsite.com\');\n\n')
        f.write('define(\'FS_METHOD\', \'direct\');\n\n')
        f.write('define(\'AUTOSAVE_INTERNAL\', 240);\n\n')
        f.write('define(\'DISALLOW_FILE_EDIT\', true);\n\n')
        f.write('define(\'DISALLOW_FILE_MODS\', true);\n\n')
        f.write(self.complet + '\n')
        f.close()