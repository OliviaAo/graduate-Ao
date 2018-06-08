
'''
Function: Sort lines in a file
Auhor: Ao Li
Date: 30-04-2018
'''
try:
	# f = open('positionDictionary/positionDictionary50.txt','r')
	f = open('hospital_names_expand.txt','r')
	f_sort = open('hospital_names_expand_sort.txt','w')
	lines = f.readlines()
	lines.sort()
	f_sort.writelines(lines)
finally:
	f.close()
	f_sort.close()