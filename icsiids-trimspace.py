#!/usr/bin/python
#
# A script for tidying up disk usage in logging directories.
# It takes a file glob and a size limit and removes the oldest files that
# match the glob such that the total size of the fiels does not exceed
# the file limit.  If there are no globs specified on the command line,
# it reads a list of files from stdin.

import sys
import os
import os.path
import glob
import optparse
import re
import time

prog="icsiids-trimspace"
version="%s v0.1" % prog

dateformat = "%Y-%m-%dT%T"

parser = optparse.OptionParser(prog=prog, version=version)

parser.add_option("-s", "--limit", action="store", dest="limit", help="size limit in bytes, allowed suffices {,k,m,g,t}")
parser.add_option("-v", "--verbose", action="store_true", default=False,
                  dest="verbose", help="produce diagnostic output")
parser.add_option("-n", "--noop", action="store_true", default=False,
                  dest="verbose", help="do not actually delete files")

(options,args) = parser.parse_args(sys.argv)

def error(string):
    sys.stdout.write("%s: ERROR - %s\n" % (prog, string))
    sys.exit(1)

if not options.limit:
    error("need to specify --limit option")
m = re.match(r'^(\d+)([kmgt]?)$', options.limit)
if not m:
    error("limit must be a number followed by an optional:\nk (kilobytes), m (megabytes), g (gigabytes) or t (terabytes")
limit = int(m.group(1))
unit = m.group(2)
if unit=="k":
    limit *= 1024
elif unit=="m":
    limit *= (1024*1024)
elif unit=="g":
    limit *= (1024*1024*1024)
elif unit=="t":
    limit *= (1024*1024*1024*1024)

if (options.verbose):
    sys.stdout.write("%s\n" % version)
    sys.stdout.write("limit: %i bytes\n" % limit)

if (limit<1024*1024):
    error("limit must by >=1MB")

# The list of files we are operating on
files = [ ]

# If no args, take file list from stdin
if len(args)==1:
    for line in sys.stdin:
        l = line.strip()
        if l=="":
            continue
        files.append(line.strip())
else:
# If args, treat them as globs
    for g in args[1:]:
        files += glob.glob(g)

if len(files)==0:
    error("no files found")


fstats = [ ]
for f in files:
    if os.path.isdir(f):
        error("%s is a directory" % f)
    if os.path.islink(f):
        error("%s is a soft link" % f)
    mtime = os.path.getmtime(f)
    size = os.path.getsize(f)
    fstats.append((f, mtime, size))



if (options.verbose):
    sys.stdout.write("Files:\n")
    for (f, mtime, size) in fstats:
        mtimestr = time.strftime(dateformat, time.localtime(mtime))
        sys.stdout.write("  %s: mtime=%s, %s bytes\n" % (f, mtimestr, size))
    

sys.exit(0)
