##
## progname: ttva.py
## version: 1.03
## modify date: 2016-1128 01:25:35
## by: arioso27
## for: write a utf_16_le file with BOM


import sys
import os
import codecs
import random
import string
from datetime import datetime
import time

out = None

##for: generate dafault 8 chars string with lower ascii & digits
##usage: s1 = ranStr()
def ranStr( size=8, chars=string.ascii_lowercase + string.digits ):
	return ''.join( random.choice(chars) for _ in range(size) )
#_ def ranStr


##main part
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
	avpfile = "" + os.getenv("TEMP") + "\\" + ranStr() + ".avp"
	print( "avpfile=" + avpfile )

	now = datetime.now()
	nowStr = now.strftime( "%m%d-%H%M" )
	nowWeek = now.strftime( "%w" )

	print( "nowStr = "+ nowStr )
	print( "nowWeek = "+ nowWeek )
	mTime = time.localtime( )
	locTime = time.strftime( "%Y-%m%d %H:%M:%S", mTime )
	print( "locTime = "+ locTime )
	out.flush()

	try:
		avpio = open( avpfile, 'wb' )
		avpio.write( codecs.BOM_UTF16_LE )
		avpio.write( "test line 1\r\nLine 22\r\n".encode('utf_16_le') )
		avpio.write( "Line 333\r\n".encode('utf_16_le') )
		avpio.write( "--- {0} ---\r\n".format(locTime).encode('utf_16_le') )
		
		avpio.flush()
		rt = avpio.close()
	except:
		print( "Unexpected error:", sys.exc_info()[0] )
		out.flush()
	#_ try


#_ def main


if __name__ == "__main__":
	main()

	##sys.exit(main())
#_ if
