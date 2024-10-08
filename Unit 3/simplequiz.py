def tally_score():
    score = 0
name = input("How do you spell your teacher's name?\n>")
if name == "Osowski":
    score = score + 1
age = input("How old is Osowski?\n>")
if age == "31":
    score = score + 1
color = input("What is Osowskis favorite color?\n")
if color == "Black":
    score = score + 1
print(score)
cloth = input("what pants is Osowski wearing?\n>")
if cloth == "Khakis":
    score = score + 1
beard = input("Is he clean shave?\n>")
if beard == "nah":
    score = score + 1
print(str(score) + "/5")

tally_score()



# string funciton
# string functions are a group of functions that modify string, they manipulate them
# .lower()
# .lower() changes the string to be all lowercase
x = "Lord of the rings"
x = x.lower()
print(x)

#.upper() changes the string to uppercase
# .capitalize() changes the entire string to lowercase, then capitalizes the first letter
# "hello world!" > "Hello world!"

#.title() changes the entire string to titlecase
# "Hello world!" > "Hello World!"

# .swapcase() inverts the capitalization of each character
# "Hello World!" > hELLO wORLD!""





