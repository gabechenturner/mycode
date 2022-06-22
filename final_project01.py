#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import time
# Replace RPG starter project with this code when new instructions are live

# Character List

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Here are your characters
    
    Troll, White Walker, Martian, Amorphous Blob

    ========

    Commands:
      go [direction]
      use [item in inventory]
      get [item]
    ''')

    #pick your character
Character_name= input("pick one of the following Troll, White Walker, Martian, Amorphous Blob\n")

print(f"Hello {Character_name}")
time.sleep(5)
def showStatus():
    """determine the current status of the player"""
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'item' : 'bottle of vodka',
                  'hint' : 'use vodka to end game'
                 },

            'Kitchen' : {
                  'north' : 'Hall',
                  'west' : 'Garage',
                  'south' : 'Basement',
                  'item' : 'Block of C4'
                 },

            'Garage' : {
                  'east': 'Kitchen',
                  'item' : 'RPG'
                 },
            
            'Basement' : {
                  'north' : 'Kitchen',
                  'east' : 'Mine Shaft',
                  'item' : 'Siren'
                 },

            'Mine Shaft' : {
                'north' : 'Valhalla',
                'west' : 'Basement'
                 },

            'Valhalla' : {
                'west' : 'Kitchen',
                'south' : 'Mine Shaft'
                }

            }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:
    showStatus()


    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':  
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)
    #if they type 'hint' first
    if move[0] == 'hint':
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
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    #if they 'use' item then something happens

    if move[0] == "use":
        if "block of c4" in inventory and currentRoom == "Kitchen" and move[1] == "block of c4":
            print("You arm your C4 and blast a hole in the east, wall revealing a shining path to Valhalla!")
            rooms["Kitchen"]["east"]= "Valhalla"
            inventory.remove("block of c4")

    if move[0] == "use":
        if "siren" in inventory and currentRoom == "Mine Shaft" and move[1] == "siren":
            print("You use the siren and crumble the wall, deafening your ears but showering your eyes with the stunning awe of Valhalla from above! Will you continue to the north?")
            rooms["Mine Shaft"]["north"]= "Valhalla"
            inventory.remove("siren")

    if move[0] == "use":
        if "bottle of vodka" in inventory and currentRoom == "Hall" and move[1] == "bottle of vodka":
            if Character_name =="Troll":
                print("You quit and now your drunk, 'c'est la vie")
            inventory.remove("bottle of vodka")
            time.sleep(5)
            print("Bye, Bye :-(")
            exit()
