# st22112
# 2022-10-17
numbers=[1,2,3,4,5,6,7,8,9,10]
biggest = numbers[0]
smallest = numbers[0]
for i in numbers:
    if i > biggest:
        biggest = i
    if i < smallest:
        smallest = i
print("biggest is {}".format(biggest))
print("smallest is {}".format(smallest))
