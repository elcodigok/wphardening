Changelog
=========

v1.6
----

### Featured

- Remove Theme twentyfifteen (FIX #82).
- Checking static files (FIX #83).
- Change url in Plugins, add https:// (FIX #87).
- Add Ninja Firewall Plugin for WordPress (FIX #81).
- Change permission 444 to wp-config-wphardening.php (FIX #95).
- Information Leak file error_log (FIX #97).
- Add 6G Firewall 2016 (FIX #88).
- Header X-Content-Type-Options (FIX #98).
- Security Headers - X-Frame-Options (FIX #100).
- Headers - X-XSS-Protection (FIX #99).
- Add WPS Hide Login Plugin for WordPress (FIX #107).
- Disable REST API (FIX #85).

### Improvement

- WPHardening compatible with WordPress 4.4, 4.4.1, 4.4.2, 4.5, 4.5.1, 4.5.2, 4.5.3, 4.6, 4.6.1, 4.7, 4.7.1, 4.7.2, 4.7.3 and 4.7.4
- Empty Trash 5 days (FIX #101).
- Disable Javascript Concatenation (FIX #105).
- Delete watermark on every files (FIX #92).

v1.5
----

### Featured

- Compressing static files *.css and *.js --minify (FIX #21).
- Changing file and directory Owner. --chown (FIX #50).
- Implement option WP_ALLOW_MULTISITE in wp-config.php (FIX #53).
- Remove Plugins readme.txt file (FIX #57).
- Enumeration Malware Scan (FIX #64).
- Disable automatic updates (FIX #66).
- Remove Theme Twentyfourteen (FIX #68).
- Stream recommended plugin (FIX #71).
- Simple History recommended plugin (FIX #72).
- Override of default file permissions in wp-config.php (FIX #73).
- Integration with Travis CI (FIX #77).
- Integration with Coveralls (FIX #78).

### Improvement

- Separate Class for menu (FIX #10).
- Improve malware scanner (FIX #49).
- Unify options --fingerprinting and --delete-version (FIX #51).
- Remove statics files (FIX #55).
- Protection wp-config.php file with .htaccess (FIX #65).
- Debug list of recommended plugins (FIX #67).
- Normalized Source Code to PEP8.
- WPHardening compatible with WordPress 4.1.1, 4.1.2, 4.2, 4.2.1, 4.2.2, 4.2.3, 4.2.4 and 4.3

### Bug

- Improve updateWPHardening class (FIX #38).
- Remove Full Path Disclosure (FIX #56).
- Debug data/wordpress.fuzz.txt list (FIX #61).
- Remove options php_flag display_errors off (FIX #79).


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
