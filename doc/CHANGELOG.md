Changelog
=========

v1.5
----

- Fix #10 - Separate Class for menu.
- Fix #21 - Compressing static files.
- Fix #38 - Improve updateWPHardening class.
- Fix #49 - Improve malware scanner.
- Fix #50 - Changing file and directory owner. --chown
- Fix #51 - Unify options --fingerprinting and --delete-version
- Fix #53 - Implement option WP_ALLOW_MULTISITE
- Fix #55 - Remove statics files.
- Fix #56 - Remove Full Path Disclosure.
- Fix #57 - Remove Plugins readme.txt file.
- Fix #61 - Debug wordpress.fuzz.txt list.
- Fix #64 - Enumeration Malware scan.
- Fix #65 - Protection wp-config.php file.
- Fix #66 - Disable automatic updates.
- Fix #67 - Debug list of recommended plugins.ç
- Fix #68 - Remove Theme twentyfourteen.
- Fix #71 - Stream recommended plugin.
- Fix #72 - Simple History recommended plugin.
- Fix #73 - Override of default file permissions in wp-config.php
- Fix #77 - Integration with Travis CI.
- Fix #78 - Integration with Coveralls.
- Normalized Source Code to PEP8.
.
v1.4 (2014-11-29)
-----------------

- Add control Libwww-perl
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
