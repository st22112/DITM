import time

def tprint(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)

def tinput(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    return input()

#ok
name = tinput("What is your name? ")
tprint("I don't care about your name " + name)

time.sleep(2)
print("\n")

colour = tinput("What is your favorite colour " + name + "? ")
tprint("I like " + colour + " more than you")

time.sleep(2)
print("\n")

food = tinput("What is your favorite food " + name + "? ")
tprint("I also like " + food + " more than you")

time.sleep(5)
print("\n")

tprint("Thank you for this information, your data will be sent straight to /dev/null \n")

