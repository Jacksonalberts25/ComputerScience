wind = input("whats the wind speed?")
wind = int(wind)


if wind < 74:
    print("Category 1")
   

elif wind < 111:
    print("Category 2")

elif wind < 130:
    print("Category 3")

elif wind < 157:
    print("Category 4")

elif wind > 157:
    print("Category 5")


