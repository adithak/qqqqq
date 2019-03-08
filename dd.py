import sys,string, math, itertools

l,q = input().split()
l,q = int(l),int(t)
m = [ int(x) for x in input().split()]
for i in range(0,l) :
    if (86400-m[i]) >= q :
        print(i+1)
        sys.exit()
    q -= (86400-m[i])
