

prime = True
cost = 20
age = 17
consent = False

if prime:
    if age >= 18:
        print("Free shipping applied sigma")
    elif consent:
        print("Free shipping applied sigma")
    else:
        print("No free shipping for you beta")

elif cost >= 25:
    if age >= 18:
        print("free shipping applied sigma")
    elif consent:
        print("free shipping applied sigma")
    else:
        print("no free ship for you beta")

else:
    print("no free shipping or you beta")
     

raining = input("is it raining outside?")
outside = input("do you plan on going outside?")


if raining.lower() == "yes":
    outside = input("do you plan on going outside")
    
    if outside.lower("yes"):
        print("bring an umbrella")
    else:
        print("no umbrella")
else: 
    print("no umrbrella")

