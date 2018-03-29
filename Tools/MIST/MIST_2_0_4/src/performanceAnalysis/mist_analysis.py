
'''
Function: Performance Anlysis for MIST
Auhor: Ao Li
Date: 28-03-2018
'''
try:

	# Read Scrubbed File
	# f = open('scrubbedTest/90/scrubbed_original_testcase90.xml','r')
	f = open('/Users/ao/Desktop/graduate-Ao/Tools/MIST/MIST_2_0_4/src/scrubbed_original_testcase50.xml','r')

	# Initial Statistic File
	f_Age       = open('./results/Results_Age.txt','w')
	f_People    = open('./results/Results_People.txt','w')
	f_Position  = open('./results/Results_Position.txt','w')
	f_Telephone = open('./results/Results_Phone.txt','w')
	

	# Initial Counter:
	countAge = countAge_tp = countAge_fp = 0
	countPeople = countPeople_tp = countPeople_fp = 0
	countPosition = countPosition_tp = countPosition_fp = 0
	countTelephone = countTelephone_tp = countTelephone_fp = 0
	
	# Print and Count TP and FP
	for line in f.readlines():

		# Age:
		if (line.find("[AGE]") != -1 ):
			f_Age.write(line)
			countAge += line.count("[AGE]")
	
			# Count True Positive and False Positive:
			if(line.find("TYPE=\"AGE\">")!= -1 ):
				count1 = line.count("[AGE]")
				count2 = line.count("TYPE=\"AGE\">")
				if count2 < count1: 
					countAge_tp += count2
					countAge_fp += count1 - count2
				else:
					countAge_tp += count1
			else:
				countAge_fp += line.count("[AGE]")
	

		# Doctor + Patient:
		if (line.find("[DOCTOR]") != -1 ) or (line.find("[PATIENT]") != -1 ):
			f_People.write(line)
			countPeople += line.count("[DOCTOR]") + line.count("[PATIENT]")

			# Count True Positive and False Positive:
			if (line.find("TYPE=\"DOCTOR\">") != -1 ) or (line.find("TYPE=\"PATIENT\">") != -1 ):
				count1 = line.count("[DOCTOR]") + line.count("[PATIENT]")
				count2 = line.count("TYPE=\"DOCTOR\">") + line.count("TYPE=\"PATIENT\">")
				if count2 < count1: 
					countPeople_tp += count2
					countPeople_fp += count1 - count2
				else:
					countPeople_tp += count1
			else:
				countPeople_fp += line.count("[DOCTOR]") + line.count("[PATIENT]")


		# Location + Hospital:
		if (line.find("[LOCATION]") != -1 ) or (line.find("[HOSPITAL]") != -1 ):
			f_Position.write(line)
			countPosition += line.count("[LOCATION]") + line.count("[HOSPITAL]")

			# Count True Positive and False Positive:
			if (line.find("TYPE=\"LOCATION\">") != -1 ) or (line.find("TYPE=\"HOSPITAL\">") != -1 ):
				count1 = line.count("[LOCATION]") + line.count("[HOSPITAL]")
				count2 = line.count("TYPE=\"LOCATION\">") + line.count("TYPE=\"HOSPITAL\">")
				if count2 < count1: 
					countPosition_tp += count2
					countPosition_fp += count1 - count2
				else:
					countPosition_tp += count1
			else:
				countPosition_fp += line.count("[HOSPITAL]") + line.count("[LOCATION]")

		# Telephone
		if (line.find("[PHONE]") != -1 ):
			f_Telephone.write(line)
			countTelephone += line.count("[PHONE]")
	
			# Count True Positive and False Positive:
			if(line.find("TYPE=\"PHONE\">")!= -1 ):
				count1 = line.count("[PHONE]")
				count2 = line.count("TYPE=\"PHONE\">")
				if count2 < count1: 
					countTelephone_tp += count2
					countTelephone_fp += count1 - count2
				else:
					countTelephone_tp += count1
			else:
				countTelephone_fp += line.count("[PHONE]")


	# Print All Counter:
	print ("Total_Age:       %4d, TP: %4d, FP: %4d" %(countAge, countAge_tp, countAge_fp))
	f_Age.write("Total_Age: %d, TP: %d, FP: %d" %(countAge, countAge_tp, countAge_fp))
	print ("Total_People:    %4d, TP: %4d, FP: %4d" %(countPeople, countPeople_tp, countPeople_fp))
	f_People.write("Total_People: %d, TP: %d, FP: %d" %(countPeople, countPeople_tp, countPeople_fp))
	print ("Total_Position:  %4d, TP: %4d, FP: %4d" %(countPosition, countPosition_tp, countPosition_fp))
	f_Position.write("Total_Position: %d, TP: %d, FP: %d" %(countPosition, countPosition_tp, countPosition_fp))
	print ("Total_Telephone: %4d, TP: %4d, FP: %4d" %(countTelephone, countTelephone_tp, countTelephone_fp))
	f_Telephone.write("Total_Telephone: %d, TP: %d, FP: %d" %(countTelephone, countTelephone_tp, countTelephone_fp))



finally:
	f.close()
	f_Age.close()
	f_People.close()
	f_Position.close()
	f_Telephone.close()

