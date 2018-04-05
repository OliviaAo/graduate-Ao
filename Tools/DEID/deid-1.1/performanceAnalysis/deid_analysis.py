
'''
Function: Performance Anlysis for De-ID Scrubber
Auhor: Ao Li
Date: 21-03-2018
'''
try:

	# Read Scrubbed File
	# f = open('./peopleScrubbedTest/50/scrubbed_original_test50.res','r')
	f = open('./peopleScrubbedTest/50/scrubbed_original_dictionary_test50.res','r')
	# f = open('/Users/ao/Desktop/graduate-Ao/Tools/DEID/deid-1.1/original_test50.res','r')

	# Initial Statistic File
	f_People   = open('./results/Results_People.txt','w')
	f_Position = open('./results/Results_Position.txt','w')
	

	# Initial Counter:
	countPeople = countPeople_tp = countPeople_fp = 0
	countPosition = countPosition_tp = countPosition_fp = 0
	
	# Print and Count TP and FP
	for line in f.readlines():

		# People:
		if (line.find("**First Name") != -1 ) or (line.find("**Initials") != -1 ) or (line.find("**Last Name") != -1 ) or (line.find("**Company")):
			f_People.write(line)
			countPeople += line.count("**First Name") + line.count("**Initials") + line.count("**Last Name") + line.count("**Company")

			# Count True Positive and False Positive:
			if(line.find("TYPE=\"DOCTOAR\"") != -1 ) or (line.find("TYPE=\"PATIENT\"") != -1 ):
				count1 = line.count("**First Name") + line.count("**Initials") + line.count("**Last Name") + line.count("**Company")
				count2 = line.count("TYPE=\"DOCTOAR\"") + line.count("TYPE=\"PATIENT\"") 
				if count2 < count1:
					countPeople_tp += count2
					countPeople_fp += count1 - count2
				else:
					countPeople_tp += count1
			else:
				countPeople_fp += line.count("**First Name") + line.count("**Initials") + line.count("**Last Name") + + line.count("**Company")


		# Position (Location + Hosipital):
		if (line.find("**Hospital") != -1 ) or (line.find("**Street Add") != -1 ) or (line.find("**Location") != -1 ) or (line.find("**Position")!=-1):
			f_Position.write(line)
			countPosition += line.count("**Position") + line.count("**Hospital") + line.count("**Street Add") + line.count("**Location")

			# Count True Positive and False Positive:
			if(line.find("TYPE=\"LOCATION\"")!= -1 ) or (line.find("TYPE=\"HOSPITAL\"") != -1 ):
				count1 = line.count("**Position") + line.count("**Hospital") + line.count("**Street Add") + line.count("**Location")
				count2 = line.count("TYPE=\"LOCATION\"") + line.count("TYPE=\"HOSPITAL\"")
				if count2 < count1:
					countPosition_tp += count2
					countPosition_fp += count1 - count2
				else:	
					countPosition_tp += count1
			else:
				countPosition_fp += line.count("**Position") + line.count("**Hospital") + line.count("**Street Add") + line.count("**Location")


	# Print All Counter:
	print ("Total_People:    %4d, TP: %4d, FP: %4d" %(countPeople, countPeople_tp, countPeople_fp))
	f_People.write("Total_People: %d, TP: %d, FP: %d" %(countPeople, countPeople_tp, countPeople_fp))
	print ("Total_Position:  %4d, TP: %4d, FP: %4d" %(countPosition, countPosition_tp, countPosition_fp))
	f_Position.write("Total_Position: %d, TP: %d, FP: %d" %(countPosition, countPosition_tp, countPosition_fp))



finally:
	f.close()
	f_People.close()
	f_Position.close()

