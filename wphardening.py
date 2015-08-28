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
from lib.wpconfigWordPress import wpconfigWordPress
from lib.timthumbWordPress import timthumbWordPress
from lib.updateWPHardening import updateWPHardening
from lib.malwareScanWordPress import malwareScanWordPress
from lib.loadConfWordPress import loadConfWordPress
from lib.termcolor import colored
from lib.registerLog import registerLog
import os
import sys
import urllib2


def main():
    usage = "usage: %prog [options] arg"
    version = colored('WPHardening', 'green') + ' version' + \
        colored(' 1.5-dev', 'yellow')
    parser = OptionParser(usage, version=version)
    parser.add_option(
        "-v", "--verbose", action="store_true", dest="verbose",
        default=False, help="Active verbose mode output results",
    )
    parser.add_option(
        "--update", action="store_true", dest="update",
        default=False, help="Check for WPHardening latest stable version"
    )
    group1 = OptionGroup(
        parser, "Target",
        "This option must be specified to modify the package WordPress."
    )
    group1.add_option(
        "-d", "--dir", dest="path",
        help="**REQUIRED** - Working Directory.", metavar="DIRECTORY"
    )
    group1.add_option(
        "--load-conf", dest="loadconf", metavar="FILE",
        help="Load file configuration."
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
        "-t", "--timthumb", action="store_true", dest="timthumb",
        help="Find the library TimThumb."
    )
    group2.add_option(
        "--wp-config", action="store_true", dest="wpconfig",
        help="Wizard generated wp-config.php"
    )
    #group2.add_option(
        #"--delete-version", action="store_true",
        #dest="delete_version", help="Deleted version WordPress."
    #)
    group2.add_option(
        "--plugins", action="store_true", dest="plugins",
        help="Download Plugins Security."
    )
    group2.add_option(
        "--proxy", action="store", type="string", dest="proxy",
        help="Use a HTTP proxy to connect to the target url for --plugins and \
--wp-config."
    )
    group2.add_option(
        "--indexes", action="store_true", dest="indexes",
        help="It allows you to display the contents of directories."
    )
    group2.add_option(
        "--malware-scan", action="store_true", dest="malwares",
        help="Malware Scan in WordPress project."
    )
    parser.add_option_group(group2)

    group3 = OptionGroup(
        parser, "Miscellaneous",
    )
    group3.add_option(
        "-o", "--output", help="Write log report to FILE.log", metavar="FILE",
        dest="output"
    )
    parser.add_option_group(group3)

    (options, args) = parser.parse_args()

    if options.loadconf is not None:
        options.path = loadConfWordPress(options.loadconf).getDirectory()
        #options.delete_version = loadConfWordPress(options.loadconf).getDeleteVersion()
        options.chmod = loadConfWordPress(options.loadconf).getChmod()
        options.robots = loadConfWordPress(options.loadconf).getRobots()
        options.finger = loadConfWordPress(options.loadconf).getFingerprinting()
        options.wpconfig = loadConfWordPress(options.loadconf).getWpConfig()
        options.indexes = loadConfWordPress(options.loadconf).getIndexes()
        options.timthumb = loadConfWordPress(options.loadconf).getTimthumb()
        options.malwares = loadConfWordPress(options.loadconf).getMalwareScan()
        options.output = loadConfWordPress(options.loadconf).getOutput()

    if options.output is None:
        filename = 'wphardening.log'
    else:
        filename = options.output
    log = registerLog(filename)
    log.setConfigure()

    if options.update:
        log.add("Check for WPHardening latest stable version")
        updateWPHardening(os.path.abspath(".")).update()
        sys.exit()

    if options.path is None:
        log.add("Did not specify a working directory.")
        parser.print_help()
        sys.exit()

    options.path = os.path.abspath(options.path)
    if os.path.exists(options.path):
        if checkWordpress(options.path, options.verbose).isWordPress():
            #if options.delete_version is not None:
            #    deleteVersionWordPress(options.path).delete()
            if options.chmod is not None:
                chmodWordPress(options.path, options.verbose).changePermisions()
            if options.robots is not None:
                robotsWordPress(options.path).createRobots()
            if options.finger is not None:
                deleteVersionWordPress(options.path).delete()
                fingerprintingWordPress(options.path, options.verbose).searchStaticFile()
            if options.wpconfig is not None:
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
                    asdf = wpconfigWordPress(options.path, options.proxy)
                else:
                    asdf = wpconfigWordPress(options.path, options.proxy)
                asdf.createConfig()
            if options.indexes is not None:
                indexesWordPress(options.path, options.verbose).createIndexes()
            if options.timthumb is not None:
                timthumbWordPress(options.path).checkTimbthumb()
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
            if options.malwares is not None:
                malwareScanWordPress(options.path).scan()
            if options.remove is not None:
                removeWordPress(options.path).delete()
    else:
        log.add("Could not find the specified directory.")
        print colored('\nCould not find the specified directory.\n', 'red')

if __name__ == "__main__":
    main()
