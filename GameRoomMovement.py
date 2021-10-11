#Dictionary with avalable directions in current room
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
#Dictionary with the rooms commands for the current room; what direction leads where, what items origanally in room
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
    #The intro of the game with the inital prompts
    print("You can type a ditection: NORTH, SOUTH, EAST, or WEST\n"
          "Or type QUIT")
    print("Start of game.\n"
          "In Command Center.\n"
          "You can only go SOUTH")
    game_input()

def room_dialog(my_room):
    """Dialog that is output for the current room after room_to_room(),
    after dialog, it then sends player back for the next input"""
    if 'command_center' == current_room[0]:
        print("You enter the Command Center again.\n"
              "The emergency lights are still blinking and the alarm is still sounding.\n"
              "You don't see anything useful here, the only exit is SOUTH.\n"
              "What do you do?")
        game_input()
    elif 'med_bay' == current_room[0]:
        print("You enter the Med Bay and see medical equipment strewn about the large, starile room.\n"
                  "You doors leading NORTH, SOUTH, EAST, and WEST")
        game_input()
    elif 'barracks' == current_room[0]:
        print("In barracks-armor NOT picked up\n"
              "You see doors leading NORTH, SOUTH, EAST, and WEST")
        game_input()
    elif 'provisions' == current_room[0]:
        print("in provisions before O2 pick up\n"
            "You doors leading SOUTH and EAST")
        game_input()
    elif 'kitchen' == current_room[0]:
        print("in kitchen before LEROY\n"
            "You doors leading NORTH, and EAST")
        game_input()
    elif 'dinning_room' == current_room[0]:
        print("in dinning hall before engine plans pick up\n"
            "You doors leading EAST and WEST")
        game_input()
    elif 'cryo_dock' == current_room[0]:
        print("in cryo befor weapon pick up\n"
            "You doors leading SOUTH and WEST")
        game_input()
    elif 'docking_bay' == current_room[0]:
        print("in docking bay before keycard pick up\n"
            "You doors leading NORTH and WEST")
        game_input()
    elif 'equipment_room' == current_room[0]:
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

def game_input():
    """Takes the user input then convers it to a string***currently set up for when more then one element in user_input
    checks user input to see if it matches any direction, it does it checks it with the available directions in
    current room, if it matches one it directs player to room_to_room where it will initiate the room change
    if it does not match any available directions, it displays that it is not available and sends the user back for
    another input
    If it did not match any directions at all, it then checks to see if the input matches any possible quit options
    if so the game is quit, if not is continues on"""
    user_input = input("What do you do?\n>").lower().split()
    user_input = user_input[0]
    print(user_input)
    if user_input in directions:
        print(user_input)
        if user_input in aval_directions.get(current_room[0]):
            room_to_room(user_input)
        else:
            print("You can't go that way!")
            game_input()
    if user_input in player_quit:
        quit()
    else:
            print("I don't understand")
    #FIXME: this is where the poroblem APPEARS to be

def room_to_room(user_input):
    """a value is first crated to match the current room, then the current room(list[0]) us updated by checking the
    room_commands dictionary. it then gets the value that matches my_room and then gets the value from that that matches
    the user_input form game_input
    It then sends the user to room_dialog with the my_room value"""
    my_room = current_room[0]
    current_room[0] = room_commands.get(my_room).get(user_input)
    room_dialog(my_room)

current_room = ["command_center"]
my_room = current_room[0]
directions = ("north", "south", "east", "west")
del_words = ["go", "move", "to", "the", "do"]
player_quit = ["quit", "stop", "end"]


intro()