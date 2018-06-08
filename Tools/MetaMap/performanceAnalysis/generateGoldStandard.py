'''
Function: Generate gold standard for evaluation
Auhor: Ao Li
Date: 24-05-2018
'''

def removeDuplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

try:
	num = '90'
	fr = open('generatedFile/originalText/original_test'+num+'.xml','r')
	fw_hospital = open('generatedFile/goldStandard/'+num+'/hospital.txt','w')
	fw_location = open('generatedFile/goldStandard/'+num+'/location.txt','w')
	fw_patient = open('generatedFile/goldStandard/'+num+'/patient.txt','w')
	fw_doctor = open('generatedFile/goldStandard/'+num+'/doctor.txt','w')

	hospital = []
	location = []
	patient = []
	doctor = []

	# 1. Collect Gold Standard:
	lines = fr.readlines()
	for line in lines:
		if (line.find("<PHI TYPE=\"HOSPITAL\">") != -1):
			startIndex = list(find_all(line, "<PHI TYPE=\"HOSPITAL\">"))
			for i in startIndex:
				endIndex = line.index("</PHI>", i)
				hospital.append(line[i+21:endIndex]+'\n')

		if (line.find("<PHI TYPE=\"LOCATION\">") != -1):
			startIndex = list(find_all(line, "<PHI TYPE=\"LOCATION\">"))
			for i in startIndex:
				endIndex = line.index("</PHI>", i)
				location.append(line[i+21:endIndex]+'\n')

		if (line.find("<PHI TYPE=\"PATIENT\">") != -1):
			startIndex = list(find_all(line, "<PHI TYPE=\"PATIENT\">"))
			for i in startIndex:
				endIndex = line.index("</PHI>", i)
				patient.append(line[i+20:endIndex]+'\n')

		if (line.find("<PHI TYPE=\"DOCTOR\">") != -1):
			startIndex = list(find_all(line, "<PHI TYPE=\"DOCTOR\">"))
			for i in startIndex:
				endIndex = line.index("</PHI>", i)
				doctor.append(line[i+19:endIndex]+'\n')


	
	# 2. Sort Gold Standard List:
	hospital.sort()
	location.sort()
	patient.sort()
	doctor.sort()

	# 3. De-duplicate Gold Standard List:
	hospital = removeDuplicates(hospital)
	location = removeDuplicates(location)
	patient = removeDuplicates(patient)
	doctor = removeDuplicates(doctor)

	# 4. Output to the file:
	fw_hospital.writelines(hospital)	
	fw_location.writelines(location)
	fw_patient.writelines(patient)
	fw_doctor.writelines(doctor)


finally:
	fr.close()
	fw_hospital.close()
	fw_location.close()
	fw_patient.close()
	fw_doctor.close()
