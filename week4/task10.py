# st22112
# 2022-09-05
# Your iTunes account has a starting balance of $100. You buy 3 short tracks at $1.79, four medium tracks at $2.50 and 2 long tracks at $4.50. Calculate, and display your new account balance.

balance = float(100)

balance = balance - 3*1.79
balance = balance - 4*2.5
balance = balance - 2*4.5
print("${}".format(balance))
