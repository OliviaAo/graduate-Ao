'''
Function: Performance Anlysis for PHI-Reducer
Auhor: Ao Li
Date: 25-03-2018
'''
try:

	# Read Scrubbed File
	# f = open('./scrubbedTest/90/scrubbed_original_test90.txt','r')
	f = open('./scrubbedTest/90/scrubbed_original_dictionary_test90.txt','r')

	# Initial Statistic File
	f_People   = open('./results/Results_People.txt','w')
	f_Position = open('./results/Results_Position.txt','w')
	

	# Initial Counter:
	countPeople = countPeople_tp = countPeople_fp = 0
	countPosition = countPosition_tp = countPosition_fp = 0
	
	# Print and Count TP and FP
	for line in f.readlines():

		# People:
		if (line.find("**PHIName") != -1 ):
			f_People.write(line)
			countPeople += line.count("**PHIName")

			# Count True Positive and False Positive:
			if(line.find("TYPE= '' DOCTOAR") != -1 ) or (line.find("TYPE= '' PATIENT") != -1 ):
				count1 = line.count("**PHIName") 
				count2 = line.count("TYPE= '' DOCTOAR") + line.count("TYPE= '' PATIENT") 
				if count2 < count1:
					countPeople_tp += count2
					countPeople_fp += count1 - count2
				else:
					countPeople_tp += count1
			else:
				countPeople_fp += line.count("**PHIName")


		# Position (Location + Hosipital):
		if (line.find("**PHIPosition") != -1 ) or (line.find("**PHIAddress") != -1 ) or (line.find("**PHIDictionary") != -1 ):
			f_Position.write(line)
			countPosition += line.count("**PHIPosition") + line.count("**PHIAddress") + line.count("**PHIDictionary")

			# Count True Positive and False Positive:
			if(line.find("TYPE= '' LOCATION")!= -1 ) or (line.find("TYPE= '' HOSPITAL") != -1 ):
				count1 = line.count("**PHIPosition") + line.count("**PHIAddress") + line.count("**PHIDictionary")
				count2 = line.count("TYPE= '' LOCATION") + line.count("TYPE= '' HOSPITAL")
				if count2 < count1:
					countPosition_tp += count2
					countPosition_fp += count1 - count2
				else:	
					countPosition_tp += count1
			else:
				countPosition_fp += line.count("**PHIPosition") + line.count("**PHIAddress") + line.count("**PHIDictionary")


	# Print All Counter:
	print ("Total_People:    %4d, TP: %4d, FP: %4d" %(countPeople, countPeople_tp, countPeople_fp))
	f_People.write("Total_People: %d, TP: %d, FP: %d" %(countPeople, countPeople_tp, countPeople_fp))
	print ("Total_Position:  %4d, TP: %4d, FP: %4d" %(countPosition, countPosition_tp, countPosition_fp))
	f_Position.write("Total_Position: %d, TP: %d, FP: %d" %(countPosition, countPosition_tp, countPosition_fp))



finally:
	f.close()
	f_People.close()
	f_Position.close()

