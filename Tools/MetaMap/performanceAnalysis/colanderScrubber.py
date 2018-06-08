'''
Function: Scrubber for Colander Approach
Auhor: Ao Li
Date: 24-05-2018
'''

try:
	num = '50'
	fr = open('generatedFile/metamapText/metamap_original_test'+num+'.xml', 'r')
	fw = open('generatedFile/scrubbedText/scrubbed_original_test'+num+'.xml','w')

	lines = fr.readlines()
	protected_words_dictionary = []
	temp = []
	flag = 0

	# Print and Count TP and FP
	for line in lines:
	
		# People + Position:
		if (line.find("Phrase: ") != -1 ):
			flag = 1
			line = line.replace("Phrase: ", "")
			line = line.replace("\n"," ")
			temp.append(line)
		elif ( line.find("Meta Mapping") !=-1 and flag == 1):
			flag = 0
			str = temp.pop(0)
			protected_words_dictionary.append(str)
		elif (line == '\n' and flag == 1):
			flag = 0
			temp = []
		elif (line.find("Processing 00000000") != -1 ):
			protected_words_dictionary.append('\n')
		


	for item in protected_words_dictionary:
		fw.write(item)

finally:
	fr.close()
	fw.close()
