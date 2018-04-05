
'''
Function: Training Dictionary
Auhor: Ao Li
Date: 21-03-2018
'''

try:

	f = open('./testDataset/test50/original_train50.xml','r')
	f_d = open('./testDataset/test50/peopleDictionary50.txt','w')

	dic = []
	for line in f.readlines():
		if (line.find("<PHI TYPE=\"DOCTOR\">") != -1 ): 
			indexStart = line.index("<PHI TYPE=\"DOCTOR\">") + 19
			indexEnd = line.index("</PHI>", indexStart)
			dic.append(line[indexStart:indexEnd]+'\n')


		if (line.find("<PHI TYPE=\"PATIENT\">") != -1 ):
			indexStart = line.index("<PHI TYPE=\"PATIENT\">") + 20
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