#!/usr/bin/env python
#this code is facing some runtime error that i couldnt fix till the deadline
a=raw_input()
b=[] #list of all elements of string a
c=[] #a new array where we insert the elements of a in a new place such that its not their original place

for i in range(0,len(a)):
	b.append(a[i])




for i in range(0,len(a)-1):
	for j in range(1,len(a)):
		if a[i]!=b[j]:
			c.insert(j,a[i])
			break
			
c[0]=a[len(a)-1]
print(''.join(c))
	
