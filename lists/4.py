# st22112
# 2022-10-18
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly", "leftover items will get added at the end of the new list"]
list3 = []
if len(list1) > len(list2):
    c = len(list1)
else:
    c = len(list2)
for i in range(c):
    if i >= len(list1):
        list3.append(list2[i])
    elif i >= len(list2):
        list3.append(list1[i])
    else:
        list3.append(list1[i] + list2[i])
print(list3)
