# Removing duplicate items form a  list 


l=[1,2,4,5,7,4,2,5,2,6,7,8,9,4]
s=[]

for i in l:
	if i not in s:

		print i 
		s.append(i)
		print s
