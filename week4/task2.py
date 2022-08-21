# st22112
# 2022-08-22
# Write a program which takes as input from the user the weight of flour in grams and displays the equivalent number of cups using the formula 125g flour = 1 cup
flour = float(input("How much flour do you have in grams? ").replace('G','').replace('g',''))
if flour == 125:
    print("You have 1 cup of flour")
else:
    print("You have {} cups of flour".format(flour/125))
