i = 1
j = 100
totalsum = 0
average = 0
for count in range(i,j+1):
    totalsum = totalsum + count
average = totalsum / 100
print("sum of {} to {} is {}".format(i, j, totalsum))
print("average of the totalsum, {} is {}".format(totalsum, average))
