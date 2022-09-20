PASSWORD = "no"
userinput = ""

while userinput != PASSWORD:
    userinput = input("Enter password: ")
    if userinput != PASSWORD:
        print("Sorry the value entered in incorrect - try again.")
print("Thank you. You have entered the correct password")
