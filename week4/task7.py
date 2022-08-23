# st22112
# 2022-08-22
# Your service station has a price list for diesel ($1.47 per litre),91 Unleaded ($2.06) and 95 Octane ($2.17).  Each price needs to be increased by 10% and stored again. Display the initial prices, calculate and store the new values, then display the prices again.
gas_prices = {
        "Diesel": 1.47,
        "91 Unleaded": 2.06,
        "95 Octane": 2.17
}
for i in gas_prices:
    print("{}:${}".format(i,gas_prices[i]))
for i in gas_prices:
    gas_prices[i] = gas_prices[i]*1.10
print()
for i in gas_prices:
    print("{}:${:0.2f}".format(i,gas_prices[i]))
