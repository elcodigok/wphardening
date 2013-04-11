import fnmatch
import os
import os.path
import re
import datetime
from lib.termcolor import colored, cprint


class fingerprintingWordPress():
    def __init__(self, directory):
        self.directory = os.path.abspath(directory)
        # for files only
        self.includes = ['*.js', '*.css']
        self.includes = r'|'.join(
            [fnmatch.translate(x) for x in self.includes]
        )

    def searchStaticFile(self):
        for root, dirs, files in os.walk(self.directory):
            dirs[:] = [os.path.join(root, d) for d in dirs]

            # exclude/include files
            files = [os.path.join(root, f) for f in files]
            files = [f for f in files if re.match(self.includes, f)]

            for fname in files:
                f = open(fname, "r")
                script = f.readlines()
                f.close()
                f = open(fname, "w")
                f.writelines(self.getDateTime() + script)
                f.close()
        print colored('\nDeleted fingerprinting WordPress', 'yellow')
        print colored('\tAll changes implemented.', 'green')

    def getDateTime(self):
        self.now = [
            '/* WP Hardening - ', str(datetime.datetime.now()) + '*/\n'
        ]
        return self.now
