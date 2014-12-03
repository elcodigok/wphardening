WPHardening
===========

WPHardening fortification is a security tool for WordPress


Usage
=====

    $ python wphardening.py -h 
    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -v, --verbose         Active verbose mode output results
      --update              Check for WPHardening latest stable version

      Target:
        This option must be specified to modify the package WordPress.
    
        -d DIRECTORY, --dir=DIRECTORY
                            **REQUIRED** - Working Directory.
        --load-conf=FILE    Load file configuration.

      Hardening:
        Different tools to hardening WordPress.
    
        -c, --chmod         Chmod 755 in directory and 644 in files.
        -r, --remove        Remove files and directory.
        -b, --robots        Create file robots.txt
        -f, --fingerprinting
                            Deleted fingerprinting WordPress.
        -t, --timthumb      Find the library TimThumb.
        --wp-config         Wizard generated wp-config.php
        --delete-version    Deleted version WordPress.
        --plugins           Download Plugins Security.
        --proxy=PROXY       Use a HTTP proxy to connect to the target url for
                            --plugins and --wp-config.
        --indexes           It allows you to display the contents of directories.
        --malware-scan      Malware Scan in WordPress project.
    
      Miscellaneous:
        -o FILE, --output=FILE
                            Write log report to FILE.log


Examples
========

Check a WordPress Project

    $ python wphardening.py -d /home/path/wordpress -v

Change permissions

    $ python wphardening.py -d /home/path/wordpress --chmod -v

Remove files that are not used

    $ python wphardening.py -d /home/path/wordpress --remove -v

Create your robots.txt file

    $ python wphardening.py -d /home/path/wordpress --robots -v

Remove all fingerprinting

    $ python wphardening.py -d /home/path/wordpress --fingerprinting -v

Check a TimThumb library

    $ python wphardening.py -d /home/path/wordpress --timthumb -v

Create Index file

    $ python wphardening.py -d /home/path/wordpress --indexes -v

Download Plugins security

    $ python wphardening.py -d /home/path/wordpress --plugins

Wizard generated wp-config.php

    $ python wphardening.py -d /home/path/wordpress --wp-config

Deleted version WordPress

    $ python wphardening.py -d /home/path/wordpress --delete-version -v

WPHardening update

    $ python wphardening.py --update

Use all options

    $ python wphardening.py -d /home/user/wordpress -c -r -f -t --wp-config --delete-version --indexes --plugins -o /home/user/wphardening.log


Project Home
============

www.caceriadespammers.com.ar


Git Repository
==============

https://github.com/elcodigok/wphardening


Issues
======

https://github.com/elcodigok/wphardening/issues