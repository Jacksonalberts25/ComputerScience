#for loops 
#THis is a big deal
#for loops allow the programmers to repeat, or what we call loop

#write a program that prints the numbers 1 through 10
# each on a new line

fav_food = ["Eggs Bennies", "friend chicken", "man n cheese"]

# for<var> in <list>:

for i in range(90,101):
    print(i)

for food in fav_food:
    print(food)
    #runs all of the lines inside the foor loop
    #when it reaches the bottom of the list , it runs again
    #and moves on to the next item in the list
    #it ends when there are no list items left



for i in range(10,0,-1):#start, stop, step
    print(i)



#pratice problems
    
#print a cooldown
for countdown in range(10,0-1):
    print(countdown)



#sum of a list
for p in range(0,11):
    print(p)

#sum of a list
num = [68, 70, 419, 421, 665]
sum = 0 
for n in num:
    sum = sum + n
print(sum)


#squares of each number
ints = [3,2,5,4,1]
newlist = []
for i in ints:
    newlist.append(i*i)
print(newlist)

#character count

stringy = input("please enter a string\n")
numvowels = 0
for s in stringy:
    if s in ["a,", "e", "i", "o", "u"]:
        numvowels = numvowels + 1

print(numvowels)


#print mulitpication table

try:
    multi = int(input("gimme an int yo\n"))
except:
    print("womp, womp")

for i in range(00,multi+1):
    print(str(multi) + " x " + str(i) + " = " + str(multi*i))


#list of names
    names = {"peter", "john", "pual", "luke"}
    for name in names:
        print("hello, " + name + "!")
        