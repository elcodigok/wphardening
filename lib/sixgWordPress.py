#!/usr/bin/env python
"""
sixgWordPress.py

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


class sixgWordPress():
    
    def __init__(self, directory, verbose=False):
        """
        :param directory: Absolute path of the directory to check.
        :param verbose: Mode verbose.
        """
        self.directory = os.path.abspath(directory)
        self.htaccess = [
            '\n', '# 6G:[QUERY STRINGS]', '\n',
'<IfModule mod_rewrite.c>', '\n',
'\tRewriteEngine On', '\n',
'\tRewriteCond %{QUERY_STRING} (eval\() [NC,OR]', '\n',
'\tRewriteCond %{QUERY_STRING} (127\.0\.0\.1) [NC,OR]', '\n',
'\tRewriteCond %{QUERY_STRING} ([a-z0-9]{2000,}) [NC,OR]', '\n',
'\tRewriteCond %{QUERY_STRING} (javascript:)(.*)(;) [NC,OR]', '\n',
'\tRewriteCond %{QUERY_STRING} (base64_encode)(.*)(\() [NC,OR]', '\n',
'\tRewriteCond %{QUERY_STRING} (GLOBALS|REQUEST)(=|\[|%) [NC,OR]', '\n',
'\tRewriteCond %{QUERY_STRING} (<|%3C)(.*)script(.*)(>|%3) [NC,OR]', '\n',
'\tRewriteCond %{QUERY_STRING} (\\|\.\.\.|\.\./|~|`|<|>|\|) [NC,OR]', '\n',
'\tRewriteCond %{QUERY_STRING} (boot\.ini|etc/passwd|self/environ) [NC,OR]', '\n',
'\tRewriteCond %{QUERY_STRING} (thumbs?(_editor|open)?|tim(thumb)?)\.php [NC,OR]', '\n',
'\tRewriteCond %{QUERY_STRING} (\'|\")(.*)(drop|insert|md5|select|union) [NC]', '\n',
'\tRewriteRule .* - [F]', '\n',
'</IfModule>', '\n',
'\n', '# 6G:[REQUEST METHOD]', '\n',
'<IfModule mod_rewrite.c>', '\n',
'\tRewriteCond %{REQUEST_METHOD} ^(connect|debug|move|put|trace|track) [NC]', '\n',
'\tRewriteRule .* - [F]', '\n',
'</IfModule>', '\n',
'\n', '# 6G:[REFERRERS]', '\n',
'<IfModule mod_rewrite.c>', '\n',
'\tRewriteCond %{HTTP_REFERER} ([a-z0-9]{2000,}) [NC,OR]', '\n',
'\tRewriteCond %{HTTP_REFERER} (semalt.com|todaperfeita) [NC]', '\n',
'\tRewriteRule .* - [F]', '\n',
'</IfModule>', '\n',
'\n', '# 6G:[REQUEST STRINGS]', '\n',
'<IfModule mod_alias.c>', '\n',
'\tRedirectMatch 403 (?i)([a-z0-9]{2000,})', '\n',
'\tRedirectMatch 403 (?i)(https?|ftp|php):/', '\n',
'\tRedirectMatch 403 (?i)(base64_encode)(.*)(\()', '\n',
'\tRedirectMatch 403 (?i)(=\\\'|=\\%27|/\\\'/?)\.', '\n',
'\tRedirectMatch 403 (?i)/(\$(\&)?|\*|\"|\.|,|&|&amp;?)/?$', '\n',
'\tRedirectMatch 403 (?i)(\{0\}|\(/\(|\.\.\.|\+\+\+|\\\"\\\")', '\n',
'\tRedirectMatch 403 (?i)(~|`|<|>|:|;|,|%|\\|\s|\{|\}|\[|\]|\|)', '\n',
'\tRedirectMatch 403 (?i)/(=|\$&|_mm|cgi-|etc/passwd|muieblack)', '\n',
'\tRedirectMatch 403 (?i)(&pws=0|_vti_|\(null\)|\{\$itemURL\}|echo(.*)kae|etc/passwd|eval\(|self/environ)', '\n',
'\tRedirectMatch 403 (?i)\.(aspx?|bash|bak?|cfg|cgi|dll|exe|git|hg|ini|jsp|log|mdb|out|sql|svn|swp|tar|rar|rdf)$', '\n',
'\tRedirectMatch 403 (?i)/(^$|(wp-)?config|mobiquo|phpinfo|shell|sqlpatch|thumb|thumb_editor|thumbopen|timthumb|webshell)\.php', '\n',
'</IfModule>', '\n',
'\n', '# 6G:[USER AGENTS]', '\n',
'<IfModule mod_setenvif.c>', '\n',
'\tSetEnvIfNoCase User-Agent ([a-z0-9]{2000,}) bad_bot', '\n',
'\tSetEnvIfNoCase User-Agent (archive.org|binlar|casper|checkpriv|choppy|clshttp|cmsworld|diavol|dotbot|extract|feedfinder|flicky|g00g1e|harvest|heritrix|httrack|kmccrew|loader|miner|nikto|nutch|planetwork|postrank|purebot|pycurl|python|seekerspider|siclab|skygrid|sqlmap|sucker|turnit|vikspider|winhttp|xxxyy|youda|zmeu|zune) bad_bot', '\n',
'\t# Apache < 2.3', '\n',
'\t<IfModule !mod_authz_core.c>', '\n',
'\t\tOrder Allow,Deny', '\n',
'\t\tAllow from all', '\n',
'\t\tDeny from env=bad_bot', '\n',
'\t</IfModule>', '\n',
'\t# Apache >= 2.3', '\n',
'\t<IfModule mod_authz_core.c>', '\n',
'\t\t<RequireAll>', '\n',
'\t\t\tRequire all Granted', '\n',
'\t\t\tRequire not env bad_bot', '\n',
'\t\t</RequireAll>', '\n',
'\t</IfModule>', '\n',
'</IfModule>', '\n'
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

    def createFirewall(self):
        """
        :return: None
        """
        self.writeHtaccess()