def start():
    print("you stand at the entrance of the bathroom. Do you?") #this is the start of the code/adventure
    print("1. Enter the bathroom")
    print("2. turn back and go to sleep")

    choice = input("> ")

    if choice == "1":
        enter_bathroom()
    elif choice == "2":
        go_sleep()
    else:
        print("invalid choice, try again")
        into_the_bathroom()

def enter_bathroom():
    print("you confidently step into the bathroom\n")
    into_the_bathroom()

    

def go_sleep():
    print("you choose that its a better idea to just go back to sleep\n")

    choice = input("> ")




def into_the_bathroom():
    print("You see a skibidi toilet, do you")
    print("1. Interact with Skibidi")
    print("2. Take a shower and ignore Skibdi")
    print("3. Brush your teeth and ignore Skibidi") #first endings

    choice = input("> ")

    if choice == "1":
        interact()
    elif choice == "2":
        shower()
    elif choice == "3":
        brush()
    else:
        print("Invalid choice, try again")

def interact():
    print("My name is Skibidi, but you can call me skib. I was wondering if you want to go on an adventure with me?\n")
    adventure_with_skib()


def shower():
    print("you decide to shower and ignore Skibidi. Your adventure ends here\n")

def brush():
    print("you decide to brush your teeth and ignore Skibidi, your adventure ends here\n")

    choice = input("> ")




def adventure_with_skib():
    print("Skib wants to take you on an adventure, do you")
    print("1. You start you adventure with Skib")
    print("2. Deny Skib and turn away the offer")



    choice = input("> ")

    if choice == "1":
        onward_with_skib()
    elif choice == "2":
        fanum_taxed()

    else:
        print("Invalid choice, try again")

def fanum_taxed():
      print("Skib is devastated, and can't afford for you to leak the secret adventure. He Fanum taxes your soul and you perish\n")
      exit()

def onward_with_skib():
    print("As soon as you step out, an evil shake from the Grimace clan presses up on you! Do you")
    print("1. Take out your plunger unleash your balkan rage and annihilate him") #skibidi toilet referece
    print("2. Forget the plunger and fight him with straight hands")


    choice = input("> ")

    if choice == "1":
        post_fight()
        
    elif choice == "2":
        post_fight()
    
    else:
        print("Invalid choice, try again")

def post_fight():
    print("Skib is proud of you and your victory, and wants to lie down for the night. Do you")
    print("1. set up camp and cuddle Skib, you both dream of victory")
    print("2. set up camp and have some dinner. You dont cuddle with Skib though")
    print("3. You dont want to set up camp, and want to keep following your target")

    choice = input("> ")

    if choice == "1":
        print("you cuddle with Skib all night long, embracing eachother and dreaming of victory\n")
        night_well_remembered()

    if choice == "2":
        print("you fall asleep after helping Skib set up camp, dreaming of victory\n")
        night_well_remembered()

    elif choice == "3":
        print("you and Skib keep walking... However you get attacked in the night. Without your contacts, you cant see in the night well. You perish to the hands of a Kay cenat meal soilder. Your adventure end here")
        exit()

    else:
        print("Invalid choice, try again")

def night_well_remembered():
    print("after waking up, you and skib towards the final opponent - Kai Cenat - and his lair. But how do you want to enter?")
    print("1. Right through the front, pulngers high and ready to fanum tax the Kai Cenat Soilders.")
    print("2. Sneak around back through the sewage system into the the jesters (aka Jonkler) living quaters")
    print("3. Climb the south wall and sneak into the John Porks butchery")

    choice = input("> ")

    if choice == "1":
        a_death_from_soilders()


    if choice == "2":
        night_night_jonkler()


    elif choice == "3":
        john_porks_encounter()


    else:
        print("Invalid choice, try again")

def a_death_from_soilders():
    print("You fall easily to the soilders, as you arent even that sigma and actually pretty beta. Your adventure ends here\n")
    exit()

def night_night_jonkler():
    print("You pop up inside the jonklers quaters and knock him out\n")
    into_the_castle() #WHY SO FIENIOUS

def john_porks_encounter():
        print("You climb over the wall and enter John Porks Butchery. However, he's pretty friendly and wont rat you out\n")
        into_the_castle() #john pork the assassin


def into_the_castle():
    print("after excaping your respective building. you enter the Kai Cenats main chamber, but he must be off streaming, as he is nowhere to be found. However a guard is coming! Do you")          
    print("1. Hide in chest at the foot of his bed")
    print("2. Hide in Kai's closet")


    choice = input("> ")

    if choice == "1":
        locked_in()

    elif choice == "2":
        safe_for_now()

    else:
        print("Invalid choice, try again.")

def locked_in():
    print("You get into the chest. unfortunately you get locked in. Your adventure ends here\n")
    exit()
def safe_for_now():
    print("You manage to escape the guard. Then sneak down the corridor, when hes gone\n")
    fork_in_the_road()

def fork_in_the_road():
    print("As you sneak down the corridor, but come to a fork in the hallway, you could go right, or left. Do you")
    print("1. you could go down the left hallway, which seems to be emitting a blue glow from a room at the end")
    print("2. Or you could go down the right, which is pulsating an evil purple aura")
#calm easy choice for the reader

    choice = input("> ")

    if choice == "1":
        chug_jug()

    elif choice == "2":
        grimaced()


def chug_jug():
    print("You go down the blue tinted hallway, to find a fortnite chug jug. You drink it and it replensihes you of your fatigue\n")
    final_battle()

def grimaced():
    print("You must be cognitively challenged, as you picked the evil one. You bump into a Grimace Captian. He slays you easily. Your adventure ends here\n")
    exit()


def final_battle():
    print("after healing and regrouping, you walk down Kai's hallway, However, he's mad sigma so he just bashes through his door to meet you halfway. Do you")
    print("1. Take out your plunger, charge at him and honorably fight Mr. Cenat")
    print("2. Submit, offer yourself for physical labor, or as a sevant.")

    choice = input("> ")


    if choice == "1":
        for_your_honor()

    elif choice =="2":
        final_death()


def for_your_honor():
        print("you bravely fight Sir Cenat, your battle lasts for ages, however you come out on top. This is the end of your adventure. You and Skib live the rest of your life as legends")
        exit()
        
def final_death():
        print("You attempt to run away from what wouldve been a winnable battle. But your 'beta'ness was your downfall. This is the end of your adventure, you arent remembered, and the Kai Colonies take over the Skibiverse")
        exit()
    
start()