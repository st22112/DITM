import time, sys

def tprint(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)

#ok
print("ok")
x=1
y=1.13
stringThing="wow, a string"
print(x , "\t" , y , "\t" , stringThing)

tprint("What is your name? "),
name = input()
tprint("I don't care about your name " + name)

time.sleep(2)
print("\n")

tprint("What is your favorite colour " + name + "? "),
colour = input()
tprint("I like " + colour + " more than you")

time.sleep(5)
print("\n")
tprint("f**k off " + name + "\n")
