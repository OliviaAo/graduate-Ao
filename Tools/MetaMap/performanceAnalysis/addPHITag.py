
'''
Function: Add annotation for scrubbed text
Auhor: Ao Li
Date: 24-05-2018
'''
import re

def stringTailor( str ):
	
	if str.find(" ") != -1:
		index = str.index(" ")
		str = str[index+1:]
	else:
		str = ""
	return str

def insert_str(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]

try:

	# Read Scrubbed File
	num ='90'
	fileType = 'original'
	fr = open('generatedFile/scrubbedText/'+num+'/scrubbed_'+fileType+'_test'+num+'.xml','r')
	fw = open('generatedFile/scrubbedText/'+num+'/scrubbed_'+fileType+'_annotation_test'+num+'.xml','w')
	fr_hospital_gs = open('generatedFile/goldStandard/'+num+'/hospital.txt','r')
	fr_location_gs = open('generatedFile/goldStandard/'+num+'/location.txt','r')
	fr_patient_gs = open('generatedFile/goldStandard/'+num+'/patient.txt','r')
	fr_doctor_gs = open('generatedFile/goldStandard/'+num+'/doctor.txt','r')
	
	lines = fr.readlines()
	hospitals = fr_hospital_gs.readlines()
	locations = fr_location_gs.readlines()
	patients = fr_patient_gs.readlines()
	doctors = fr_doctor_gs.readlines()


	for line in lines:
	
		# Position (Hospital + Location):
		# Hospital:
		
		for hospital in hospitals:
			hospital = hospital.rstrip()
			temp = line
			while temp:
				if re.match(hospital,temp, re.IGNORECASE):
					index = line.index(temp)
					line = insert_str(line,"<PHI TYPE=\"HOSPITAL\">",index)
					line = insert_str(line,"</PHI>",index+21+len(hospital))
				temp = stringTailor(temp)

		# Location:
		for location in locations:
			location = location.rstrip()
	        temp = line
	        while temp:
				if re.match(location,temp,re.IGNORECASE):
					index = line.index(temp)
					line = insert_str(line,"<PHI TYPE=\"LOCATION\">",index)
					line = insert_str(line,"</PHI>",index+21+len(location))
				temp = stringTailor(temp)

		# People (Patient + Doctor):
		# Patient:
		for patient in patients:
			patient = patient.rstrip()
			temp = line
			while temp:
				if re.match(patient,temp):
					index = line.index(temp)
					line = insert_str(line,"<PHI TYPE=\"PATIENT\">",index)
					line = insert_str(line,"</PHI>",index+20+len(patient))
				temp = stringTailor(temp)

		# # # Doctor:
		for doctor in doctors:
			doctor = doctor.rstrip()
			temp = line
			while temp:
				if re.match(doctor,temp):
					index = line.index(temp)
					line = insert_str(line,"<PHI TYPE=\"DOCTOR\">",index)
					line = insert_str(line,"</PHI>",index+19+len(doctor))
				temp = stringTailor(temp)

		fw.write(line)
		print "~~~~"

finally:
	fr.close()
	fw.close()
	fr_hospital_gs.close()
	fr_location_gs.close()
	fr_patient_gs.close()
	fr_doctor_gs.close()


