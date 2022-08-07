# st22112
# 2022-08-08

clothes = float(input("How much do you spent on clothes each month? ").replace('$',''))
transport = float(input("How much do you spent on transport each month? ").replace('$',''))
food = float(input("How much do you spent on food each month? ").replace('$',''))
rent = float(input("How much do you spent on rent each month? ").replace('$',''))
other = float(input("How much do you spent on other stuff each month? ").replace('$',''))
print("You spend a total of ${:0.2f}".format(clothes + transport + food + rent + other))
