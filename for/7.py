start = int(input("What number should I count from: "))
stop = int(input("What number should I count up to: "))
up = int(input("What number should I count up in: "))
for i in range(start, stop+1, up):
    print(i)
