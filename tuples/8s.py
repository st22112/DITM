# teamwork with shun, yay
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29), ('duplicate test', 23))
list1 = []
print(tuple1)

for i in tuple1:
	a = 0
	for j in list1:
		if i[1]>=j[1]: # change < to > to reverse
			a += 1
	list1.insert(a, i)

tuple1 = tuple(list1)
print(tuple1)
