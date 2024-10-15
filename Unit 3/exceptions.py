#exception handling
# write a program that asks for two numbers and divides them

#if = try
#elif = except with error type
#else = except
def divide_two_numbers():
    try:    # we always enter the try block, there is no condition
        x = int(input("what is the first number?\n>"))
        y = int(input("what is the second number?\n>"))
        print(x / y)

    except ZeroDivisionError:
        print("cannot divide by zero, try again.")

    except ValueError:
        print("please enter a valid numerical symbol, try again.")
        divide_two_numbers()

    except: # if anything in the try block causes an error, 
    #the try block stops immediately and the except is ran instead
    # then the except is ran
    # the rest of the try block never finishes running, its skipped
    # if the try block executes without an error, the except is kipped
    # the only way to get into the except is to "throw" an error
        print("idk what you did, but you brole it... try again.")
        divide_two_numbers()    #tell the function to run again
divide_two_numbers()


