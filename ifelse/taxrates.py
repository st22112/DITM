import signal
signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGTSTP, signal.SIG_IGN)
# disable ctrl c and ctrl z
# ctrl d 

PASSWORD = "."
i = ""
while i == "":
    print("\n\n----")
    income = 0
    tax = 0
    userinput = input("Please enter your income per year: ").replace("$", "")
    if !userinput.isdigit():
        break()

    i = input("Press enter to continue or admin password to quit: ")
    if i == PASSWORD:
        exit()
    while i != "":
        i = input("Press enter to continue or admin password to quit: ")
