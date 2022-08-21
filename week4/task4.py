# st22112
# 2022-08-22
# Write a program so it takes the dollar value of a purchase as an input from the user and displays the amount of GST to be added and then the price including GST.
gst = 0.15
cost = float(input("Insert a dollar value without GST "))
cost_gst = cost*gst
print("The amount of GST to be added is ${:0.2f}\nIt will cost ${:0.2f} altogether".format(cost_gst,cost_gst+cost))
