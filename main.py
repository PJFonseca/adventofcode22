from array import array

file1 = open("input.txt", "r")

#read all lines
lines = file1.readlines()
index=0
elfs = [0]
#traverse through lines one by one
for line in lines:
	line = line.rstrip('\n')
	print(len(line))
	if len(line)>0:
		sum=(elfs.index(index)+int(line))
	else:
		index+=1
	if index==1:
		break
#close file
file1.close
print(elfs)
elfs.sort(reverse=True)
print(elfs[0])
