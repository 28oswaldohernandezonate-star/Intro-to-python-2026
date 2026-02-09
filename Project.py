import os, time #os allows to command line time allows to create slowtext 

# creates the letter by letter visueal while text is displayed
def slowText(text, delay=0.01):
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
    time.sleep(3)
    livingRoom()


# livingroom gives you option to switch room by putting in input

def livingRoom(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are in the living room. There are doors to the kitchen, bedroom, and garden.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "kitchen":
        kitchen()
    elif choice == "bedroom":
        bedroom()
    elif choice == "garden":
        garden()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(2)
        livingRoom()


def kitchen(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are in the kitchen. There is a door to the living room.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "living room":
        livingRoom()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(2)
        kitchen()

def bedroom(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are in the bedroom. There are doors to the living room and garden.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "living room":
        bedroom()
    elif choice == "garden":
        garden()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(2)
        bedroom()

def garden(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are in the garden. There are doors to the bedroom and living room.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "bedroom":
        bedroom()
    elif choice == "living room":
        livingRoom()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(2)
        garden()




playerName = ""
start()

