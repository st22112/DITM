# st22112
# 2022-10-17
a = [100,200,300,400,500]
print(a)

lowc = 0
highc = len(a)-1
temp = 0
while (lowc != highc or lowc > highc):
    temp = a[lowc]
    a[lowc] = a[highc]
    a[highc] = temp
    lowc +=1
    highc -= 1
print(a)
