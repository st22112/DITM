# st22112
# 2022-08-22
# Calculate, and display a team's total game points for 3 matches.
# They scored 7 in the first match, 5 in the second and 10 in the third.
match_scores = [7, 5, 10]
total = 0
for i in match_scores:
    total = total + i
print("Total score: {}".format(total))
