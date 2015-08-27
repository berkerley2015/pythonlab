import subprocess, re, time, os, logging
import pdb
from os.path import exists

logging.basicConfig(level=logging.INFO)

#This function is used to assemble command string
def commandAssembly(functionKey, testeeDir, testeeResultDir, resultFileName):  
	#function--map key, testeeDir--test file directory, testeeResultDir--test result directory, resultFile--initial name of the result file
	functionTuple = commandTemplateMap[functionKey]
	functionName = functionTuple[0]
	functionArgs = functionTuple[1]
	
	functionCall = functionName + ' ' + functionArgs
	if len(functionTuple) == 3:  #indicate there is a command loader attached
		functionCall = functionTuple[2] + ' ' + functionCall
	#endof if(functionTuple) == 3
	#resultFileName = functionKey + '-' + resultFile + '-' + str(int(time.time())) + '.txt'
	resultFileDir = os.path.join(testeeResultDir, resultFileName)
	#logging.info('functionCall is-->%s' % functionCall)
	#print 'functionCall is-->%s' % functionCall
	command = functionCall % (testeeDir, resultFileDir)
	#logging.info('command is-->%s' % command)
	print 'command is-->%s' % command
	return command
#endof callFunction(function)


absolutePath = os.path.dirname(os.path.abspath(__file__))
resultFile = 'result'
commandTemplateMap = {
	'cppcheck' : (r'D:\Tools\Cppcheck\cppcheck.exe', '--enable=all %s 2> %s'),  
	#the first element in the tuple is the address of the command and the second the needed arguments
	'pmd' : (r'D:\Tools\PMD\pmd-bin-5.3.3\bin\cpd.bat', '--minimum-tokens 100 --files %s --language cpp > %s'),
	'cpplint' : (r'D:\Tools\styleguide\cpplint\cpplint.py', '%s 2> %s', 'python')
}

#1. Get the selected software ready
functionKey = raw_input('Please enter the software you would like to use:')
#1.1 construct the function folder
try:
	functionDir = os.path.join(absolutePath, functionKey)
	if os.path.exists(functionDir):
		print '%s already exists', functionDir
	else:
		os.mkdir(functionDir)
except StandardError,e:
	print 'function directory construction failure:', e
	logging.exception(e)
#1.2 construct the testee result file
testeeDir = raw_input('Please enter the programs you would like to test:')
testeeResultDir = testeeDir
if not os.path.exists(testeeDir):
	raise ValueError('this path doesn\'t exist. Please check the input and enter it again.')
#1.2.1 if testeeDir is a directory
if os.path.isdir(testeeDir):
	if testeeDir.endswith('/'):
		testeeResultDir = testeeDir.rstrip('/')
	if not testeeDir == '':
		testeeResultDir = os.path.split(testeeDir)[1]
		testeeResultDir = os.path.join(functionDir, testeeResultDir)
		if not os.path.exists(testeeResultDir):
			os.mkdir(testeeResultDir)
		else:
			print '%s already exists' % testeeResultDir
	else:
		raise ValueError('testDir should not be empty or only contains \'/\' or \'\\\'')
else: #1.2.2 if testeeResultDir is a file
	testeeResultDir = os.path.split(testeeDir)[1]  #file name with extentions
	testeeResultDir = testeeResultDir.split(r'.')[0]  #file name only without extentions
	testeeResultDir = os.path.join(functionDir, testeeResultDir)
	if not os.path.exists(testeeResultDir):
		os.mkdir(testeeResultDir)
	else:
		print '%s already exists' % testeeResultDir	
#endof if...else...

#1.2.2 Get the resultFile absolute path ready
resultFileName = functionKey + '-' + resultFile + '-' + str(int(time.time())) + '.txt'

#2. Subprocess calljlk the software and generate outputs
try:
	if not functionKey == 'all':
		
		command = commandAssembly(functionKey, testeeDir, testeeResultDir, resultFileName)
		print 'command is:', command
		subprocess.call(command, shell=True)
		print 'result %s gets generated' % resultFileName
	else:  #call all 
		#pass  #need finishing later
		for functionKey in commandTemplateMap:
			#pdb.set_trace()
			#logging.info('functionKey is %s' % functionKey)
			command = commandAssembly(functionKey, testeeDir, testeeResultDir, resultFileName)
			subprocess.call(command, shell=True)
		#endof for...in...
except StandardError, e:
	print 'Encounter StandardError: ', e
	#raise StandardError('Problem encountered!')
#resultFile.close()
#endof open(resultDir, 'a') as resultFile:

#3. Consolidate all the outputs

























