
'''
Function: Performance Anlysis
Auhor: Ao Li
Date: 21-03-2018
'''
try:

	# Read Scrubbed File
	# f = open('./scrubbedTest/50/scrubbed_original_test50.xml','r')
	f = open('./scrubbedTest/50/scrubbed_original_dictionary_test50.xml','r')

	# Initial Statistic File
	f_ID       = open('./results/Results_ID.txt','w')
	f_Age      = open('./results/Results_Age.txt','w')
	f_Date     = open('./results/Results_Date.txt','w')
	f_Doctor   = open('./results/Results_Doctor.txt','w')
	f_Position = open('./results/Results_Position.txt','w')
	f_Telephone    = open('./results/Results_Phone.txt','w')
	

	# Initial Counter:
	countID = countID_tp = countID_fp = 0
	countAge = countAge_tp = countAge_fp = 0
	countDate = countDate_tp = countDate_fp = 0
	countDoctor = countDoctor_tp = countDoctor_fp = 0
	countPosition = countPosition_tp = countPosition_fp = 0
	countTelephone = countTelephone_tp = countTelephone_fp = 0
	
	# Print and Count TP and FP
	for line in f.readlines():

		# ID:
		if (line.find("xxxxSSN") != -1 ) or (line.find("xxxxSUSPICIOUS_NUM") != -1 ):
			f_ID.write(line)
			countID += line.count("xxxxSSN") + line.count("xxxxSUSPICIOUS_NUM")

			# Count True Positive and False Positive:
			if(line.find("ID xxxxSSN") != -1 ) or (line.find("ID xxxxSUSPICIOUS_NUM") != -1 ):
				countID_tp += line.count("ID xxxxSSN") + line.count("ID xxxxSUSPICIOUS_NUM")
			else:
				countID_fp += line.count("xxxxSSN") + line.count("xxxxSUSPICIOUS_NUM")

		# Age:
		if (line.find("xxxxAGE") != -1 ) or (line.find("xxxxWRITTEN_AGE") != -1 ):
			f_Age.write(line)
			countAge += line.count("xxxxAGE") + line.count("xxxxWRITTEN_AGE")
	
			# Count True Positive and False Positive:
			if(line.find("AGE xxxxAGE")!= -1 ) or (line.find("AGE xxxxWRITTEN_AGE")!= -1 ):
				countAge_tp += line.count("xxxxAGE") + line.count("xxxxWRITTEN_AGE")
			else:
				countAge_fp += line.count("xxxxAGE") + line.count("xxxxWRITTEN_AGE")

		# Date:
		if (line.find("xxxxDATE") != -1 ):
			f_Date.write(line)
			countDate += line.count("xxxxDATE")
	
			# Count True Positive and False Positive:
			if(line.find("DATE xxxxDATE")!= -1 ):
				countDate_tp += line.count("xxxxDATE")
			else:
				countDate_fp += line.count("xxxxDATE")

		# Doctor:
		if (line.find("xxxxDOCTOR_OLDER") != -1 ) or (line.find("xxxxDOCTOR") != -1 ):
			f_Doctor.write(line)
			countDoctor += line.count("xxxxDOCTOR")

			# Count True Positive and False Positive:
			if(line.find("TYPE xxxxDOCTOR_OLDER" ) != -1 ):
				countDoctor_tp +=  line.count("xxxxDOCTOR_OLDER") 
			else:
				countDoctor_fp +=  line.count("xxxxDOCTOR")


		# Location + Hospital:
		if (line.find("xxxPOSITION") != -1 ) or (line.find("xxxHOSPITAL") != -1 ):
			f_Position.write(line)
			countPosition += line.count("xxxPOSITION") + line.count("xxxHOSPITAL")

			# Count True Positive and False Positive:
			if(line.find("TYPE=\"LOCATION\"")!= -1 ) or (line.find("TYPE=\"HOSPITAL\"") != -1 ):
				countPosition_tp += line.count("xxxPOSITION") + line.count("xxxHOSPITAL") 
			else:
				countPosition_fp += line.count("xxxPOSITION") + line.count("xxxHOSPITAL")

		# Telephone
		if (line.find("xxxxTELEPHONE") != -1 ):
			f_Telephone.write(line)
			countTelephone += line.count("xxxxTELEPHONE")
	
			# Count True Positive and False Positive:
			if(line.find("PHONE xxxxTELEPHONE")!= -1 ):
				countTelephone_tp += line.count("xxxxTELEPHONE")
			else:
				countTelephone_fp += line.count("xxxxTELEPHONE")


	# Print All Counter:
	print ("Total_ID:        %4d, TP: %4d, FP: %4d" %(countID, countID_tp, countID_fp))
	f_ID.write("Total_ID: %d, TP: %d, FP: %d" %(countID, countID_tp, countID_fp))
	print ("Total_Age:       %4d, TP: %4d, FP: %4d" %(countAge, countAge_tp, countAge_fp))
	f_Age.write("Total_ID: %d, TP: %d, FP: %d" %(countAge, countAge_tp, countAge_fp))
	print ("Total_Date:      %4d, TP: %4d, FP: %4d" %(countDate, countDate_tp, countDate_fp))
	f_Date.write("Total_Date: %d, TP: %d, FP: %d" %(countDate, countDate_tp, countDate_fp))
	print ("Total_Doctor:    %4d, TP: %4d, FP: %4d" %(countDoctor, countDoctor_tp, countDoctor_fp))
	f_Doctor.write("Total_Doctor: %d, TP: %d, FP: %d" %(countDoctor, countDoctor_tp, countDoctor_fp))
	print ("Total_Position:  %4d, TP: %4d, FP: %4d" %(countPosition, countPosition_tp, countPosition_fp))
	f_Position.write("Total_Position: %d, TP: %d, FP: %d" %(countPosition, countPosition_tp, countPosition_fp))
	print ("Total_Telephone: %4d, TP: %4d, FP: %4d" %(countTelephone, countTelephone_tp, countTelephone_fp))
	f_Telephone.write("Total_Telephone: %d, TP: %d, FP: %d" %(countTelephone, countTelephone_tp, countTelephone_fp))



finally:
	f.close()
	f_ID.close()
	f_Age.close()
	f_Date.close()
	f_Doctor.close()
	f_Position.close()
	f_Telephone.close()

