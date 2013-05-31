#!/usr/bin/env python
#
# tombstone.py
#
# @pyver: ~2.7
# @author: fei
# @since: 2013-05-31
#

import optparse
import subprocess

# add options
parser = optparse.OptionParser()
parser.add_option('-n', '--ndk', dest='ndk', help='NDK ROOT')
parser.add_option('-t', '--tomb', dest='tomb', help='tombstone file')
parser.add_option('-s', '--sym', dest='sym', help='SYM ROOT')
parser.add_option('-o', '--obfile', dest='obfile', help='obfile file (.so)')
parser.add_option('-g', '--target', dest='target', help='target architecture')
parser.add_option('-a', '--addr2line', dest='addr2line', help='addr2line path')
# parse
(options, args) = parser.parse_args()


# exit on missing options
if not(options.ndk and options.tomb and options.sym and options.obfile and options.addr2line):
	parser.print_help()
	exit()
else:
	print "\nStacktrace for %s according to %s\n" %( options.tomb, options.obfile)
	#
	# get stack trace from tombstone
	#NDK_ROOT/ndk-stack -sym SYM_ROOT -dump tombstone
	ndkstack = "%s/%s" %( options.ndk, "ndk-stack")
	call = "%s -sym %s -dump %s" %( ndkstack, options.sym, options.tomb)
	args = ( ndkstack, "-sym", options.sym, "-dump", options.tomb )
	proc = subprocess.Popen( args, stdout=subprocess.PIPE)
	lines = []
	for line in proc.stdout.readlines():
		if line.find( options.obfile) >= 0:
			i = line.find( "pc") + 3
			temp = line[i : i+8]
			lines.append( temp)

	#lines = " ".join( lines)
	
	addr2line = "%s/%s" %( options.ndk, options.addr2line)
	obfile = "%s/%s/%s" %( options.sym, options.target, options.obfile)
	args = [ addr2line, "-Cfsp", "-e", obfile ] + lines
	proc = subprocess.Popen( args, stdout=subprocess.PIPE)
	
	for line in proc.stdout.readlines():
		print line[:-1]

