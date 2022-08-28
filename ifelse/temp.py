# st22112
# 2022-08-29
# Ask for temperature and print response based on the value
temp = float(input("What is the temperature? "))
if temp >= 18 and temp <= 32:
    print("It is nice and warm today")
elif temp < 18:
    print("It is too cold for me.")
else:
    print("It's too hot for me!")
