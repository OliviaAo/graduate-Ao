

f = open('locations_ambig.txt','r')
f1 = open('sorted.txt','w')
lines = f.readlines();

lines.sort()

for line in lines:
	f1.write(line)

f.close()
f1.close()