#i!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""
import sys
import time

# Character List
# Troll, White Walker, Martian, Amorphous Blob
def print1by1(text, delay=0.03):
    # function imported for printing line 1 by 1
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def showInstructions():
    
    """Show the game instructions when called"""
    #print a main menu and the commands
    print1by1('''

    Sub-par RPG Game
   
    ========
    
    Now that you've picked a charcter, feel free to explore the environment,
    but don't worry this game isn't very difficult, the programmer is pretty lame

    ========
    
    Make it to Valhalla, or just quit, either one is fine with me

    Commands:
      map [see "The Map"]
      go  [north, south, east, west]
      use [item in inventory]
      get [item]
    ''')

    #pick your character
Character_name= input("pick one of the following Troll, White Walker, Martian, Amorphous Blob\n")

print1by1(f"Hello {Character_name}...")
time.sleep(3)
def showStatus():
    """determine the current status of the player"""
    #print the player's current status
    print('---------------------------')
    print(f"The {Character_name}" ' is in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
        print("---------------------------")
    if "hint" in rooms[currentRoom]:
        print('Theres a hint in here, ' + rooms[currentRoom]['hint'])
    

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'item' : 'bottle of vodka',
                  'hint' : 'use vodka to quit game'
                 },

            'Kitchen' : {
                  'north' : 'Hall',
                  'west' : 'Garage',
                  'south' : 'Basement',
                  'item' : 'Block of C4',
                  'hint' : 'use C4 to find Valhalla'
                 },

            'Garage' : {
                  'east': 'Kitchen',
                  'item' : 'RPG',
                  'hint' : 'besides getting a cool rocket, you cant win here'
                 },
            
            'Basement' : {
                  'north' : 'Kitchen',
                  'east' : 'Mine Shaft',
                  'item' : 'Siren',
                  'hint' : 'use Siren in the mineshaft, to the east to win'
                 },

            'Mine Shaft' : {
                'west' : 'Basement'
                 },

            'Valhalla, you done well' : {
                'west' : 'Kitchen',
                'south' : 'Mine Shaft',
                },

            }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:
    showStatus()

    #get the player's next 'move'
    move = ''
    while move == '':  
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)
    
    # shows the map when called
    if move[0] == 'map':
        print('''

                  "The Map"

                    Hall

        Garage     Kitchen      Valhalla
                      
                   Basement     Mineshaft
            ''')
    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1].upper() in rooms[currentRoom]['item'].upper():
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' aquired!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    
    #if they 'use' item then something happens

    if move[0] == "use":
        if "block of c4" in inventory and currentRoom == "Kitchen" and move[1] == "block of c4":
            print1by1("You arm your C4 and blast a hole in the east wall, revealing a shining path to Valhalla!\n")
            rooms["Kitchen"]["east"]= "Valhalla"
            inventory.remove("block of c4")
            time.sleep(3)
            print1by1("Well, that was anti-climatic, oh yea, you win\n")
            time.sleep(3)
            exit()
    
    if move[0] == "use":
        if "RPG" in inventory and currentRoom == "Garage" and move[1] == "RPG":
            if Character_name == "Troll":
                print1by1("Good job, now your dead")
                inventory.remove("RPG")
                time.sleep(3)
                exit()

    if move[0] == "use":
        if "siren" in inventory and currentRoom == "Mine Shaft" and move[1] == "siren":
            print1by1("You use the siren and crumble the wall, deafening your ears but showering your eyes with the stunning awe of Valhalla from above! Will you continue to the north and claim your spot?\n")
            rooms["Mine Shaft"]["north"]= "Valhalla"
            inventory.remove("siren")
            time.sleep(4)
            print1by1("You did and now... you died\n")
            time.sleep(3)
            exit()

    if move[0] == "use":
        if "bottle of vodka" in inventory and currentRoom == "Hall" and move[1] == "bottle of vodka":
            
            if Character_name =="White Walker":
                print1by1("You see a dragon, riden by John Snow in a loin cloth, things are getting really weird, sooo, let's just end it\n")
                time.sleep(3)
                print1by1("Bye, Bye ;-$\n")
                time.sleep(3)
                exit()

            if Character_name =="Troll":
                print1by1("Now your drunk, and don't wanna play anymore, 'c'est la vie\n")
                time.sleep(3)
                print1by1("Bye, Bye :-(\n")
                time.sleep(3)
                exit()

            if Character_name =="Martian":
                print1by1("Now that Congress has acknowledged my existance, I can longer go home, time to make a movie where I slap Will Smith....\n")
                time.sleep(3)
                print1by1("Too soon???\n")
                time.sleep(3)
                exit()
            
            if Character_name =="Amorphous Blob":
                print1by1("You know how Vodka thins the blood, well, it also has the same effect on blobs.... there's a drain nearby...... and your gone...\n")
                time.sleep(3)
                exit()
