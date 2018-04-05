
'''
Function: Training Dictionary
Auhor: Ao Li
Date: 21-03-2018
'''

try:

	f = open('./test50/original_testcase50.xml','r')
	f_d = open('./test50/positionDictionary50.txt','w')

	dic = []
	for line in f.readlines():
		if (line.find("<PHI TYPE=\"LOCATION\">") != -1 ): 
			indexStart = line.index("<PHI TYPE=\"LOCATION\">") + 21
			indexEnd = line.index("</PHI>", indexStart)
			dic.append(line[indexStart:indexEnd]+'\n')


		if (line.find("<PHI TYPE=\"HOSPITAL\">") != -1 ):
			indexStart = line.index("<PHI TYPE=\"HOSPITAL\">") + 21
			indexEnd = line.index("</PHI>", indexStart)
			dic.append( line[indexStart:indexEnd]+'\n' )


	# Remove redundant from the list:
	dic = list(set(dic))
	dic.sort()

	for item in dic:
		f_d.write(item)

finally:

	f.close()
	f_d.close()