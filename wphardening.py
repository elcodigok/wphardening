#!/usr/bin/env python
"""
wphardening.py

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

from optparse import OptionParser, OptionGroup
from lib.checkWordpress import checkWordpress
from lib.chmodWordPress import chmodWordPress
from lib.removeWordPress import removeWordPress
from lib.robotsWordPress import robotsWordPress
from lib.deleteVersionWordPress import deleteVersionWordPress
from lib.fingerprintingWordPress import fingerprintingWordPress
from lib.pluginsWordPress import pluginsWordPress
from lib.indexesWordPress import indexesWordPress
from lib.termcolor import colored, cprint
from lib.registerLog import registerLog
import os
import sys
import urllib2


def main():
    usage = "usage: %prog [options] arg"
    version = colored('WP Hardening', 'green') + ' version' + \
        colored(' 1.1 - Beta', 'yellow')
    parser = OptionParser(usage, version=version)
    parser.add_option(
        "-v", "--verbose", action="store_true", dest="verbose",
        help="active verbose mode output results",
    )
    group1 = OptionGroup(
        parser, "Target",
        "This option must be specified to modify the package WordPress."
    )
    group1.add_option(
        "-d", "--dir", dest="path",
        help="**REQUIRED** - Working Directory.", metavar="DIRECTORY"
    )
    parser.add_option_group(group1)

    group2 = OptionGroup(
        parser, "Hardening", "Different tools to hardening WordPress."
    )
    group2.add_option(
        "-c", "--chmod", action="store_true", dest="chmod",
        help="Chmod 755 in directory and 644 in files."
    )
    group2.add_option(
        "-r", "--remove", action="store_true", dest="remove",
        help="Remove files and directory."
    )
    group2.add_option(
        "-b", "--robots", action="store_true", dest="robots",
        help="Create file robots.txt"
    )
    group2.add_option(
        "-f", "--fingerprinting", action="store_true",
        dest="finger", help="Deleted fingerprinting WordPress."
    )
    group2.add_option(
        "--delete-version", action="store_true",
        dest="delete_version", help="Deleted version WordPress."
    )
    group2.add_option(
        "--plugins", action="store_true", dest="plugins",
        help="Download Plugins Security."
    )
    group2.add_option(
        "--proxy", action="store", type="string", dest="proxy",
        help="Use a HTTP proxy to connect to the target url for --plugins."
    )
    group2.add_option(
        "--indexes", action="store_true", dest="indexes",
        help="It allows you to display the contents of directories."
    )
    parser.add_option_group(group2)
    
    group3 = OptionGroup(
        parser, "Miscellaneous",
    )
    group3.add_option(
        "-o", "--output", help="Write log report to FILE.", metavar="FILE",
        dest="output"
    )
    parser.add_option_group(group3)

    (options, args) = parser.parse_args()
    
    if options.output is None:
        filename = 'wphardening.log'
    else:
        filename = options.output
    log = registerLog(filename)
    log.setConfigure()

    if options.path is None:
        log.add("Did not specify a working directory.")
        parser.print_help()
        sys.exit()

    options.path = os.path.abspath(options.path)
    if os.path.exists(options.path):
        wordpress = checkWordpress(options.path)
        if wordpress.isWordPress():
            print colored(options.path, 'yellow') + ' -', \
                colored('This project directory is a WordPress.\n', 'green')
            if options.delete_version is not None:
                asdf = deleteVersionWordPress(options.path)
                asdf.delete()
            if options.chmod is not None:
                asdf = chmodWordPress(options.path)
                asdf.changePermisions()
            if options.remove is not None:
                qwer = removeWordPress(options.path)
                qwer.delete()
            if options.robots is not None:
                zxcv = robotsWordPress(options.path)
                zxcv.createRobots()
            if options.finger is not None:
                asdf = fingerprintingWordPress(options.path)
                asdf.searchStaticFile()
            if options.plugins is not None:
                if options.proxy is not None:
                    protocolo, rest = urllib2.splittype(options.proxy)
                    if protocolo is None:
                        raise ValueError("unknown URL type: %s") % \
                            (options.proxy)
                    host, rest = urllib2.splithost(rest)
                    host, port = urllib2.splitport(host)
                    if port is None:
                        raise ValueError("unknown protocol for %s") % \
                            (options.proxy)
                    puerto = int(port)
                    asdf = pluginsWordPress(options.path, options.proxy)
                else:
                    asdf = pluginsWordPress(options.path, options.proxy)
                asdf.questions()
            if options.indexes is not None:
                asdf = indexesWordPress(options.path)
                asdf.createIndexes()
        else:
            log.add(options.path + " This Project directory is not a WordPress.")
            print colored(options.path, 'yellow') + ' -', \
                colored('This Project directory is not a WordPress.\n', 'red')
    else:
        log.add("Could not find the specified directory.")
        print colored('\nCould not find the specified directory.\n', 'red')

if __name__ == "__main__":
    main()
