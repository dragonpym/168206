	def Message(arrays,left,eight):
	mid = len(arrays)/2
	mid = int(mid)
	if left == mid or mid == eight:
		if int(arrays[left-1]) > int(arrays[eight-1]):
			arrays[left-1],arrays[eight-1] = arrays[eight-1],arrays[left-1]
		return arr
	else:
		arrays1 = Message(arrays[:mid],left,mid)
		a = int(eight) - int(mid)
		arrays2 = Message(arrays[mid:],left,a)
		return sorf(arrays1,arrays2)

def sorf(arr1,arr2):
	arr = []
	while len(arr1)!=0 and len(arr2)!=0:
		if arr1[0] >= arr2[0]:
			arr.append(arr2.pop(0))
		else:
			arr.append(arr1.pop(0))
	if len(arr1)==0:
		for i in range(0,int(len(arr2))):
			arr.append(arr2[i])
	else:
		for i in range(0,int(len(arr1))):
			arr.append(arr1[i])
	return arr
	
arrge = [1,5,2,3,4,8,7,6]
arrge2 = Message(arrge,1,int(len(arrge)))
print(arrge)
print(arrge2)	
