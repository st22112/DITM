# print second element from array
words = ["bat", "cat", "hat", "mat"]
print(words[1])
print()

# print random element from array
import random
myword = random.choice(words)
print(myword)
print()

# ok
ages = [4, 7, 34, 7, 53]
print(ages)
print(ages[0])
print(ages[3])
print()

#
animals = ["pupper", "doggo", "woofer"]
for animal in animals:
    print("I'd like a {}".format(animal))
print()

#
numbers = [3, 7, 43, 12, 9, 11]
for number in numbers:
    print("{}x2={} ".format(number, 2*number))
