# teamwork with shun, yay
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
list1 = []

for i in tuple1:
    a = 0
    for j in tuple1:
        if i[1]<j[1]: # change < to > to reverse
            a = a+1
    list1.append(tuple1[a])

tuple1 = tuple(list1)
print(tuple1)
