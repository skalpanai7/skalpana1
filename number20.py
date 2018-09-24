n=int(input())
list=[int(x) for x in raw_input().split()]
list.sort()
l=list[::-1]
print ''.join(map(str,l))
