'''
Function: Read and Write .pkl file in python
Auhor: Ao Li
Date: 26-03-2018
'''
import cPickle as pickle  
f = open('whitelist2.pkl','r') 
f_w = open('positionDictionary/positionDictionary90.txt','r')
f_pkl = open('whitelist_test.pkl','w') 

# Read pkl Files:
info = pickle.load(f)  
print info   #show file


# Write pkl Files:
pickle.dump(lines,f_pkl,pickle.HIGHEST_PROTOCOL)