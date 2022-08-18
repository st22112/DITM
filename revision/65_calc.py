# st22112
# 2022-08-18
# Calculate which year a person will be 65

import datetime
year_65 = int(input("What year were you born in? "))+65
if year_65 < datetime.datetime.now().year:
    print("You were 65 in the year " + str(year_65))
elif year_65 == datetime.datetime.now().year:
    print("You are 65 this year")
else:
    print("You will be 65 in the year " + str(year_65))
