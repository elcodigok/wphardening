WPHardening [![Build Status](https://travis-ci.org/elcodigok/wphardening.svg?branch=master)](https://travis-ci.org/elcodigok/wphardening) [![Coverage Status](https://coveralls.io/repos/elcodigok/wphardening/badge.svg?branch=master&service=github)](https://coveralls.io/github/elcodigok/wphardening?branch=master)
===========

<img src="https://raw.githubusercontent.com/elcodigok/wphardening/develop/doc/images/logo-wphardening-v1.png" alt="WPHardening" title="WPHardening" height="200px" align="right" />

Fortify the security of any WordPress installation.

**❮ NOTE ❯** This tool releases new versions on a regular basis. Make sure to update your dependencies frequently to get the latest version. Check out the [changelog](https://github.com/elcodigok/wphardening/releases) or [CHANGELOG.md](https://github.com/elcodigok/wphardening/blob/master/doc/CHANGELOG.md) to learn about the new features.

-----

Installation
------------

Installing WPHardening requires you to execute one console command:

```bash
$ pip install -r requirements.txt
```

Usage
-----

    $ python wphardening.py -h 

     __          _______  _    _               _            _
     \ \        / /  __ \| |  | |             | |          (_)
      \ \  /\  / /| |__) | |__| | __ _ _ __ __| | ___ _ __  _ _ __   __ _
       \ \/  \/ / |  ___/|  __  |/ _` | '__/ _` |/ _ \ '_ \| | '_ \ / _` |
        \  /\  /  | |    | |  | | (_| | | | (_| |  __/ | | | | | | | (_| |
         \/  \/   |_|    |_|  |_|\__,_|_|  \__,_|\___|_| |_|_|_| |_|\__, |
                                                                     __/ |
            Fortify the security of any WordPress installation.     |___/
    
         Caceria de Spammers - http://www.caceriadespammers.com.ar

    Usage: python wphardening.py [options]

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
        --chown=user:group  Changing file and directory owner.
        --wp-config         Wizard generated wp-config.php
        --plugins           Download Plugins Security.
        --proxy=PROXY       Use a HTTP proxy to connect to the target url for
                            --plugins and --wp-config.
        --indexes           It allows you to display the contents of directories.
        --minify            Compressing static file .css and .js
        --malware-scan      Malware Scan in WordPress project.

      Miscellaneous:
        -o FILE, --output=FILE
                            Write log report to FILE.log


Examples
--------

### Check a WordPress Project

Before using the tool, we must ensure that our working directory is **WordPress**.

```bash
$ python wphardening.py -d /home/path/to/wordpress -v
```

### Change permissions

This option is to add the correct permissions to files and directories.

```bash
$ python wphardening.py -d /home/path/to/wordpress --chmod -v
```

### Remove files that are not used

Part of the fortification of any system is to remove those files, directories or components required.

```bash
$ python wphardening.py -d /home/path/to/wordpress --remove -v
```

### Create your robots.txt file

WordPress default does not incorporate the robots.txt file with this option poemos customize our robots.txt

```bash
$ python wphardening.py -d /home/path/to/wordpress --robots -v
```

For more information [robots.txt](http://www.robotstxt.org/)

### Remove all fingerprinting and Version

```bash
$ python wphardening.py -d /home/path/to/wordpress --fingerprinting -v
```

### Check a TimThumb library

```bash
$ python wphardening.py -d /home/path/to/wordpress --timthumb -v
```

### Create Index file

This file is created as a way to avoid sailing in a directory.

```bash
$ python wphardening.py -d /home/path/to/wordpress --indexes -v
```

### Download Plugins security

The following is a list of the most commonly used security plugins that you can download automatically:

 * [AntiVirus](https://wordpress.org/extend/plugins/antivirus/)
 * [Bad Behavior](https://wordpress.org/extend/plugins/bad-behavior/)
 * [Block Bad Queries](https://wordpress.org/extend/plugins/block-bad-queries/)
 * [Exploit Scanner](https://wordpress.org/extend/plugins/exploit-scanner/)
 * [Latch](https://wordpress.org/plugins/latch/)
 * [Simple History](https://wordpress.org/plugins/simple-history/)
 * [Stream](https://wordpress.org/plugins/stream/)
 * [WP Security Scan](https://wordpress.org/extend/plugins/wp-security-scan/)
 * [WP-DBManager](https://wordpress.org/extend/plugins/wp-dbmanager/)

```bash
$ python wphardening.py -d /home/path/to/wordpress --plugins
```

### Wizard generated wp-config.php

This command automatically creates a file called **wp-config-wphardening.php** which can then rename it.

```bash
$ python wphardening.py -d /home/path/to/wordpress --wp-config
```

### WPHardening update

With this option you can always have the latest version of WPHardening.

```bash
$ python wphardening.py --update
```

### Use all options

```bash
$ python wphardening.py -d /home/path/to/wordpress -c -r -f -t --wp-config --indexes --plugins -o /home/user/wphardening.log
```

Project Home
------------

www.caceriadespammers.com.ar


Git Repository
--------------

https://github.com/elcodigok/wphardening


Issues
------

https://github.com/elcodigok/wphardening/issues
