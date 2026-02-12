import os, time #os allows to command line time allows to create slowtext 

# creates the letter by letter visueal while text is displayed
def slowText(text, delay=0.07):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  


#Starts by getting name and introducing the rooms then playing you in living room. missing choice to pick room.
def start():
    global playerName
    os.system('cls' if os.name == 'nt' else 'clear') # checking for somthing related to input 
    slowText("Welcome to the game! Please enter your name: ")
    playerName = input()
    slowText("Hello, {}! You find yourself in the living room of a mysterious house.".format(playerName))
    slowText("From here, you can go to the kitchen, the bedroom, or the garden.")
    time.sleep(2)
    livingRoom()


# livingroom gives you option to switch room by putting in input

def livingRoom(): 
    global inv
    os.system('cls' if os.name == 'nt' else 'clear')
    print("backpack: {}".format(backpack))
    slowText("You are in the living room. There are doors to the kitchen, bedroom, and garden. You can also search for items")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "kitchen":
        kitchen()
    elif choice == "bedroom":
        bedroom()
    elif choice == "garden":
        garden()
    elif choice == "search for items":
        slowText("You searched the room and found a ")
    else:
        print("Invalid choice. Please try again.")
        time.sleep(2)
        livingRoom()


def bedroom(): 
    global inv
    os.system('cls' if os.name == 'nt' else 'clear')
    print("backpack: {}".format(backpack))
    slowText("You are in the bedroom. There is a door to the living room. You can also search for items")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "living room":
        livingRoom()
    elif choice == "search for items":
        if search(backpack, "shovel"):
            slowText("You searched the bedroom and found nothing...")
            time.sleep(2)
            bedroom()
        else:
            slowText("You searched the bedroom and found a flashlight, do you want to pick it up?")
            choice = input().strip().lower()
            if choice == "yes":
                backpack.append("flashlight")
                time.sleep(2)
                bedroom()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(2)
        bedroom()

def kitchen(): 
    global inv
    os.system('cls' if os.name == 'nt' else 'clear')
    print("backpack: {}".format(backpack))
    slowText("You are in the kitchen. There are doors to the living room and garden. You can also search for items")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "living room":
        bedroom()
    elif choice == "garden":
        garden()
    elif choice == "search for items":
        if search(backpack, "paper clip"):
            slowText("You searched the kitchen and found nothing...")
            time.sleep(1)
            kitchen()
        else:
            slowText("You searched a junk draw in the kitchen and found a paper clip, do you want to pick it up?")
            choice = input().strip().lower()
            if choice == "yes":
                backpack.append("paper clip")
                slowText("You picked up a paper clip")
                kitchen()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(2)
        bedroom()

def garden(): 
    global inv
    os.system('cls' if os.name == 'nt' else 'clear')
    print("backpack: {}".format(backpack))
    slowText("You are in the garden. There are doors to the kitchen and living room. You can also search for items")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "kitchen":
        kitchen()
    elif choice == "living room":
        livingRoom()
    elif choice == "search for items":
        if search(backpack, "shovel"):
            slowText("You searched the garden and found nothing...")
            time.sleep(1)
            garden()
        else:
            slowText("You searched the garden and found a shovel, do you want to pick it up?")
            choice = input().strip().lower()
            if choice == "yes":
                backpack.append("shovel")
                slowText("You picked up a shovel")
                garden()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(2)
        garden()

def search(pack, item):
    found = False
    for i in range (len(pack)):
        if pack[i] == item:
            found = True
    return found 

backpack = []
playerName = ""
start()

