fib1 = 0
fib2 = 1
fibtemp = 0
print(fib1)
print(fib2)
for i in range(10-2):
    fibtemp = fib1 + fib2
    fib1 = fib2
    fib2 = fibtemp
    print(fibtemp)
