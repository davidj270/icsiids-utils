#!/usr/bin/python
#
# A script for tidying up disk usage in logging directories.
# It takes a file glob and a size limit and removes the oldest files that
# match the glob such that the total size of the fiels does not exceed
# the file limit

import sys
import os
import glob
import os.path
import optparse
import re
prog="icsiids-trimspace"
version="%s v0.1" % prog

parser = optparse.OptionParser(prog=prog, version=version)

parser.add_option("--size", action="store", default="0", dest="limit", help="size limit suffix {,k,m,g,t}")
parser.add_option("-v", "--verbose", action="store_true", default=False,
                  dest="verbose")
parser.add_option("-n", "--noop", action="store_true", default=False,
                  dest="verbose", help="do not actually delete files")

(options,args) = parser.parse_args(sys.argv)

if (options.verbose):
    sys.stdout.write("%s\n" % version)

files = [ ]
for g in args:
    files += glob.glob(g)

if (options.verbose):
    sys.stdout.write("Files:\n")
    for f in files:
        sys.stdout.write("  %s\n" % f)


sys.exit(0)
