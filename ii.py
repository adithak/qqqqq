def oddeven():
	m=int(input())
	p=[]
	for i in range(m):
		p.append(int(input()))
	w,f=[],[]
	for i in range(m):
		if i%3==0 and l[i]%3!=0:
			w.append(p[i])
		elif i%3!=0 and l[i]%3==0:
			w.append(p[i])
	print(w)
try:
	oddeven()
except:
	print('invalid')
