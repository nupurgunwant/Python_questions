#!/usr/bin/env python
T=int(raw_input())
for j in range(0,T):
	s=raw_input()
	string1=''
	string2=''
	for i in range(0,len(s),2):
		string1=string1+s[i] #creating a string of all even elements
	for i in range(1,len(s),2):
		string2=string2+s[i] #creating a string of all odd elements
	print(string1+' '+string2)
