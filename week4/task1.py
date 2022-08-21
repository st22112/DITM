# st22112
# 2022-08-22
# Write a program which asks you what value gift card you have been given asks you for the name of the book you bought how much it cost then displays a summary of what you have bought and how much you have left on your card.
card = float(input("How much money is in your gift card? ").replace('$',''))
book = input("What is the name of the book you bought? ")
book_price = float(input("How much did the book cost? ").replace('$',''))
if book_price < card:
    print("You have bought the book \"{}\" which cost ${}\nYou have ${:0.2f} left is your gift card".format(book,book_price,card-book_price))
else:
    print("You have bought the book \"{}\" which cost ${:0.2f}\nYou have $0 left is your gift card".format(book,book_price))
