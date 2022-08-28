# st22112
# 2022-08-29
# ask user for weather and print response based on the input
weather = input("What is the weather? ").upper()
if weather == "RAINING":
    print("Pack an umbrella")
elif weather == "SUNNY":
    print("You need to have sunscreen")
elif weather == "WINDY":
    print("You should bring your jacket")
else:
    print("{}? I've never heard of that kind of weather before".format(weather.lower()))
