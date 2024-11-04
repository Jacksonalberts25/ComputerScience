import random
#python has four types of collections
# tuple
# set 
# >list
# >dictionary

# today we focus on lists
# a list is a way to store more than one value in a single variable
#the values in the list are called items
#items can be accessed by their INDEX (position in the list) 
# index                     0                   1       2                   3           4
best_elden_ring_weapons = ["Blasphemous", "moonveil", "Rivers of blood", "iron ball", "bloodhounds fang"]
best_years = [1776, 1985, 1994, 1957, 2016]


print(best_years[0])
print(best_elden_ring_weapons[0])
print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1])



#list functions
#.pop()
#removes an item at a given index
best_elden_ring_weapons.pop(1) #remove moonveil from the game

#.remove()
#removes an item  by value - removes the first instance of the value

best_elden_ring_weapons.remove("Blasphemous") # if value doesnt exist, it errors

#.append()
# adds the value as a new item to the end of the list
best_elden_ring_weapons.append("deaths poker")
numbers = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
print(numbers)
#.sort()
#sorts the numbers from smallest to greatest
numbers.sort()
print(numbers)

#max()
#print the largest number in the list
print(max(numbers))

#min()
#prints the smallest number in the list
print(min(numbers))

#strings.... are just.... lists of characters :0
print(len("owsowski"))



