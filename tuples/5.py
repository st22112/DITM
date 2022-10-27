tuple1 = (11, 22)
tuple2 = (99, 88)

print(tuple1)
print(tuple2)
print()

temptuple = tuple1
tuple1 = tuple2
tuple2 = temptuple

print(tuple1)
print(tuple2)
