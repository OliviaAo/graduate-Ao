
'''
Function: Performance Anlysis for Colander Approach
Auhor: Ao Li
Date: 13-05-2018
'''

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def count( lines, hospital, location, patient, doctor):

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

	hospital.sort()
	location.sort()
	patient.sort()
	doctor.sort()

	return hospital, location, patient, doctor

def searchPHI(list, list_gs, count_fn):


	for item in list:
		if item in list_gs:
			list_gs.remove(item)
			count_fn += 1

	return count_fn, list_gs
try:

	# Read Scrubbed File
	num = '50'
	fr_ori = open('generatedFile/scrubbedText/'+num+'/scrubbed_original_annotation_test'+num+'.xml','r')
	fr_imp = open('generatedFile/scrubbedText/'+num+'/scrubbed_improved_annotation_test'+num+'.xml','r')
	fr_gs = open('generatedFile/originalText/original_test'+num+'.xml','r')

	# Initial Counter:
	countPeople = countPeople_ori_tp = countPeople_ori_fn = countPeople_imp_tp = countPeople_imp_fn = 0
	countPosition = countPosition_ori_tp = countPosition_ori_fn = countPosition_imp_tp = countPosition_imp_fn = 0
	
	# Print and Count TP and FP
	lines_ori = fr_ori.readlines()
	lines_imp = fr_imp.readlines()
	lines_gs = fr_gs.readlines()

	hospitals_ori = []
	hospitals_imp = []
	hospitals_ori_gs = []
	hospitals_imp_gs = []
	locations_ori = []
	locations_imp = []
	locations_ori_gs = []
	locations_imp_gs = []
	patients_ori = []
	patients_imp = []
	patients_ori_gs = []
	patients_imp_gs = []
	doctors_ori = []
	doctors_imp = []
	doctors_ori_gs = []
	doctors_imp_gs = []

	hospitals_ori_gs,locations_ori_gs,patients_ori_gs,doctors_ori_gs = count(lines_gs,hospitals_ori_gs,locations_ori_gs,patients_ori_gs,doctors_ori_gs)
	hospitals_imp_gs,locations_imp_gs,patients_imp_gs,doctors_imp_gs = count(lines_gs,hospitals_imp_gs,locations_imp_gs,patients_imp_gs,doctors_imp_gs)
	hospitals_ori,locations_ori,patients_ori,doctors_ori = count(lines_ori, hospitals_ori,locations_ori,patients_ori,doctors_ori)
	hospitals_imp,locations_imp,patients_imp,doctors_imp = count(lines_imp, hospitals_imp,locations_imp,patients_imp,doctors_imp)

	countPosition = len(hospitals_ori_gs) + len(locations_ori_gs)
	countPeople = len(patients_ori_gs) + len(doctors_ori_gs)

	# Hospital:
	countPosition_ori_fn, hospitals_ori_gs = searchPHI( hospitals_ori, hospitals_ori_gs, countPosition_ori_fn )
	countPosition_imp_fn, hospitals_imp_gs = searchPHI( hospitals_imp, hospitals_imp_gs, countPosition_imp_fn )

	# Location:
	countPosition_ori_fn, locations_ori_gs = searchPHI( locations_ori, locations_ori_gs, countPosition_ori_fn )
	countPosition_imp_fn, locations_imp_gs = searchPHI( locations_imp, locations_imp_gs, countPosition_imp_fn )

	# Patient:
	countPeople_ori_fn, patients_ori_gs = searchPHI( patients_ori, patients_ori_gs, countPeople_ori_fn )
	countPeople_imp_fn, patients_imp_gs = searchPHI( patients_imp, patients_imp_gs, countPeople_imp_fn )

	# Doctor:

	countPeople_ori_fn, doctors_ori_gs = searchPHI( doctors_ori, doctors_ori_gs, countPeople_ori_fn )
	countPeople_imp_fn, doctors_imp_gs = searchPHI( doctors_imp, doctors_imp_gs, countPeople_imp_fn )

	# Calculate False Negative:
	countPosition_ori_tp += len(hospitals_ori_gs) + len(locations_ori_gs)
	countPosition_imp_tp += len(hospitals_imp_gs) + len(locations_imp_gs)
	countPeople_ori_tp += len(patients_ori_gs) + len(doctors_ori_gs)
	countPeople_imp_tp += len(patients_imp_gs) + len(doctors_imp_gs)


	# Print All Counter:
	print ("Original Total Scrubbed:  %4d, TP: %4d, FN: %4d" %(countPeople+countPosition, countPeople_ori_tp+countPosition_ori_tp, countPeople_ori_fn+countPosition_ori_fn))
	print ("Original Total_People:    %4d, TP: %4d, FN: %4d" %(countPeople, countPeople_ori_tp, countPeople_ori_fn))
	print ("Original Total_Position:  %4d, TP: %4d, FN: %4d" %(countPosition, countPosition_ori_tp, countPosition_ori_fn))
	print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
	print ("Improved Total Scrubbed:  %4d, TP: %4d, FN: %4d" %(countPeople+countPosition, countPeople_imp_tp+countPosition_imp_tp, countPeople_imp_fn+countPosition_imp_fn))
	print ("Improved Total_People:    %4d, TP: %4d, FN: %4d" %(countPeople, countPeople_imp_tp, countPeople_imp_fn))
	print ("Improved Total_Position:  %4d, TP: %4d, FN: %4d" %(countPosition, countPosition_imp_tp, countPosition_imp_fn))


finally:
	fr_ori.close()
	fr_imp.close()
	fr_gs.close()



