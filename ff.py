a=[]
m=[]
m1=[]
m2=[]
n=int(input('no of elements? \n'))
for x in range(0,n):
	num=int(input())
	arr.append(num)
for x in a:
	if x not in m:
		m.append(x)
	else:
		m1.append(x)
for x in m:
	if x not in t1:
		m2.append(x)
print (m2)
