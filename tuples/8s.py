tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
list1 = []
list2 = []
for i,j in tuple1:
	a=0
	for k,l in tuple1:
		if j>l:
			a = a+1
	list1.append(a)
b=0
for x in tuple1:
	list2.insert(list1[b],x)
	b=b+1
tuple1 = tuple(list2)
print (tuple1)
