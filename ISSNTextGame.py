#CURRENTLY THE DIRECTIONS AND PICKUP FUNCTINS WORK CORRECTLY!!!
#COPY BEFORE EDITTING!!!
aval_directions = {
    'command_center': {
        'south'
    },
    'med_bay': {
        'north', 'south', 'east', 'west'
    },
    'barracks': {
        'north', 'south', 'east', 'west'
    },
    'provisions': {
        'south', 'east'
    },
    'kitchen': {
        'north', 'east'
    },
    'dinning_hall': {
        'east', 'west'
    },
    'cryo_dock': {
        'south', 'west'
    },
    'docking_bay': {
        'north', 'west'
    },
    'equipment_room': {
        'east', 'west'
    }}

room_commands = {
    'command_center':
        dict(south='med_bay', items='none'),
    'med_bay':
        dict(north='command_center', south='barracks', east='cryo_dock', west='provisions', items='medkit'),
    'barracks':
        dict(north='med_bay', south='engine_room', east='equipment_room', west='dinning_hall',
             items='armor'),
    'dinning_hall':
        dict(east='barracks', west='kitchen', items='engine plans'),
    'kitchen':
        dict(north='provisions', east='dinning_hall', items='leroy'),
    'provisions':
        dict(south='kitchen', east='med_bay', items='oxygen'),
    'equipment_room':
        dict(east='docking_bay', west='barracks', items='toolkit'),
    'cryo_dock':
        dict(south='docking_bay', west='med_bay', items='energy weapon'),
    'docking_bay':
        dict(north='cryo_dock', west='equipment_room', items='keycard'),
    'engine_room':
        dict(no='barracks')
}

def intro():
    issn_welcome = "\nWelcome to the International Starship Nova!\nAlso known as the ISSN.\n"
    breifing1 = "\nYou have been chosen for a maintnaince shift as you " \
                "where briefed on prior to launch.\nAs your contract stated it " \
                "will be a 2 week shift to help maintain various " \
                "parts of the ship.\nYou have been chosen based on your " \
                "skill set and passenger number.\n"
    print(issn_welcome, breifing1)
    intro_one = "It has been a week sence you woke up on the ISSN, along with your fellow crewmates \n" \
                "Dr. Suki Yomura and Leroy Hinks. \n" \
                "It has been calm as you worked on the general maitnence of the ship, \n" \
                "Dr. Yomura tended to your fellow shipmates \n" \
                "currently in cryo, and Hinks tended to the BioDome as well as the \n" \
                "embryoes of future husbandry animals.\n" \
                "Together with your current maintnece team as well as the past and future teams, \n" \
                "you know you will all make it to Alfa Centari.\n" \
                "You have been doing some rutien sensor maitnence in the command center when-\n" \
                "BEEP--BEEP--BEEP--BEEP--BEEP--\n" \
                "The alarms sound and the lights flash\n" \
                "Panic sets in."
    print(intro_one)
    game_input()
#FIXME: item_pickup not reacting correctly find bug and fix!!!
def item_pickup(player_input):
    print(room_commands.get(current_room[0]).get('items'))
    if (x in player_input for x in item_list) and (player_input == room_commands.get(current_room[0]).get('items')):
        if player_input != any(inventory):
            inventory.append(player_input)
            item_list.remove(player_input)
            print("Inventory: ", inventory, "Item list:", item_list)
            game_input()
        else:
            print("You don't see that")
            game_input()
    elif player_input == any(inventory):
        print("Inentory:", inventory, "itemlist:", item_list)
        print("You already have that!")
        game_input()
    else:
        print("You don't see that")
        game_input()

def room_dialog(my_room):
    if 'command_center' == current_room[0]:
        print("You enter the Command Center again.\n"
              "The emergency lights are still blinking and the alarm is still sounding.\n"
              "You don't see anything useful here, the only exit is SOUTH.\n"
              "What do you do?")
        game_input()
    elif 'med_bay' == current_room[0]:
        if 'medkit' == any(inventory):
            print("You enter the Med Bay once again.\n"
                  "Nothing has changed and you don't see anything else of use.\n"
                  "You see doors leading NORTH, SOUTH, EAST, and WEST")
            game_input()
        else:
            print("You enter the Med Bay and see medical equipment strewn about the large, starile room.\n"
                  "You notice a MEDKIT still on the wall by the door. That will come in usefull!\n"
                  "You look around but everything else is either broken or unrecognizable to you.\n"
                  "You doors leading NORTH, SOUTH, EAST, and WEST")
            game_input()
    elif 'barracks' == current_room[0]:
        if 'armor' == any(inventory):
            print("In barracks after armor pickup\n"
                  "You doors leading NORTH, SOUTH, EAST, and WEST")
            game_input()
        else:
            print("In barracks-armor NOT picked up\n")
            game_input()
    elif 'provisions' == current_room[0]:
        if 'oxygen' == any(inventory):
            print("In provisions after O2 pick up\n"
            "You doors leading SOUTH and EAST")
            game_input()
        else:
            print("in provisions before O2 pick up\n"
            "You doors leading SOUTH and EAST")
            game_input()
    elif 'kitchen' == current_room[0]:
        if 'leroy'== any(inventory):
            print("in kitchen after LEROY\n"
            "You doors leading NORTH and EAST")
            game_input()
        else:
            print("in kitchen before LEROY\n"
            "You doors leading NORTH, and EAST")
            game_input()
    elif 'dinning_room' == current_room[0]:
        if 'engine plans' == any(inventory):
            print("in dinning room after engine plans pick up\n"
            "You doors leading EAST and WEST")
            game_input()
        else:
            print("in dinning hall before engine plans pick up\n"
            "You doors leading EAST and WEST")
            game_input()
    elif 'cryo_dock' == current_room[0]:
        if 'energy weapon' == any(inventory):
            print("in cryo after weapon pick up\n"
            "You doors leading SOUTH and WEST")
            game_input()
        else:
            print("in cryo befor weapon pick up\n"
            "You doors leading SOUTH and WEST")
            game_input()
    elif 'docking_bay' == current_room[0]:
        if 'keycard' == any(inventory):
            print("in docking bay after keycard pick up\n"
            "You doors leading NORTH and WEST")
            game_input()
        else:
            print("in docking bay before keycard pick up\n"
            "You doors leading NORTH and WEST")
            game_input()
    elif 'equipment_room' == current_room[0]:
        if 'toolkit' == any(inventory):
            print("in equipment room after toolkit pick up\n"
            "You doors leading EAST, and WEST")
            game_input()
        else:
            print("in equipment room before toolkit pick up\n"
            "You doors leading EAST, and WEST")
            game_input()
    elif 'engine_room' == current_room[0]:
        fight_scene()
    else:
        print("Something went wrong!")
        something_wrong = 0
        something_wrong =+1
        if something_wrong == 3:
            print("I'm sorry! Something went very wrong!\n"
                  "RESTARTING GAME")
            startover()
        else:
           game_input()
#FIXME: INPUT to seperate what actin to take
def game_input():
    user_input = input(">").lower().split()
    if 'the' == any(user_input):
        user_input.remove('the')
    elif 'to' == any(user_input):
        user_input.remove('to')
    elif 'do' == any(user_input) or 'i' == any(user_input):
        user_input.remove('do')
        user_input.remove('i')
    else:
        pass
    if len(user_input) == 1:
        user_input = user_input[0]
        if (x in user_input for x in directions):
            if (x in user_input for x in get_directions):
                room_to_room(user_input)
            else:
                print("You can't go that way!")
                game_input()
        elif (x in user_input for x in player_help):
            help_menu()
        elif (x in user_input for x in start_over):
            startover()
        elif user_input == "quit":
            quit()
        else:
            print("I don't understand")
    elif len(user_input) == 2 or len(user_input) == 3:
        player_action = []
        player_action.append(user_input[0])
        print(user_input)
        if len(user_input) == 3:
            user_input[1] = user_input[1] + user_input[2]
        elif len(user_input) == 2:
            user_input[1] = user_input[1]
        else:
            game_input()
    #FIXME: this is where the poroblem APPEARS to be
    if any(take_action) == user_input[0]:
        print("WRONG")
        user_input = user_input[1]
        item_pickup(user_input)
    elif (x in user_input[0] for x in move_action):
        print(user_input)
        user_input = user_input[1]
        room_to_room(user_input)
    else:
        print("ttestt")
    #else:
        #print("I don't understand")

def room_to_room(user_input):
    my_room = current_room[0]
    current_room[0] = room_commands.get(my_room).get(user_input)
    print(current_room[0])
    room_dialog(my_room)


#def help_menu()
#def startover()
current_room = ["command_center"]
my_room = current_room[0]
directions = ("north", "south", "east", "west")
item_list = ["medkit", "armor", "engine plans", "leroy", "oxygen",
             "toolkit", "energy weapon", "keycard"]
inventory = []
take_action = ["get", "take", "grab"]
move_action = ["go" , "move" , "look"]
player_help = ["help", "helpme", "what", "whattake" , "helpmenu", "inventory", "items"]
start_over =["startover", "tryagain", "retry", "doover", "mulligan"]
get_directions = list(aval_directions.get(my_room))

intro()
