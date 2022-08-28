# st22112
# 2022-08-29
# Ask for temperature and print response based on the value
temp = float(input("What is their temperature? "))
age = int(input("What is their age? "))
print("Thier age is: {}\nThier temperature is: {}".format(age, temp))
if age <2 and temp >= 38:
    print("Call a doctor")
elif temp > 39.5:
    print("High Fever")
