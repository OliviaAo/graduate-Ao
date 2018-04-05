
'''
Function: Performance Anlysis for HMS Scrubber
Auhor: Ao Li
Date: 21-03-2018
'''
try:

	# Read Scrubbed File
	# f = open('./peopleScrubbedTest/50/scrubbed_original_test50.xml','r')
	f = open('./peopleScrubbedTest/50/scrubbed_original_dictionary_test50.xml','r')

	# Initial Statistic File b
	f_People   = open('./results/Results_Doctor.txt','w')
	f_Position = open('./results/Results_Position.txt','w')
	

	# Initial Counter:
	countPeople = countPeople_tp = countPeople_fp = 0
	countPosition = countPosition_tp = countPosition_fp = 0
	
	# Print and Count TP and FP
	for line in f.readlines():

		# People = Doctor + Patient:
		if (line.find("xxxxDOCTOR") != -1 ) or (line.find("xxxPEOPLE") != -1 ):
			f_People.write(line)
			countPeople += line.count("xxxxDOCTOR") + line.count("xxxPEOPLE")

			# Count True Positive and False Positive:
			if(line.find("TYPE=\"DOCTOR\"")!= -1 ) or (line.find("TYPE=\"PATIENT\"") != -1 ):
				count1 = line.count("xxxxDOCTOR") + line.count("xxxPEOPLE")
				count2 = line.count("TYPE=\"DOCTOR\"") + line.count("TYPE=\"PATIENT\"")
				if count2 < count1:
					countPeople_tp +=  count2
					countPeople_fp += count1 - count2
				else:
					countPeople_tp += count1
			else:
				countPeople_fp +=  line.count("xxxxDOCTOR") + line.count("xxxPEOPLE")


		# Position = Location + Hospital:
		if (line.find("xxxPOSITION") != -1 ) or (line.find("xxxHOSPITAL") != -1 ) or (line.find("xxxxPRIVATE") != -1 ):
			f_Position.write(line)
			countPosition += line.count("xxxPOSITION") + line.count("xxxHOSPITAL") + line.count("xxxxPRIVATE")

			# Count True Positive and False Positive:
			if(line.find("TYPE=\"LOCATION\"")!= -1 ) or (line.find("TYPE=\"HOSPITAL\"") != -1 ):
				count1 = line.count("xxxPOSITION") + line.count("xxxHOSPITAL") + line.count("xxxxPRIVATE")
				count2 = line.count("TYPE=\"LOCATION\"") + line.count("TYPE=\"HOSPITAL\"")
				if count2 < count1:
					countPosition_tp += count2
					countPosition_fp += count1 - count2 
				else:
					countPosition_tp += count1
			else:
				countPosition_fp += line.count("xxxPOSITION") + line.count("xxxHOSPITAL") + line.count("xxxxPRIVATE")


	# Print All Counter:
	print ("Total_People:    %4d, TP: %4d, FP: %4d" %(countPeople, countPeople_tp, countPeople_fp))
	f_People.write("Total_People: %d, TP: %d, FP: %d" %(countPeople, countPeople_tp, countPeople_fp))
	print ("Total_Position:  %4d, TP: %4d, FP: %4d" %(countPosition, countPosition_tp, countPosition_fp))
	f_Position.write("Total_Position: %d, TP: %d, FP: %d" %(countPosition, countPosition_tp, countPosition_fp))

finally:
	f.close()
	f_People.close()
	f_Position.close()

