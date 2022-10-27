tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
sort = []

print(tuple1)

for i in range(len(tuple1)):
    if len(sort) == 0:
        sort.append(tuple1[i])
    else:
        for j in range(len(sort)):
            if sort[j][1] > tuple1[i][1]:
                sort.insert(j, tuple1[i])
                break
            if j == len(sort)-1:
                sort.append(tuple1[i])

tuple1 = tuple(sort)
print(tuple1)
