# create a function called free_shipping
# that tells you if you qualify for free shipping or not
# You only get free shipping if 
# you are a prime member, OR order is at least 25$
# and you are atleast 18 years old, or have parent consent
# your function should take four parameters
# prime (boolean), cost (float), age (int), consent (boolean)
# HUGE HINT!
# you can use more than one logical operator in a condition
# use parenthesis to group if needed

def free_shipping(age, consent, prime):
    if age >= 18 and consent == True and prime == True:
        print("25 dollars for item, 0 dollars for shipping")
    else:
        print("yeah man you are NOT getting free shipping")

free_shipping(18, True, True)
