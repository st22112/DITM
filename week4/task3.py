# st22112
# 2022-08-22
# Write a program which takes as input from the user their height in metres and displays the equivalent height in whole inches, and in feet and inches. Use the formula 1 metre = 39.37 inches. 1 foot = 12 inches.
height_metre = float(input("What is your height in metres? ").replace('m','').replace('M',''))
height_inches = height_metre*39.37
print("your height in inches is={}".format(height_inches))
height_feet = int(height_inches/12)
height_inches = height_inches%12
print("Your height in feet and inches is {}\'{:0.2f}\"".format(height_feet,height_inches))
