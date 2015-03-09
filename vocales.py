import sys
N = int(sys.argv[1])
with open("Sainte-Beuve.txt", "r") as myfile:
	data = [next(myfile) for x in xrange(N)] #.readlines(:4)
vow = 0
conso = 0
for i in range(len(data)):
	for e in range(len(data[i])):
		if data[i][e]=="a" or data[i][e]=="e" or data[i][e]=="i" or data[i][e]=="o" or data[i][e]=="u":
			vow += 1
		elif data[i][e]=="A" or data[i][e]=="E" or data[i][e]=="I" or data[i][e]=="O" or data[i][e]=="U":
			vow += 1
		else:
			conso += 1
	print("en la linea",i,"el numero de vocales es",vow)
	vow = 0			
#print vow
#print type(data[0])
