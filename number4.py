n=int(input())
list=[int(x) for x in raw_input().split()]
li=[]
for i in range(0,n):
	for j in range(i+1,n):
		
		if(list[i]==list[j] and list[i] not in li):
			li.append(list[i])
			
			
if list[i] in li:
	li.sort()
	print " ".join(map(str,li))
else:
	print "unique"

