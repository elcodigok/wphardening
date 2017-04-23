#!/usr/bin/env python
"""
restApiWordPress.py

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


class restApiWordPress():
    def __init__(self, directory):
        self.directory = os.path.abspath(directory)
        self.filters = self.directory + "/wp-includes/default-filters.php"
        self.setFunctions()
        self.setScript()

    def getFilter(self):
        return self.filters

    def setFunctions(self):
        self.functions = [
            '\n', 'if ( version_compare( $wp_version, \'4.7\', \'>=\' ) ) {',
            '\n', '\tDRA_Force_Auth_Error();',
            '\n', '} else {', '\n', '\tDRA_Disable_Via_Filters();',
            '\n', '}', '\n', '/**',
            '\n', ' * This function is called if the current version of',
            ' WordPress is 4.7 or above',
            '\n', ' * Forcibly raise an authentication error to the REST API',
            ' if the user is not logged in',
            '\n', ' */',
            '\n', 'function DRA_Force_Auth_Error() {',
            '\n', '\tadd_filter( \'rest_authentication_errors\', ',
            '\'DRA_only_allow_logged_in_rest_access\' );',
            '\n', '}', '\n', '/**',
            '\n', ' * This function gets called if the current version of',
            ' WordPress is less than 4.7',
            '\n', ' * We are able to make use of filters to actually disable',
            ' the functionality entirely', '\n', ' */',
            '\n', 'function DRA_Disable_Via_Filters() {',
            '\n', '\t// Filters for WP-API version 1.x',
            '\n', '\tadd_filter( \'json_enabled\', \'__return_false\' );',
            '\n',
            '\tadd_filter( \'json_jsonp_enabled\', \'__return_false\' );',
            '\n',
            '\n', '\t// Filters for WP-API version 2.x', '\n',
            '\tadd_filter( \'rest_enabled\', \'__return_false\' );', '\n',
            '\tadd_filter( \'rest_jsonp_enabled\', \'__return_false\' );',
            '\n',
            '\n', '\t// Remove REST API info from head and headers', '\n',
            '\tremove_action( \'xmlrpc_rsd_apis', 'rest_output_rsd\' );',
            '\n', '\tremove_action( \'wp_head\',',
            ' \'rest_output_link_wp_head\', 10 );', '\n',
            '\tremove_action( \'template_redirect\',',
            ' \'rest_output_link_header\', 11 );', '\n', '}',
            '\n', '/**',
            '\n', ' * Returning an authentication error if a user who is not',
            ' logged in tries to query the REST API',
            '\n', ' * @param $access', '\n', ' * @return WP_Error',
            '\n', ' */',
            '\n', 'function DRA_only_allow_logged_in_rest_access( $access ) {',
            '\n', '\tif( ! is_user_logged_in() ) {', '\n',
            '\treturn new WP_Error( \'rest_cannot_access\',',
            ' __( \'Only authenticated users can access the REST API.\',',
            ' \'disable-json-api\' ), array( \'status\' =>',
            ' rest_authorization_required_code() ) );', '\n', '}',
            '\n', '\treturn $access;', '\n', '}'
        ]

    def getFunctions(self):
        return self.functions

    def setScript(self):
        self.f = open(self.filters, "r")
        self.script = self.f.readlines()
        self.f.close()

    def getScript(self):
        return self.script

    def disableRestApi(self):
        f = open(self.filters, "w")
        f.writelines(self.getScript() + self.getFunctions())
        f.close
        print colored('\nDisabled REST API', 'yellow')
        print colored(
            '\tModified:\twp-includes/default-filters.php',
            'red'
        )
        logging.info("Modified: wp-includes/default-filters.php")
