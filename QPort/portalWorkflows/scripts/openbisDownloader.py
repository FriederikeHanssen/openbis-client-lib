#!/usr/bin/env python
import sys, os
tmpFolder = os.environ["TMP"] 
resultFolder = tmpFolder
OUTPUT = 'workflow.input' 
cmdLine = 'getdataset -o '+ resultFolder + ' -r ' + OUTPUT
if len(sys.argv) < 2:
	sys.stderr.write("usage: ./openbisDownloader.py <input file> \n\n")
	sys.exit(1)

	
file_number = 0
if(not os.path.exists(resultFolder)):
	os.system('mkdir '+resultFolder)

for line in open(sys.argv[1], "r"):
	print '****************************************************'
	print line
	if (line.strip()):
		splittedLine = line.split('=')
		print(splittedLine[0])
		print(splittedLine[1])
		cmd = ''.join((cmdLine,splittedLine[1])) #cmdLine + splittedLine
		print cmd
		exit_code = os.system(cmd)
##		if exit_code != 0:
##			sys.stderr.write(cmdLine + " exited with status: " + str(exit_code) + "\n")
##		else:
##			print(cmdLine + " executed successfully")
		file_number += 1
	
#print("Downloaded " + str(file_number) + " files.")
