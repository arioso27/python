##
## progname: ttRe00.py
## version: 1.00
## modify date: 2016-1204 23:10:37
## by: arioso27

import sys
import os
import codecs
import re

out = None

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
	pathStr = r"\\192.168.1.23:\pub\t05.zip"
	TempStr = r'''
C:\Users\JJ\Downloads\t00.zip
C:\Users\JJ\Downloads\t20.zip

C:\Users\GiGi\Downloads\t01.zip
C:\Users\GiGi\Downloads\s01.zip

C:\Users\KiKi\Downloads\t02.zip
C:\Users\KiKi\Downloads\w00.zip
'''
	
	##replace users Downloads t00~t04.zip

	print( bl60 )
	print( "try 1:" )
	rP = r"C:\\Users\\(\w+)\\Downloads\\t0[0-4].zip"
	outStr = re.sub( rP, re.sub( r'\\', r'\\\\', pathStr), TempStr )
	print( outStr )
	print( bl60 )
	
	print( "try 2:" )
	outStr = re.sub( rP, lambda x: not x.group(0) or pathStr, TempStr )
	print( outStr )
	print( bl60 )

	
	
	#avpFileStr = re.sub( r'Path0=', repr(pathStr), avpTemp.avpTempStr )


#_ def main


if __name__ == "__main__":
	main()

	##sys.exit(main())
#_ if
