# st22112
# 2022-08-18
# Calculate percentage of test

test_type = input("What kind of test did you do? ")
total = int(input("How many questions were there? "))
score = int(input("How many did you get correct? "))
score = (score/total)*100
print("You got {}% for the {}".format(score,test_type))
