# st22112
# 2022-08-29
# Finds and prints the largest of three number
SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
def get_ordinal(i):
    # Adapted from https://codereview.stackexchange.com/questions/41298/producing-ordinal-numbers
    if 10 <= i % 100 <= 20:
        return 'th'
    else:
        return SUFFIXES.get(i % 10, 'th')

# Add as many numbers as you wish
numbers = [12, 25, 52]
ranking = [0, 0]
n = 1
for i in numbers:
    print("{}{} Number = {}".format(n,get_ordinal(n),i))
    if n==1 or ranking[1] < i:
        ranking[0] = n
        ranking[1] = i
    n += 1
print("The {}{} Number is the greatest among the three".format(ranking[0],get_ordinal(ranking[0])))
