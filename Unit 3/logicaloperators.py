# logical operators
# arithmetic operators + - * / // ** %
# comparison operators < > >= <= == 
# logical operators ---- and or !(not)
# and means that both conditions must be true
# or means that at least one condition must be true
# ! (not) means the inverse, ex. != (not equal to)
def check_eligibility(age,exp):
    if age >= 18 and age <= 22:  #BOTH conditions ust be true
        print("you are eligible")
    else:
        print("you aint eligibile")

check_eligibility()

