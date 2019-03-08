import sys,string, math, itertools
b = int(input())
Sm = []
if b==2 :
    print('3')
    print('2 1 2')
    sys.exit()
if b==3 :
    print('4')
    print('2 1 3 2')
    sys.exit()
kl = b//2
for i in range(2,b+1,2) :
    Sm.append(i)
for i in range(1,b,2 ) :
    Sm.append(i)
for i in range(2,b+1,2 ) :
    Sm.append(i)
print(len(Sm))
