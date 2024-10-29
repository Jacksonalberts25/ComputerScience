import random

r = random.randrange(0, 10)
# first number is inclusive, second is exclusive
# 0 <= result < 10
print(r)

print("you hav a 25 percent chance to win")
p = random.random()
# random.random generates a random float between 0 and 1

if p <= 0.25:
    print("you win")
else:
    print("you lose")

