
'''
Function: Generate potential PHI list
Auhor: Ao Li
Date: 24-05-2018
'''

def removeDuplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

try:
	num = '50'
	fr = open('generatedFile/metamapText/metamap_original_test'+num+'.xml', 'r')
	fw_hospital_phrase = open('generatedFile/potentialPHIList/'+num+'/hospital_phrase.txt','w')
	fw_location_phrase = open('generatedFile/potentialPHIList/'+num+'/location_phrase.txt','w')
	fw_hospital_word = open('generatedFile/potentialPHIList/'+num+'/hospital_word.txt','w')
	fw_location_word = open('generatedFile/potentialPHIList/'+num+'/location_word.txt','w')


	lines = fr.readlines()
	startIndex = 9
	locations_phrase = []
	hospitals_phrase = []
	hospitals_word = []
	locations_word = []


	# 1. Generate Protential PHI Lists:
	for line in lines:
	
		# Hospital:
		if (line.find("Health Care Related Organization") != -1 ):
			if line.find('(') != -1:
				endIndex = line.index('(')
			else:
				endIndex = line.index('[')
			hospitals_phrase.append(line[startIndex:endIndex]+'\n')

		# Location:
		if ( line.find("Geographic Area") !=-1 ):
			if line.find('(') != -1:
				endIndex = line.index('(')
			else:
				endIndex = line.index('[')
			locations_phrase.append(line[startIndex:endIndex]+'\n')
		

	# 2. Sort  and De-duplicate Protential PHI Phrase List:
	hospitals_phrase.sort()
	locations_phrase.sort()
	hospitals_phrase = removeDuplicates(hospitals_phrase)
	locations_phrase = removeDuplicates(locations_phrase)

	# 3. Output to Phrase File:
	fw_hospital_phrase.writelines(hospitals_phrase)	
	fw_location_phrase.writelines(locations_phrase)

	# 4 Seperate Phrase into Words:
	for hospital in hospitals_phrase:
		temp = hospital.split()
		temp = [x + '\n' for x in temp]
		hospitals_word.extend(temp)
	for location in locations_phrase:
		temp = location.split()
		temp = [x + '\n' for x in temp]
		locations_word.extend(temp)

	# 5. Remove Comma:
	hospitals_word = remove_values_from_list(hospitals_word,',')
	locations_word = remove_values_from_list(locations_word,',')

	# 6. Sort and De-duplicate
	hospitals_word.sort()
	locations_word.sort()
	hospitals_word = removeDuplicates(hospitals_word)
	locations_word = removeDuplicates(locations_word)

	# 7. Output to The Word File:
	fw_hospital_word.writelines(hospitals_word)	
	fw_location_word.writelines(locations_word)

finally:
	fr.close()
	fw_hospital_phrase.close()
	fw_location_phrase.close()
	fw_hospital_word.close()
	fw_location_word.close()

