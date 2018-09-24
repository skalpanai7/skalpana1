n=int(input())
list=[int(x) for x in raw_input().split()]
li=[]
for i in range(0,n):
	for j in range(i+1,n):
		
		if(list[i]==list[j]):
			li.append(list[i])
	if list[i] not in li:
		print list[i]
	n=int(input())
list=[int(x) for x in raw_input().split()]
li=[]
for i in range(0,n):
	for j in range(i+1,n):
		
		if(list[i]==list[j]):
			li.append(list[i])
	if list[i] not in li:
		print list[i]
	
