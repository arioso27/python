##
## progname: ttRe00.py
## version: 1.00
## modify date: 2016-1204 03:08:37
## by: arioso27

import sys
import os
import codecs
import re

out = None

bl40 = ''.join( '-' for _ in range(40) )
bl60 = '-' * 60

def main( argv=None ):
	sys.stdout = codecs.getwriter("utf_8")(sys.stdout.detach()) ##important
	sys.stdin = codecs.getwriter("utf_8")(sys.stdin.detach()) ##important
	global out
	out = sys.stdout

	if argv is None:
		argv = sys.argv
		# etc., replacing sys.argv with argv in the getopt() call.
	#_ if

	noArgv = len(argv)
	
	## --- Todo ---
	pathStr = "j:\\temp\\00.txt"
	TempStr = '''\
Add new file [Path0] for write
Count file [Path0] lines [Line0]
'''
	print( bl40 )
	print( "try 1:" )
	outStr = re.sub( r'Path0', pathStr, TempStr )
	print( outStr )
	print( bl40 )
	print( "try 2:" )
	outStr = re.sub( r'Path0', r'{0}'.format(pathStr), TempStr )
	print( outStr )
	print( bl40 )
	print( "try 3:" )
	outStr = re.sub( r'Path0', re.sub( r'\\', r'\\\\', pathStr), TempStr )
	print( outStr )
	print( bl40 )
	
	pathStr1 = os.path.normpath( "j:/temp/00.txt" )
	print( "try 4:" )
	outStr = re.sub( r'Path0', pathStr1, TempStr )
	print( outStr )
	print( bl40 )

	print( "try 5:" )
	outStr = re.sub( r'Path0', lambda x: not x.group(0) or pathStr, TempStr )
	print( outStr )
	print( bl60 )

	
	
	#avpFileStr = re.sub( r'Path0=', repr(pathStr), avpTemp.avpTempStr )


#_ def main


if __name__ == "__main__":
	main()

	##sys.exit(main())
#_ if
