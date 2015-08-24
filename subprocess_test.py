import subprocess, re, time, os, logging
from os.path import exists

resultFile = 'result'

#1. Get the selected software ready
function = raw_input('Please enter the software you would like to use:')
#1.1 construct the function folder
try:
	functionDir = os.path.join('.', function)
	if os.path.exists(functionDir):
		print '%s already exists', functionDir
	else:
		os.mkdir(functionDir)
except StandardError,e:
	print 'function directory construction failure:', e
	logging.exception(e)
#1.2 construct the testee result file
testeeDir = raw_input('Please enter the programs you would like to test:')
if not os.path.exists(testeeDir):
	raise ValueError('this path doesn\'t exist. Please check the input and enter it again.')
#1.2.1 if testeeDir is a directory
if os.path.isdir(testeeDir):
	if testeeDir.endswith('/'):
		testeeDir = testeeDir.rstrip('/')
	if not testeeDir == '':
		testeeDir = os.path.split(testeeDir)[1]
		testeeDir = os.path.join(functionDir, testeeDir)
		if not os.path.exists(testeeDir):
			os.mkdir(testeeDir)
		else:
			print '%s already exists' % testeeDir
	else:
		raise ValueError('testDir should not be empty or only contains \'/\' or \'\\\'')
else: #1.2.2 if testeeDir is a file
	testeeDir = os.path.split(testeeDir)[1]  #file name with extentions
	testeeDir = testeeDir.split(r'.')[0]  #file name only without extentions
	testeeDir = os.path.join(functionDir, testeeDir)
	if not os.path.exists(testeeDir):
		os.mkdir(testeeDir)
	else:
		print '%s already exists' % testeeDir	
#endof if...else...

#1.3 Get the resultFile ready
timeTail = int(time.time())
resultFileName = resultFile + str(timeTail) + '.txt'  #name230984209.txt
resultFileDir = os.path.join(testeeDir, resultFileName)

#2. Subprocess call the software and generate outputs
try:
	command = "cppcheck --enable=all G:\program\cpp\SolarRadiation-master 2> %s" % resultFileDir
	print command
	subprocess.check_call(command, shell=True)
except StandardError, e:
	print 'Encounter StandardError: ', e
#resultFile.close()
#endof open(resultDir, 'a') as resultFile:

#3. Consolidate all the outputs

























