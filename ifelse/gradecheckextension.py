# st22112
# 2022-08-29
# Ask user for test scores and prints a message based on the input
def checker(i,j,ui,s):
    if i == "under":
        if ui < j:
            print(s)
    elif i == "over":
        if ui >= j:
            print(s)
    elif ui >= i and ui < j:
        print(s)

i = int(input("What was the test out of? "))
j = int(input("What was your mark? "))
grade = round(j/i*100)

print("Your grade is {}%".format(grade))

checker("under", 50, grade, "You got a F")
checker(50, 70, grade, "You got a C")
checker(70, 90, grade, "You got a B")
checker("over", 90, grade, "You got an A")
