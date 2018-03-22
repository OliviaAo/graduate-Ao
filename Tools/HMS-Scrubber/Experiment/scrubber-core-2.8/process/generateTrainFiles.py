
'''
Function: Generate Dictionary Training Files
Auhor: Ao Li
Date: 21-03-2018
'''

import random

def writeFile( f, writeList ):
	for line in writeList:
		f.write(line)

try:

	# Open File:
	f = open('original_testcase.xml','r')
	f_head = open('processHead.xml','r')
	f_tail = open('processTail.xml','r')
	f_train = open('./test50/original_testcase50.xml','w')
	f_test  = open('./test50/original_test50.xml','w')
	lines = f.readlines()
	linesHead = f_head.readlines()
	linesTail = f_tail.readlines()

	# Number of lines in the file:
	lineNum = len(lines)

	# Number of lines for training:
	percentage = 0.5
	lineTrainNum = int(lineNum * percentage)

	# Create random number list:
	randomList = random.sample(xrange(lineNum),lineTrainNum)

	lineTrainList = []
	lineTestList = []
	i = 0
	for line in lines:
		if i in randomList:
			lineTrainList.append(line)
		else:
			lineTestList.append(line)
		i += 1

	print lineNum, len(lineTrainList), len(lineTestList)

	writeFile(f_train, linesHead)
	writeFile(f_test,linesHead)
	writeFile(f_train, lineTrainList)
	writeFile(f_test, lineTestList)
	writeFile(f_train, linesTail)
	writeFile(f_test,linesTail)


finally:
 	f.close()
 	f_train.close()
 	f_test.close()