# st22112
# 2022-08-29
# Ask user for temperature in celsius and prints a message based on the input
def checker(i,j,ui,s):
    if i == "under":
        if ui < j:
            print(s)
    elif i == "over":
        if ui >= j:
            print(s)
    elif ui >= i and ui < j:
        print(s)

temp = float(input("What is the temperature(In celcius)? "))

checker("under", 0, temp, "The temperature is freezing.")
checker(0, 10, temp, "The temperature is very cold.")
checker(10, 20, temp, "The temperature is cold.")
checker(20, 30, temp, "The temperature is good.")
checker(30, 40, temp, "The temperature is hot.")
checker("over", 40, temp, "The temperature is very hot.")
