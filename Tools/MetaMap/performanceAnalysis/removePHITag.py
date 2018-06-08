

'''
Function: Remove PHI tags in original text
Auhor: Ao Li
Date: 24-05-2018
'''

import re
try:
	num = 90
	fr = open('generatedFile/originalText/original_test'+num+'.xml','r')
	fw = open('generatedFile/reformattedText/reformatted_original_test'+num+'.xml','w')

	lines = fr.readlines()
	for line in lines:
		line = re.sub('<PHI TYPE=\"(\w)+\">','',line)
		line = re.sub('<\/PHI>','',line)
		fw.write(line)


finally:
	fr.close()
	fw.close()
