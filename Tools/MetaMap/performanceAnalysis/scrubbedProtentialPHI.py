'''
Function: Scrubbed text with help of metamap semantic groups
Auhor: Ao Li
Date: 25-05-2018
'''

import re

def stringTailor( str ):
	
	if str.find(" ") != -1:
		index = str.index(" ")
		str = str[index+1:]
	else:
		str = ""
	return str

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in xrange(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

def match(phiList, line):

	for item in phiList:
		item = item.rstrip()
		temp = line
		while temp:
			if re.match(item,temp,re.IGNORECASE):
				index = line.index(temp)
				for i in range(len(item)):
					line = replacer(line,'*',index+i)
			temp = stringTailor(temp)

	return line

try:

	# Read Scrubbed File
	num ='50'
	fr = open('generatedFile/scrubbedText/'+num+'/scrubbed_original_test'+num+'.xml','r')
	fw = open('generatedFile/scrubbedText/'+num+'/scrubbed_improved_test'+num+'.xml','w')
	fr_hospital_phrase_gs = open('generatedFile/potentialPHIList/'+num+'/hospital_phrase.txt','r')
	fr_location_phrase_gs = open('generatedFile/potentialPHIList/'+num+'/location_phrase.txt','r')
	fr_hospital_word_gs = open('generatedFile/potentialPHIList/'+num+'/hospital_word.txt','r')
	fr_location_word_gs = open('generatedFile/potentialPHIList/'+num+'/location_word.txt','r')

	lines = fr.readlines()
	hospitals_phrase = fr_hospital_phrase_gs.readlines()
	locations_phrase = fr_location_phrase_gs.readlines()
	hospitals_word = fr_hospital_word_gs.readlines()
	locations_word = fr_location_word_gs.readlines()

	for line in lines:

		# Hospital:
		# For Phrase Match
		line = match( hospitals_phrase, line)
		# For Word Match
		line = match ( hospitals_word, line)


		# Location:
		# For Phrase Match
		line = match( locations_phrase, line)
		# For Word Match
		line = match ( locations_word, line)
		
		fw.write(line)
		print "~~~~"


finally:
	fr.close()
	fw.close()
	fr_hospital_phrase_gs.close()
	fr_location_phrase_gs.close()
	fr_hospital_word_gs.close()
	fr_location_word_gs.close()












