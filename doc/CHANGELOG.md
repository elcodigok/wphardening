Changelog
=========

v1.5
----

### Featured

- Compressing static files (Fix #21).
- Changing file and directory owner. --chown (Fix #50).
- Implement option WP_ALLOW_MULTISITE (Fix #53).
- Remove Plugins readme.txt file (Fix #57).
- Enumeration Malware scan (Fix #64).
- Disable automatic updates (Fix #66).
- Remove Theme twentyfourteen (Fix #68).
- Stream recommended plugin (Fix #71).
- Simple History recommended plugin (Fix #72).
- Override of default file permissions in wp-config.php (Fix #73).
- Integration with Travis CI (Fix #77).
- Integration with Coveralls (Fix #78).

### Improvement

- Separate Class for menu (Fix #10).
- Improve malware scanner (Fix #49).
- Unify options --fingerprinting and --delete-version (Fix #51).
- Remove statics files (Fix #55).
- Protection wp-config.php file (Fix #65).
- Debug list of recommended plugins (Fix #67).
- Normalized Source Code to PEP8.
- WPHardening compatible with WordPress 4.1.1, 4.1.2, 4.2, 4.2.1, 4.2.2, 4.2.3, 4.2.4 and 4.3

### Bug

- Improve updateWPHardening class (Fix #38).
- Remove Full Path Disclosure (Fix #56).
- Debug wordpress.fuzz.txt list (Fix #61).


v1.4 (2014-11-29)
-----------------

- Add control Libwww-perl.
- Optimization source code.
- New set default vales in --wp-config
- Add Query string Exploits.
- Validation input options.
- Add error_reporting(0);
- Add @ini_set('display_errors', 0);
- Add filter login_error.
- Add Options Memori Limit in --wp-config
- Print version Timthumb library.
- Create new options --malware-scan
- Avoid Full Path Disclosure.
- New structure to eliminate themes.
- Create new options --load-conf


v1.3 (2014-07-31)
-----------------

- Change function wp_admin_css().
- Improved wordpress.fuzz.txt list.
- Handle the error when no Internet connection detected pluginsWordPress.py
- Handle the error when no Internet connection detected wpconfigWordPress.py
- Latch recommended plugin.
- Rename variable names.
- Improving detection of WordPress projects.
- Add auto-update core.
- Add a library to find timthumb.php
- Updated of PEP8 in the file wpconfigWordPress.py
- Updated of PEP8 in the file pluginsWordPress.py
- Full functionality with verbose mode.
- WPHardening compatible with WordPress 3.9, 3.9.1 and 3.9.2


v1.2 (2014-03-16)
-----------------

- New option in --wp-config to desctivar wp-cron.php
- Improvements in the new function to disable wp-cron.php
- Remove unsed libraries.
- New file extensions to modify fingerprintingWordPress.
- DISALLOW_UNFILTERED_HTML in wp-config-wphardening.php
- chmod 0640 to the file wp-config-wphardening.php
- FORCE_SSL_LOGIN and FORCE_SSL_ADMIN to the file wp-config-wphardening.php


v1.1 (2013-05-02)
-----------------

- License GPLv3 to all files in the source code.
- Protection for the .htaccess file.
- New record of activities in log file.
- New --wp-config option to generate the configuration file.
- Entering the URL option --robots


v1.0 (2013-04-12)
------------------

- New options --plugins
- New options -f --fingerprinting
- Create file robots.txt
- New options for changemod -c
- New options --indexes
- New options --delete-version
- Normalized PEP8.
