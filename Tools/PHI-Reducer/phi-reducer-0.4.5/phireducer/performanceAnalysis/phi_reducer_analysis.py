
'''
Function: Performance Anlysis for PHI-Reducer
Auhor: Ao Li
Date: 25-03-2018
'''
try:

	# Read Scrubbed File
	f = open('/Users/ao/Desktop/graduate-Ao/Tools/PHI-Reducer/phi-reducer-0.4.5/phireducer/output_test/original_test50_phi_reduced.txt','r')


	# Initial Statistic File
	f_People_Position   = open('./results/Results_People.txt','w')
	

	# Initial Counter:
	countPeople_Position = countPeople_Position_tp = countPeople_Position_fp = 0
	
	# Print and Count TP and FP
	for line in f.readlines():

		# People + Position:
		if (line.find("**PHIName") != -1 ) or (line.find("**PHIPosition") != -1 ) or (line.find("**PHIAddress") != -1 ) or (line.find("**PHIDictionary") != -1 ):
			f_People_Position.write(line)
			countPeople_Position += line.count("**PHIName") + line.count("**PHIPosition") + line.count("**PHIAddress") + line.count("**PHIDictionary")

			# Count True Positive and False Positive:
			if(line.find("TYPE= '' DOCTOAR" ) != -1 ) or (line.find("TYPE= '' PATIENT") != -1 ) or (line.find("TYPE= '' LOCATION")!= -1 ) or (line.find("TYPE= '' HOSPITAL") != -1 ):
				count1 = line.count("TYPE= '' DOCTOAR") + line.count("TYPE= '' PATIENT") + line.count("TYPE= '' LOCATION") + line.count("TYPE= '' HOSPITAL")
				count2 = line.count("**PHIName") + line.count("**PHIPosition") + line.count("**PHIAddress") + line.count("**PHIDictionary")
				countPeople_Position_tp += line.count("TYPE= '' DOCTOAR") + line.count("TYPE= '' PATIENT") + line.count("TYPE= '' LOCATION") + line.count("TYPE= '' HOSPITAL")
				if count2>count1:
					countPeople_Position_fp += count2 - count1
			else:
				countPeople_Position_fp += line.count("**PHIName") + line.count("**PHIPosition") + line.count("**PHIAddress") + line.count("**PHIDictionary")


	# Print All Counter:
	print ("Total_People:    %4d, TP: %4d, FP: %4d" %(countPeople_Position, countPeople_Position_tp, countPeople_Position_fp))
	f_People_Position.write("Total_People: %d, TP: %d, FP: %d" %(countPeople_Position, countPeople_Position_tp, countPeople_Position_fp))


finally:
	f.close()
	f_People_Position.close()

