# st22112
# 2022-09-05
# I have 2 bank balances, one contains $100.00 in US$, the other $100.00 in AUS$. Write a money conversion to display your total worth in NZ$. The exchange rates can be found online by researching “Exchange Rates”.

us_balance = float(100)
au_balance = float(100)

print("NZD ${:0.2f}".format(us_balance*1.64+au_balance*1.11))
