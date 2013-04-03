WPHardening
===========

WPHardening fortification is a security tool for WordPress


Usage
=====

    $ python wphardening.py -h 
    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -v, --verbose         active verbose mode output results

      Target:
        This option must be specified to modify the package WordPress.
    
        -d DIRECTORY, --dir=DIRECTORY
                            **REQUIRED** - Working Directory.

      Hardening:
        Different tools to hardening WordPress.
    
        -c, --chmod         Chmod 755 in directory and 644 in files.
        -r, --remove        Remove files and directory.
        -b, --robots        Create file robots.txt
        -f, --fingerprinting
                            Deleted fingerprinting WordPress.
        --delete-version    Deleted version WordPress.
        --plugins           Download Plugins Security.
    
      Miscellaneous:
        --wizard            Simple wizard interface for beginner users


Examples
========

    $ python wphardening.py -d /home/user/wordpress -c -r -f --delete-version
