# st22112
# 2022-09-05
# A family has spent the afternoon picking berries, and will be charged by the total weight at the rate of $5 per kg. They have picked 9 buckets, 13 boxes and 14 punnets. A punnet weighs 250 grams. A box weighs 1.5kg. A bucket weighs 7 kg. Calculate and display the total charge.

charge = 5 # charge per kg
buckets = 9
boxes = 13
punnets = 14

total_charge = (buckets*1.5 + boxes*7 + punnets*0.25)*charge
print("Total charge: ${}".format(total_charge))
