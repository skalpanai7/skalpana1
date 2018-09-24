n=int(input())
list=[int(x) for x in raw_input().split()]
l=[]
for i in range(0,n):
	if list[i]==i:
		l.append(i)
			
			
if list[i] in l:
	l.sort()
	print " ".join(map(str,l))
else:
	print "-1"
