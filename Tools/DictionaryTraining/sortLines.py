
'''
Function: Sort lines in a file
Auhor: Ao Li
Date: 30-04-2018
'''
try:
	f = open('positionDictionary/positionDictionary.txt','r')
	lines = f.readlines()
	lines.sort()
	f.writelines(lines)
finally:
	f.close()