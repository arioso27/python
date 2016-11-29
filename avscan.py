##
## progname: avscan.py
## version:
## modify date: 2016-1126 05:30:15
## by: arioso27

#stexbar
#K:\Git\git-bash.exe -c 'py "J:\SkyDrive\work\python\avscan.py" "%sel*paths" &&read'


import sys
import os
import codecs
import re
import random
import string
import subprocess
from shlex import quote

import avpTemp
out = None

##for: generate dafault 8 chars string with lower ascii & digits
##usage: s1 = ranStr()
def ranStr( size=8, chars=string.ascii_lowercase + string.digits ):
	return ''.join( random.choice(chars) for _ in range(size) )
#_ def ranStr


def spCmd( cmd_in=None ):
	print( "--- spCmd start ---" )
	if( cmd_in is None or len(cmd_in) <= 0 ):
		print( "spCmd: command is empty" )
		out.flush()
		return 0
	#_ if
	try:
		#out_bytes = subprocess.check_output( cmd_in )
		#out_bytes = subprocess.check_output( cmd_in, shell=True, stderr=subprocess.STDOUT )
		out_bytes = subprocess.check_output( cmd_in, stderr=subprocess.STDOUT )
		##print("[",out_bytes.decode("mbcs" ), "]" )
		print( "[", out_bytes.decode("utf_8"), "]" )
	except subprocess.CalledProcessError as e:
		out_bytes = e.output  # Output generated before error
		code = e.returncode  # Return code
		print( "code=", code, "[", out_bytes, "]" )
		out.flush()
		return 0
	except:
		print( "Unexpected error:", sys.exc_info()[0] )
		out.flush()
		return 0
	#_ try
	return 1
#_ def spCmd


##
def main( argv=None ):
	global out
	sys.stdout = codecs.getwriter("utf_8")(sys.stdout.detach()) ##important
	sys.stdin = codecs.getwriter("utf_8")(sys.stdin.detach()) ##important
	out = sys.stdout

	if argv is None:
		argv = sys.argv
		# etc., replacing sys.argv with argv in the getopt() call.
	#_ if

	noArgv = len(argv)
	
	## --- Todo ---
	#print( avpTemp.avpTempStr )

	if noArgv <= 1:
		print("Error: No paths are selected ")
		exit()
	#_ if
	
	dirIN = argv[1]
	#print( "dirIN=", dirIN )

	dirIN = dirIN.strip('"')
	print( "strip dirIN="+ dirIN )
	out.flush()
	
	selxpaths = argv[1].split("*")
	#print( "type of selxpaths[0]"+ str(type(selxpaths[0])) +"[" + selxpaths[0] + "]" )
	#print( "selxpaths=", selxpaths[0].encode("utf-8").decode("utf-8") )

	print( "selxpaths lens=" + str(len(selxpaths)) )
	i = 0
	pathStr = ""
	for xp in selxpaths:
		pathStr += ("Path" + str(i) + "=" + xp + "\n" )
		
		##step for
		i += 1
	#_ for
	
	#print( "pathStr=" )
	#print ( pathStr )
	
	#avpFileStr = re.sub( r'Path0=', pathStr, avpTemp.avpTempStr )
	#avpFileStr = re.sub( r'Path0=', repr(pathStr), avpTemp.avpTempStr )
	avpFileStr = avpTemp.avpTempStr.replace( "Path0=\n", pathStr )
	print ( "---------------------" )
	print ( avpFileStr )
	out.flush()
	
	avpfile = "" + os.getenv("TEMP") + "\\" + ranStr() + ".avp"
	#print( "avpfile=" + avpfile )

	##avpio = codecs.open( avpfile, 'w', 'utf_8_sig', 'crlf_newline: true' )
	#avpio = open( avpfile, 'w', encoding='utf_8_sig', newline='\r\n' )
	avpio = open( avpfile, 'w', encoding='utf_16_le', newline='\r\n' )
	##avpio = codecs.getwriter("utf_8_sig")(avpio.detach())
	#avpio.write( codecs.BOM_UTF16_LE )
	print( "codecs.BOM_UTF16_LE=[{0}]".format( codecs.BOM_UTF16_LE ) )
	##change unix to dos
	#avpFileStr = re.sub( r"\n", "\r\n", avpFileStr )
	try:
		avpio.write( codecs.BOM_UTF16_LE.decode('utf_16_le') )
		avpio.write( avpFileStr )
	except:
		print( "ERROR: avpio.write ~ ", sys.exc_info()[0] )
	#_ try
	avpio.flush()
	rt = avpio.close()
	
	##"C:\Program Files (x86)\Avira\Antivirus\avscan.exe" /CFG="J:\SkyDrive\work\avp\scan-00.avp" /PATH="K:\download\[Software]\NppExec20160628_dll.zip" 
	#Cmd_prog = 'C:\Program Files (x86)\Avira\Antivirus\avscan.exe'
	Cmd_prog = "C:\\Program Files (x86)\\Avira\\Antivirus\\avscan.exe"
	#print( "Cmd_prog=" + Cmd_prog )

	#doCmd = [ "cat", avpfile ]
	#print( "doCmd=", doCmd )
	#out.flush()
	#rt = spCmd( doCmd )
	#out.flush()

	##doCmd = [ Cmd_prog, '/CFG=' + '"' + avpfile + '"' ]
	##doCmd = [ Cmd_prog, '/CFG=' + quote(avpfile) ]
	#doCmd = [ Cmd_prog, (r' /CFG="{0}" '.format(avpfile)) ]
	#print( "doCmd=", doCmd )
	##print( "doCmd join=" + ' '.join(doCmd) )
	#out.flush()
	
	doCC = '"{0}" /CFG="{1}"'.format( Cmd_prog, avpfile )
	print( "doCC=", doCC )
	out.flush()
	#sts = subprocess.call( doCC, shell=True )
	#sts = subprocess.call( doCC )
	rt = spCmd( doCC )

	#rt = spCmd( doCmd )
	out.flush()

#_ def main


if __name__ == "__main__":
	main()

	##sys.exit(main())
#_ if
