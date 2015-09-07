WPHardening [![Build Status](https://travis-ci.org/elcodigok/wphardening.svg?branch=master)](https://travis-ci.org/elcodigok/wphardening) [![Coverage Status](https://coveralls.io/repos/elcodigok/wphardening/badge.svg?branch=master&service=github)](https://coveralls.io/github/elcodigok/wphardening?branch=master)
===========

WPHardening fortification is a security tool for WordPress

**❮ NOTE ❯** This tool releases new versions on a regular basis. Make sure to update your dependencies frequently to get the latest version. Check out the [changelog](https://github.com/elcodigok/wphardening/releases) or [CHANGELOG.md](https://github.com/elcodigok/wphardening/blob/master/doc/CHANGELOG.md) to learn about the new features.

-----

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
              Fortification is a Security Tool for WordPress.       |___/
    


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


Installation
------------

Installing WPHardening requires you to execute one console command:

```bash
$ pip install -r requirements.txt
```

Examples
--------

Check a WordPress Project

```bash
$ python wphardening.py -d /home/path/to/wordpress -v
```

Change permissions

```bash
$ python wphardening.py -d /home/path/to/wordpress --chmod -v
```

Remove files that are not used

```bash
$ python wphardening.py -d /home/path/to/wordpress --remove -v
```

Create your robots.txt file

```bash
$ python wphardening.py -d /home/path/to/wordpress --robots -v
```

Remove all fingerprinting and Version

```bash
$ python wphardening.py -d /home/path/to/wordpress --fingerprinting -v
```

Check a TimThumb library

```bash
$ python wphardening.py -d /home/path/to/wordpress --timthumb -v
```

Create Index file

```bash
$ python wphardening.py -d /home/path/to/wordpress --indexes -v
```

Download Plugins security

```bash
$ python wphardening.py -d /home/path/to/wordpress --plugins
```

Wizard generated wp-config.php

```bash
$ python wphardening.py -d /home/path/to/wordpress --wp-config
```

WPHardening update

```bash
$ python wphardening.py --update
```

Use all options

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
