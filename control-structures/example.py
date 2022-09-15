question = input("Would you like to know what the weather is like tommorow," " <yes or no> : ").lower()

if question == "yes" or question == "y":
    print("It will be raining tomorrow!")
elif question == "no" or question == "n":
    print("That's OK, you can find out tomorrow.")
else:
    print("I don't know what you mean!")
