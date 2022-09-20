import signal
signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGTSTP, signal.SIG_IGN)
# disable ctrl c and ctrl z
# ctrl d kills
import getpass

PASSWORD = "password"
while True:
    i = "null"
    while i != "":
        i = getpass.getpass("Press enter to continue or admin password (password) to quit: ")
        if i == PASSWORD:
            exit()

    income = 0
    tax = 0
    userinput = "null"
    print("\n\n----")
    userinput = input("Please enter your income per year: $").replace("$", "")
    if userinput.replace('.','',1).isdigit():
        userinput = float(userinput)
        if userinput <= 14000:
            print("Your tax rate is 10.5%")
            print("You will need to pay ${:0.2f}".format(userinput*0.105))
        elif userinput > 14000 and userinput <= 48000:
            print("Your tax rate is 17.5%")
            print("You will need to pay ${:0.2f}".format(userinput*0.175))
        elif userinput > 48000 and userinput <= 70000:
            print("Your tax rate is 30%")
            print("You will need to pay ${:0.2f}".format(userinput*0.30))
        elif userinput > 70000 and userinput <= 180000:
            print("Your tax rate is 33%")
            print("You will need to pay ${:0.2f}".format(userinput*0.33))
        else:
            print("You're too rich to calculate i guess")
    else:
        print("Invalid input\n\"{}\" entered".format(userinput))
    print("-----\n\n")
