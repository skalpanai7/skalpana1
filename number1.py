def nextPower_2 ( n ):
	value  =  1 
	while  ( value  <=  n):
		value  =  value << 1

	return  value 
n=int(input())
print(nextPower_2(n))
