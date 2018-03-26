
'''
Function: Performance Anlysis
Auhor: Ao Li
Date: 21-03-2018
'''
try:

	# Read Scrubbed File
	# f = open('./scrubbedTest/50/scrubbed_original_test50.xml','r')
	f = open('/Users/ao/Desktop/graduate-Ao/Tools/DEID/deid-1.1/scrubbed_original_test50.res','r')

	# Initial Statistic File
	f_Age      = open('./results/Results_Age.txt','w')
	f_People   = open('./results/Results_People.txt','w')
	f_Position = open('./results/Results_Position.txt','w')
	f_Telephone    = open('./results/Results_Phone.txt','w')
	

	# Initial Counter:
	countAge = countAge_tp = countAge_fp = 0
	countPeople = countPeople_tp = countPeople_fp = 0
	countPosition = countPosition_tp = countPosition_fp = 0
	countTelephone = countTelephone_tp = countTelephone_fp = 0
	
	# Print and Count TP and FP
	for line in f.readlines():

		# Age:
		if (line.find("**Age") != -1 ):
			f_Age.write(line)
			countAge += line.count("**Age") 
	
			# Count True Positive and False Positive:
			if(line.find("AGE\">[**Age")!= -1 ):
				countAge_tp += line.count("**Age")
			else:
				countAge_fp += line.count("**Age")


		# People:
		if (line.find("**First Name") != -1 ) or (line.find("**Initials") != -1 ) or (line.find("**Last Name") != -1 ):
			f_People.write(line)
			countPeople += line.count("**First Name") + line.count("**Initials") + line.count("**Last Name")

			# Count True Positive and False Positive:
			if(line.find("TYPE=\"DOCTOAR\"" ) != -1 ) or (line.find("TYPE=\"PATIENT\"") != -1 ):
				countPeople_tp += line.count("**First Name") + line.count("**Initials") + line.count("**Last Name")
			else:
				countPeople_fp += line.count("**First Name") + line.count("**Initials") + line.count("**Last Name")


		# Position (Location + Hosipital):
		if (line.find("**Hospital") != -1 ) or (line.find("**Street Add") != -1 ) or (line.find("**Location") != -1 ):
			f_Position.write(line)
			countPosition += line.count("**Position") + line.count("**Hospital") + line.count("**Street Add") + line.count("**Location")

			# Count True Positive and False Positive:
			if(line.find("TYPE=\"LOCATION\"")!= -1 ) or (line.find("TYPE=\"HOSPITAL\"") != -1 ):
				countPosition_tp += line.count("**Position") + line.count("**Hospital") + line.count("**Street Add") + line.count("**Location")
			else:
				countPosition_fp += line.count("**Position") + line.count("**Hospital") + line.count("**Street Add") + line.count("**Location")

		# Telephone
		if (line.find("**Telephone") != -1 ):
			f_Telephone.write(line)
			countTelephone += line.count("**Telephone")
	
			# Count True Positive and False Positive:
			if(line.find("TYPE=\"PHONE\"")!= -1 ):
				countTelephone_tp += line.count("**Telephone")
			else:
				countTelephone_fp += line.count("**Telephone")


	# Print All Counter:
	print ("Total_Age:       %4d, TP: %4d, FP: %4d" %(countAge, countAge_tp, countAge_fp))
	f_Age.write("Total_ID: %d, TP: %d, FP: %d" %(countAge, countAge_tp, countAge_fp))
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

