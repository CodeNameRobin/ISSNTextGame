# Heather Robinson Text Based Game

aval_directions = {  # DICTIONARY of rooms wth directions
    'Command Center': {
        'south'
    },
    'Med Bay': {
        'north', 'south', 'east', 'west'
    },
    'Barracks': {
        'north', 'south', 'east' 'west'
    },
    'Provision Hall': {
        'south', 'east'
    },
    'Kitchen': {
        'north', 'east'
    },
    'Dinning Hall': {
        'east', 'west'
    },
    'Cryo Dock': {
        'south', 'west'
    },
    'Docking Bay': {
        'north', 'west'
    },
    'Equipment Room': {
        'east', 'west'
    }
}

rooms_commands = {  # room commands - directionals and items
    'Command Center':
        dict(south='Med Bay', items='none'),
    'Med Bay':
        dict(north='Command Center', south='Barracks', east='Cryo Dock', west='Provision Hall', items='medkit'),
    'Barracks':
        dict(north='Med Bay', south='Engine Room', east='Equipment Room', west='Dinning Hall',
             items='armor'),
    'Dinning Hall':
        dict(east='Barracks', west='Kitchen', items='schematics'),
    'Kitchen':
        dict(north='Provision Hall', east='Dinning Hall', items='extinguisher'),
    'Provision Hall':
        dict(south='Kitchen', east='Med Bay', items='oxygen'),
    'Equipment Room':
        dict(east='Docking Bay', west='Barracks', items='toolkit'),
    'Cryo Dock':
        dict(south='Docking Bay', west='Med Bay', items='weapon'),
    'Docking Bay':
        dict(north='Cryo Dock', west='Equipment Room', items='keycard'),
    'Engine Room':
        dict(no='barracks')
}


def intro():
    """Intro of the game. Gives the entry setup as well as asking if the user wants to play"""
    print(
        "  _____         _                             _    _                       _    _____  _                     _      _          _   _                    \n"
        " |_   _|       | |                           | |  (_)                     | |  / ____|| |                   | |    (_)        | \ | |  \n"
        "   | |   _ __  | |_  ___  _ __  _ __    __ _ | |_  _   ___   _ __    __ _ | | | (___  | |_  __ _  _ __  ___ | |__   _  _ __   |  \| |  ___ __   __ __ _ \n"
        "   | |  | '_ \ | __|/ _ \| '__|| '_ \  / _` || __|| | / _ \ | '_ \  / _` || |  \___ \ | __|/ _` || '__|/ __|| '_ \ | || '_ \  | . ` | / _ \\ \ / // _` |\n"
        "  _| |_ | | | || |_|  __/| |   | | | || (_| || |_ | || (_) || | | || (_| || |  ____) || |_| (_| || |   \__ \| | | || || |_) | | |\  || (_) |\ V /| (_| |\n"
        " |_____||_| |_| \__|\___||_|   |_| |_| \__,_| \__||_| \___/ |_| |_| \__,_||_| |_____/  \__|\__,_||_|   |___/|_| |_||_|| .__/  |_| \_| \___/  \_/  \__,_|\n"
        "                                                                                                                      | | \n"
        "                                                                                                                      |_| \n")
    print("Would you like to play?\n"
          "YES or NO")
    play_game = input('>').lower()
    issn_welcome = "Welcome to the International Starship Nova!\nAlso known as the ISSN.\n"
    briefing1 = "\nYou have been chosen for a maintenance shift as you " \
                "where briefed on prior to launch.\nAs your contract stated it " \
                "will be a 2 week shift to help maintain various " \
                "parts of the ship.\nYou have been chosen based on your " \
                "skill set and passenger number.\n" \
                "As you may have noticed the are cardinal directions on this ship,\n" \
                "it has been magnetized for human convenience.\n" \
                "Please refer to these directions when making your way around the ship.\n" \
                "---------------------------------------------------"  # an introdutory paragraph
    intro_one = "It has been a week since you woke up on the ISSN, along with your fellow crewmates \n" \
                "Dr. Suki Yomura and Leroy Hinks. \n" \
                "It has been calm as you worked on the general maintenance of the ship, \n" \
                "Dr. Yomura tended to your fellow shipmates \n" \
                "currently in cryo, and Hinks tended to the BioDome as well as the \n" \
                "embryos of future husbandry animals.\n" \
                "Together with your current maintenance team as well as the past and future teams, \n" \
                "you know you will all make it to Alfa Centauri.\n" \
                "You have been doing some routine sensor maintenance in the command center when-\n" \
                "BEEP--BEEP--BEEP--BEEP--BEEP--\n" \
                "The alarms sound and the lights flash\n" \
                "Panic sets in.\n" \
                "You see a door leading SOUTH\n" \
                "---------------------------------------------------"
    if play_game == 'yes':  # if input is YES then start game
        print(issn_welcome, briefing1)
        print(intro_one)
        print("To move state a direction\n"
              "NORTH, SOUTH, EAST, WEST\n"
              "To pick up an item type GET and the item"
              "Other Commands: \nINVENTORY, HELP, STARTOVER, and QUIT")
        game_input()
    elif play_game == 'no':  # if input is NO then quit
        print("GoodBye!")
        quit()
    else:
        print("I don't understand.")
        intro()


def game_input():
    """Takes the user input then converts it to a string***currently set up for when more then one element in user_input
    checks user input to see if it matches any direction, it does it checks it with the available directions in
    current room, if it matches one it directs player to room_to_room where it will initiate the room change
    if it does not match any available directions, it displays that it is not available and sends the user back for
    another input
    If it did not match any directions at all, it then checks to see if the input matches any possible quit options
    if so the game is quit, if not is continues on"""
    print("---------------------------------------------------")
    player_input = input("What do you do?\n>").lower().split()
    for x in player_input:  # Check each word in input for matching words in del_words to delete
        if x in del_words:
            player_input.remove(x)
    user_input = player_input[0]
    if user_input in directions:  # Check to see if input matches any directions
        if user_input in aval_directions.get(current_room[0]):  # Check to see if input matches any avail directions
            room_to_room(user_input)  # if input matches room direction, move to room movement
        else:
            print("You can't go that way!")
            game_input()
    elif user_input in take_action:  # check to see if input matches any take_action
        user_input = player_input[1]
        if user_input in rooms_commands.get(current_room[0]).get('items'):  # check to see if item is in room
            if user_input in inventory:  # check to see if item matches any in inventory
                print("You already have that!")
                game_input()
            elif user_input in item_list:  # check item in item list, them move item from item list to inventory
                inventory.append(user_input)
                item_list.remove(user_input)
                print("You pick up", user_input)
                game_input()
            else:
                print("Something went wrong.")
                game_input()
    elif user_input in player_help:  # check user input for help action
        print("You are in the {}".format(current_room[0]).strip('[]'))
        print("You can go", "{}".format(*aval_directions.get(my_room)).upper().strip('[]'))
        print("\nTo move state a direction:\n"
              "NORTH, SOUTH, EAST, WEST\n"
              "\nTo pick up an item type GET and the item"
              "Other Commands: \nINVENTORY, HELP, STARTOVER, and QUIT")
        game_input()
    elif user_input == "inventory":  # check input for inventory prompt
        if inventory == []:
            print("You have nothing in your inventory")
            print("You have not found:", *item_list[:])
            game_input()
        else:
            print("INVENTORY: ", inventory[:])
            print("You have not found:", *item_list[:])
            game_input()
    elif user_input in player_quit:
        quit()
    elif user_input in player_startover:
        startover()
    else:
        print("I don't understand")
        game_input()


def room_to_room(user_input):
    """a value is first crated to match the current room, then the current room(list[0]) us updated by checking the
    room_commands dictionary. it then gets the value that matches my_room and then gets the value from that that matches
    the user_input form game_input
    It then sends the user to room_dialog with the my_room value"""
    # my_room = current_room[0]
    current_room[0] = rooms_commands.get(current_room[0]).get(user_input)
    room_dialog()


def alien_fight():
    """Determines if the player is ready to fight if yes then moves to fight scene if not it  backs out ot last
    room user was in"""
    user_input = input("Are you ready to fight the alien?\n>")
    if user_input == 'no':
        room = current_room[0]
        current_room[0] = rooms_commands.get(room).get(user_input)
        play()
    elif user_input == 'yes':
        print("time to fight")
        fight_scene()
    else:
        print("I don't understand...")


def room_dialog():
    """Dialog that is output for the current room after room_to_room(), diffrent dialog for before and after item pickup
    after dialog, it then sends player back for the next input"""
    if 'Command Center' == current_room[0]:
        print("You enter the Command Center again.\n"
              "The emergency lights are still blinking and the alarm is still sounding.\n"
              "You don't see anything useful here, the only exit is SOUTH.\n"
              "What do you do?")
        game_input()
    elif 'Med Bay' == current_room[0]:
        if 'medkit' in item_list:
            print("You enter the Med Bay and see medical equipment strewn about the large, sterile room.\n"
                  "You see the MEDKIT on the wall but not much else of use\n"
                  "You see doors leading NORTH, SOUTH, EAST, and WEST")
            game_input()
        else:
            print("You go back into the Med Bay. You still don't see anything of use.\n"
                  "You see doors leading NORTH, SOUTH, EAST, and WEST")
            game_input()
    elif 'Barracks' == current_room[0]:
        if 'armor' in item_list:
            print("You enter the Barracks.\n"
                  "There are bunks lining the walls and you spot a trunk marked ARMOR in front of one.\n"
                  "Nothing else looks useful in here.\n"
                  "You see doors leading NORTH, SOUTH, EAST, and WEST")
            game_input()
        else:
            print("You go back ino the Barracks.\n"
                  "Nothing has changed and nothing looks useful.\n"
                  "You see doors leading NORTH, SOUTH, EAST, and WEST")
            game_input()
    elif 'Provision Hall' == current_room[0]:
        if 'oxygen' in item_list:
            print("You enter the Provision Hall.\n"
                  "You see the OXYGEN tank on a shelf, but nothing else of interest.\n"
                  "You see doors leading SOUTH and EAST")
            game_input()
        else:
            print("You enter the Provision Hall again.\n"
                  "Nothing looks useful.\n"
                  "You see doors leading SOUTH and EAST")
    elif 'Kitchen' == current_room[0]:
        if 'extinguisher' in item_list:
            print("You enter the Kitchen. You see Leroy's foot poking out from behind a counter.\n"
                  "With all the blood, you don't want to look.\n"
                  "You find a fire EXTINGUISHER near one of the doors.\n"
                  "You see doors leading NORTH and EAST")
            game_input()
        else:
            print("You enter the Kitchen again. Avoiding where Leroy lays,\n"
                  "you see nothing has changed and there isn't anything useful here.\n"
                  "You see doors leading NORTH and EAST")
    elif 'Dinning Room' == current_room[0]:
        if 'schematics' in item_list:
            print("You enter the Dinning Room. Tables dotted the room with trays and utinsles.\n"
                  "On one table you see the engine SCHEMATICS that you where going over at lunch the other day.\n"
                  "You don't see anything else of use here.\n"
                  "You see doors leading EAST and WEST")
            game_input()
        else:
            print("You enter the Dinning Room again.\n"
                  "Nothing has changed and you don't see anything useful here.\n"
                  "You see doors leading EAST and WEST")
            game_input()
    elif 'Cryo Dock' == current_room[0]:
        if 'weapon' in item_list:
            print("You enter the Cryo Docks.\n"
                  "Cryo pods with the last of humankind slumbering peacefully inside.\n"
                  "Near the one of the doors where the security officer pods and next to each was an energy WEAPON\n"
                  "You don't see anything else useful here.\n"
                  "You see doors leading SOUTH and WEST")
            game_input()
        else:
            print("You enter the Cryo Docks again.\n"
                  "Nothing has changed and you don't see anything useful.\n"
                  "You see doors leading SOUTH and WEST")
            game_input()
    elif 'Docking Bay' == current_room[0]:
        if 'keycard' in item_list:
            print("You enter the Docking Bay. You see Dr. Yomura near the first-aid cabinet she was restocking.\n"
                  "Next to her you see your KEYCARD. Nothing else looks useful here.\n"
                  "You see doors leading NORTH and WEST")
            game_input()
        else:
            print("You enter the Docking Bay again.\n"
                  "Nothing has changed and you don't see anything useful here.\n"
                  "You see doors leading NORTH and WEST")
            game_input()
    elif 'Equipment Room' == current_room[0]:
        if 'toolkit' in item_list:
            print("You enter the Equipment Room.\n"
                  "You see shelves filled with different pieces of equipment for the ship\n"
                  "and on one shelf you see your TOOLKIT. Nothing else looks useful here.\n"
                  "You see doors leading EAST and WEST")
            game_input()
        else:
            print("You enter the Equipment Room again.\n"
                  "You see shelves filled with different pieces of equipment for the ship\n"
                  "but nothing looks useful\n"
                  "You see doors leading EAST and WEST")
            game_input()
    elif 'Engine Room' == current_room[0]:
        fight_scene()
    else:
        print("Something went wrong!")
        something_wrong = 0
        something_wrong = +1
        if something_wrong == 3:
            print("I'm sorry! Something went very wrong!\n"
                  "RESTARTING GAME")
            startover()
        else:
            game_input()


def fight_scene():
    """Fight scene with final boss in game! Goes through final fight and if player has
    all items, they will win, if not they will lose from the lack of that item"""
    print("You enter the Engine Room and see the horrifying thing ripping into the engines.\n"
          "As the door shuts behind you the alien flings a chung of metal from the engine right to you")
    if "armor" not in inventory:
        print("It tears into your stomach and smacks you into the closed door.\n"
              "You can't go any further. If only you had found some armor!")
        print("YOU LOSE! Try Again?\n"
              "YES or NO")
        yes_or_no()
    else:
        print("It hits you in the stomach and knocks the wind out of you!\n"
              "Thankfully you had armor on or it could have been much worse!\n"
              "---------------------------------------------------\n"
              "But now the Alien has noticed you! It crouches down and lunges at you!")
        if "energy weapon" not in inventory:
            print("You have nothing to defend yourself with and as it grabs you with on clawed hand"
                  "and swallows you whole.\n"
                  "You can't go any further. If only you had found a weapon!")
            yes_or_no()
        else:
            print("You pull out your energy weapon as it opens its mouth wide.\n"
                  "With perfect aim you are able to shoot into its mouth.\n"
                  "It stops startled momentarily before it convulses and you have splattered Alien on your shows.\n"
                  "Energy weapons are powerful, you note as you look at the once Alien on the walls\n"
                  "---------------------------------------------------\n"
                  "You begin to move to the engine to start repairs before it is to late, but as you take\n"
                  "your first step you fall flat on the floor.\n"
                  "You look down to see a pool of blood forming below you.")
            if 'medkit' not in inventory:
                print("You have nothing to stop the bleeding!\n"
                      "You can't go any further. If only you had found some medical supplies!\n")
                yes_or_no()
            else:
                print("You use the medkit to stop the bleeding and fix yourself up the best you can with what you "
                      "have.\n "
                      "You drag yourself back to your feet and over to the engines to see what you can do.\n"
                      "---------------------------------------------------\n"
                      "You notice smoke coming from the engine. As you get closer you begin to cough.")
                if 'oxygen' not in inventory:
                    print("You try to reach the engine through the smoke, but you begin choking and fall to the "
                          "ground.\n "
                          "You can't go any further. If only you had found an oxygen tank!")
                    yes_or_no()
                else:
                    print("You pull out the oxygen tank and begin to breath easier as you make your way to the "
                          "engine.\n "
                          "---------------------------------------------------\n"
                          "You see that the Alien had caused a fire on the engine!")
                    if 'extinguisher' not in inventory:
                        print("You don't have a way to put out the fire! You run franticly back-and-forth until you "
                              "see\n "
                              "a small spark in the fire. You look closer and... BOOM!\n"
                              "You can't go any further. If only you had a way of putting out the fire!")
                        yes_or_no()
                    else:
                        print("You take out the fire extinguisher and quickly put out the flames."
                              "---------------------------------------------------\n"
                              "You begin to look at the damage.")
                        if 'keycard' not in inventory:
                            print("You go to open the engineering panel but realize that you don't have your keycard!\n"
                                  "You try to pry open the panel. As you try to open it an alarm sounds.\n"
                                  "You try to ignore the alarms and open the engine to save the ship, until...\n"
                                  "ZAP!\n"
                                  "The  internal engine defense systems had come back online since the fire cleared."
                                  "You can not go any further. If only you had found your keycard!\n")
                            yes_or_no()
                        else:
                            print("You scan your keycard to get into the engineering panel.\n"
                                  "---------------------------------------------------\n"
                                  "You see extensive damage and it is hard to make out what everything is.")
                            if 'engine plans' not in inventory:
                                print("You start with what is closest to you and reach in..."
                                      "ZAP! You have been electricuted!\n"
                                      "Everything shifted so much you didn't see the wires had moved behind the panel\n"
                                      "You can not go any further. If only you had found the engine plans!")
                                yes_or_no()
                            else:
                                print("You pull out the engine plans. Going through the blueprints you can see how "
                                      "much everything has shifted.\n "
                                      "With this you are able to move a few components into there more appropriate "
                                      "spots but there is still extensive damage.\n"
                                      "---------------------------------------------------")
                                if 'toolkit' not in inventory:
                                    print("You try to make the repairs with your bare hands, as you have no other "
                                          "choice and the clock is ticking for the cryo pods!\n "
                                          "You are making progress until you feel you hand touch something that "
                                          "wasn't suppose to be there.\n "
                                          "You try to back peddle your hand movements but...\n"
                                          "BOOM! The engine explodes and you along with it.\n"
                                          "You can not go any further. If only you had found your toolkit!")
                                    yes_or_no()
                                else:
                                    print("You use the items in your toolkit to quickly do the most pressing "
                                          "emergency repairs to keep things working while you do more extensive "
                                          "repairs later.\n "
                                          "---------------------------------------------------\n"
                                          "You wipe your brow as you realize the emergency has passed.\n")
                                    print("YOU WIN! Try Again?\n"
                                          "YES or NO")
                                    win_input = input(">").lower()
                                    if win_input == 'yes':
                                        startover()
                                    elif win_input == 'no':
                                        print("GoodBye!")
                                        quit()
                                    else:
                                        print("I don't understand.")
                                        yes_or_no()


def startover():
    """Starts over the game from the beginning. Removes all items from inventory and puts it back in item list
    then makes the starting room the command center again."""
    while len(inventory) > 0:
        for x in inventory:
            item_list.append(x)
            inventory.remove(x)
            current_room[0] = "Command Center"
    intro()


def yes_or_no():
    """Yes or No prompt from fight scene on whether or not to play again."""
    print("YOU LOSE! Try Again?\n"
          "YES or NO")
    lose_input = input(">").lower()
    if lose_input == 'yes':
        startover()
    elif lose_input == 'no':
        print("GoodBye!")
        quit()
    else:
        print("I don't understand.")
        yes_or_no()


def play():
    """Takes player back to previous room if is not ready to fight final boss"""
    while 'engine_room' != current_room[0]:
        room_to_room(my_room)
    alien_fight()


# lists and dictionaries involving the current room and directions
current_room = ["Command Center"]
my_room = current_room[0]
directions = ("north", "south", "east", "west")
# lists of commands relevent to game_input()
take_action = ["get", "take", "grab", 'pickup']
del_words = ["go", "move", "to", "the", "do", "fire", "energy", "plans", 'engine']
player_quit = ["quit", "stop", "end"]
player_startover = ["startover", "tryagain"]
player_help = ["help", "helpme", "directions"]
# lists involving item pickup
item_list = ["medkit", "armor", "schematics", "extinguisher", "oxygen",
             "toolkit", "weapon", "keycard"]
inventory = []

intro()  # starts games
