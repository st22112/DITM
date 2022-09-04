# st22112
# 2022-09-05
# A rugby team has scored over the season 55 tries, 35 conversions, 48 penalties and 5 drop kicks. The points are 5 for a try, 3 for a penalty and a drop kick, 2 for a conversion. Calculate and display the total points for each category, and for the season.

tries = 55
conversions = 35
penalties = 48
drop_kicks = 5

total_tries = tries*5
total_conversions = conversions*2
total_penalties = penalties*3
total_drop_kicks = drop_kicks*3

total_points = total_tries + total_conversions + total_penalties + total_drop_kicks

print("Points for tries: {}\nPoints for conversions: {}\nPoints for penalties: {}\nPoints for drop kicks: {}\nTotal points: {}".format(total_tries,total_conversions,total_penalties,total_drop_kicks,total_points))
