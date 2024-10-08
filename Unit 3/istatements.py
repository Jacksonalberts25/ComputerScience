# if statements evaluate boolean expressions
#  they make decisions about which code to run next

#take a temperature
# print "temparature is hot"
temp = input("whats the temperature in f?\n>")
temp = int(temp)

# if <boolean expression> :
# should remind you of writing a function
# def <name>() :
if temp >= 80:
    print(str(temp)+ " is HOT")

if temp < 80:
    print(str(temp) + " is NOT hot...")
    

else:
    print(str(temp) + " is NOT hot")

# not all if statements need an else. in fact NONE of them NEED an else
    # else statemtents are an option, they are optional
    # all else statements must ahve a corresponding if statement
    # else statements cannot exist alone
    # an if statements can only have one else


# create a program that asks for a password
    # if the password is correct, print access granted
    # otherwise, print access denied
    # the password is skibidi68.9


password = input("skibidi68")
input_pass = input("whats the password?\n")

if input_pass == password:
    print("ACCESS GRANTED")

else:
    print("ACCESS DEBUED")


# acitvity 2, electric boogaloo
    # create a five question quiz that prints your score at the end
    # choose any five question

num1 = 


