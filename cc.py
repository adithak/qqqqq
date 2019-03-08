import sy
def make_equal(inp,extras):
	t=0
	r=0
	for x in range(0,len(inp)):
		if '|' not in inp[:x+1]:
			t+=1
		else:
			r+=1
	r-=1
	for y in range(0,len(extra)):
		if t>r:
			inp=inp+extra[y]
			r+=1
		else:
			inp=extra[y]+inp
			t+=1
	if t==r:
		return inp
	else:
		return "Impossible"

inp=raw_input()
inp=inp.upper()
i=0
for x in inp:
	if inp[i] in inp[i+1:]:
		sy.exit("Input has Repeated Weights")
	i+=1
	
i=0
if '|' in inp:
	extra=raw_input()
	extra=extra.upper()
	for x in extra:
		if extra[i] in extra[i+1:] or extra[i] in inp:
			sy.exit("Input has Repeated Weights")
		i+=1
	print make_equal(inp,extra)
else:
	sys.exit("Invalid input")
