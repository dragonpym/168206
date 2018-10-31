def sorf(a,b):
	c = []
	h = j = 0
	while j<len(a) and h<len(b):
		if a[j] < b[h]:
			c.append(a[j])
			j += 1
		else:
			c.append(b[h])
			h += 1
	if j==len(a):
		for i in b[h:]:
			c.append(i)
	else:
		for i in a[j:]:
			c.append(i)
	return c
	
def message(lis):
	if len(lis) <= 1:
		return lis
	mid = int(len(lis)/2)
	left = message(lis[:mid])
	eight = message(lis[mid:])
	return sorf(left,eight)
	
a = [15,45,88,65,21,45,7,56,15,54]
b = message(a)
print(a)
print(b)		
