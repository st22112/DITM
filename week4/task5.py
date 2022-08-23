# st22112
# 2022-08-22
# You run an event management business. Your sporting venue seats 3000 when full. You have sold out the stadium for an All Blacks game, and want to sort out transport back to town for everyone after the game.
# You have booked 95 taxis that take 4 people each. You have booked 45 buses that take 40 people each. How many people will be left waiting for the buses to come back? How many buses do you need to come back for a second trip.
import math
people = 3000
people = people-95*4 # people-taxi
people = people-45*40 # people-busses
print("There are {} people left waiting for the bus\nWe need {} busses to come back".format(people,math.ceil(people/40)))
