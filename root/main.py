current_room = "Wreckers base"
game_over = False
has_key = False
has_portal_code = False
venice_visits = 0
wrong_codes = 0
moves = 0
visited = []


def get_valid_choice(prompt: str, valid_options: list[str]) -> str:
    # Basically, whatever room you are located in, you ar given two options, and you can only type one of them, anything else is NOT accepted.
    # Global
    while True:
        choice = input(prompt)
        if choice in valid_options:
            return choice
        print("Not Correct. Please type one of the following,f:", ", ".join(valid_options))


def wreckers_base() -> None:
    #Escape the Wreckers base or fight them.
    global current_room, game_over
    choice = get_valid_choice("Do you want to 'escape from base' or 'Fight the Wreckers':",["escape from base", "Fight the Wreckers"],)
    if choice == "escape from base":
        print("You have escaped the wreckers base, where do we go now?")
        current_room = "Escape"
    else:
        print("You try escaping but get caught, game over.")
        game_over = True


def escape() -> None:
    # When you choose to escape the base, you go past the control room and get a glimpse of the portal code, you can decide whether dart should scan it or ignore it.
    global current_room, has_portal_code
    print("You and Agam escape the Wreckers' base. As you rush through the control room, you notice a strange sequence of symbols flashing on a computer screen.")
    choice = get_valid_choice("Do you want to 'scan' the sequence of symbols or 'ignore' them so you can escape faster? ",["scan", "ignore"],)
    if choice == "scan":
        print("Dart scans the the portal code using his sensors and saves the portal code to his memory.")
        print("The code on the screen reads: 09156767")
        has_portal_code = True
    else:
        print("You ignore the symbols and continue escaping. You might need that code later.")
    print("Your next stop is Venice.")
    current_room = "Venice"


def venice() -> None:
    # You can split to two pathways, either go to a local shop to buy a boat or go to the rooftop for higher ground and look for Wreckers, the choice is yours.
    global current_room, venice_visits
    if venice_visits == 0:
        prompt = "You have arrived in Venice. It is nighttime, and you see a beautiful town in the distance. Do you want to explore the 'rooftop' or travel through the canals by 'boat'? "
    else:
        prompt = "You are back in Venice. The streets feel quieter than before. Do you want to explore the 'rooftop' or travel through the canals by 'boat'? "
    venice_visits += 1
    choice = get_valid_choice(prompt, ["rooftop", "boat"])
    if choice == "rooftop":
        print("You have chosen rooftop. You make your way through the village, trying your best not to wake or disturb any of the locals. You spot a building and make your way to the rooftop.")
        current_room = "Rooftop"
    else:
        print("Ozan and Agam go to the local market while Dart stays back and keeps looking for clues. You guys buy a boat to explore the canals further.")
        current_room = "Boat"


def boat() -> None:
    # After the journey on the boat, you make it to the train station where you can make another decision.
    global current_room
    print("You and Agam call Dart over from his hiding spot and indicate that everything is set up and we can start our search through the canals. After an hour, you see ripples in the water and follow its path to a nearby Train Station. ")
    current_room = "Train Station"


def rooftop() -> None:
    # Sadly, the rooftop leads to the group getitng ambushed, game over.
    global current_room
    print("The group looks in all directions while standing at the rooftop, Dart uses his special sensors and tries to pinpoint the location of the Wreckers. The building starts shaking, and dart investigates where it came from.")
    current_room = "Wrecker Ambush"


def wrecker_ambush() -> None:
    # prints the action scene of how the group is defeated.
    global game_over
    print("Wreckers emerge from the darkness, knocking Dart off the building and leaving you and Agam vulnerable. You try and escape by going through the door, but its too late and the Wreckers capture you. YOU LOSE")
    game_over = True

def train_station() -> None:
    # you can again split into two pathways, either investigate the platform or head off to Paris via train.
    global current_room, game_over, has_key
    choice = get_valid_choice("You arrive at the train station and see chunks of metal laying around on the platform, the train that is going to Paris arrives in 5 minutes, do you want to hop onto the 'train' or 'investigate' further?",
    ["train", "investigate"],)

    if choice == "train":
        print("The three of you make your way onto the train and head for Paris. Just as the train is about to leave, a shiny object catches your eye near your seat. It's an Aztec key!")
        key_choice = get_valid_choice("Do you want to 'pick up key' or 'leave key'? ",
        ["pick up key", "leave key"],)
        if key_choice == "pick up key":
            has_key = True
            print("You pick up the Aztec key and put it in your back pocket.")
        else:
            print("You leave the key behind on the platform.")
        current_room = "Paris"
    else:
        print("The three of you pick up a trail and continue seeing cwhunks of metal until you reach a hideout spot. Dart is the first one to realize this was a trap and urges you to run. However, it is too late and Wreckers jump from behind and capture you. YOU LOSE.")
        game_over = True

def paris() -> None:
    # You can continue to the Eiffel Tower or go back to venice. one of the variables counts how many times you went to Venice, and displays it at the end of the adventure.
    global current_room
    print("The three of you arrive in Paris and the atmosphere immediately switches, the sun is rising but the village isn't thriving. You look at the eiffel tower and it looks extremely dull. Dart uses his built in lenses to figure out that Wreckers are at the eiffel tower, and they have a device that is is going to cause a ripple in the sky, which creates a portal to access their home dimension.")
    print("Do you want to go to 'Eiffel tower' or return to 'venice'.")
    choice = get_valid_choice("Choose one of the options: ", ["Eiffel tower", "venice"])
    if choice == "Eiffel tower":
        current_room = "Eiffel Tower"
    else:
        current_room = "Venice"

def eiffel_tower() -> None:
    # Dart uses his sensors once again and spots wreckers on the top floor with a device. They need to make a plan before havoc breaks loose.
    global current_room
    print("You rush thorough the quiet streets and make your way to the base of the eiffel tower. Dart figures out a way to get to the top floor, and you follow his plan. As your reaching the top floor, you locate the portal generator and need to figure out a way to destroy it, before havoc breaks lose.")
    current_room = "Final battle"

def enter_code() -> bool:
    # I made a function here where you need to type the code you scanned after escaping the Wrecker's base. If you type the right code (which is 09156767), it stops and returns true (meaning you win the game). You have three tries before the loop ends and returns to false (meaning you lose the game).
    global wrong_codes
    while wrong_codes < 3:
        code = input("Type the correct portal code to attempt and overload the generator: ")
        if code == "09156767":
            return True
        wrong_codes += 1
        print("Wrong code! please try again,  attempts used:", wrong_codes, "of 3")
    return False

def final_battle() -> None:
    # This is the last pathway in the adventure game where you can decide to attack head on, disable the generator using the key (found at the trains station), or use the portal code you got when escaping from the Wrecker's base.
    global game_over
    choice = get_valid_choice("You develop three plans but cannot decide which one to execute. You can either 'attack', 'disable generator', or 'overload generator'? ",
        ["attack", "disable generator", "overload generator"],)
    game_over = True
    if choice == "attack":
        print("You slowly creep up to the entrance and attack the first couple of body guards, Dart has no problem taking them out. Suddenly, dozens of alarms start blaring which alerts all of the Wreckers and the three of you need to find a space to hide. However, it is too late and the wreckers defeat Dart and knock you unconscious. YOU LOSE.")
    elif choice == "disable generator":
        if has_key:
            print("Dart distracts the Wreckers while you and Agam try and to disable the generator. Luckily you picked up Aztec key and your able to access the generators main hub which is where you can shut down the device. A wrecker comes sprinting towards you but just in time you confirm the option to disable the generator and the portal closes.")
            print("YOU WIN! The portal has been shut down, the ripples in the sky slowly fade away and the atmosphere changes.")
        else:
            print("You need the Aztec key to disable the generator!")
            print("The Wreckers catch you before you can shut down the generator. YOU LOSE.")
    else:
        if has_portal_code and enter_code():
            print("You and Agam use the portal code to overload the generator. It immediately shuts off, the ripples in the sky shrink and the portal collapses. YOU WIN!")
        elif has_portal_code:
            print("Too many wrong codes. The Wreckers defeat you. YOU LOSE.")
        else:
            print("You don't have the portal code. The generator becomes unstable and the Wreckers defeat you. YOU LOSE.")

# The way the final battle works is the get_valid_choice keeps asking the player to either type (attack, disable generator, or overload generator).
# Each game_over = True comes right away. This is because each option ends up with you winning or losing. This is set before the "if" inside each branch, and when the function is complete, the main loop comes to a stop.
# when you attack you lose, with the disable generator option, if you picked up the key from the train station you win. so if you have the key, has_key = True.
#Overload generator is the last option where you need to type in the portal code you got from the "current_room = escape". If you have the portal code is with the variable has_portal_code and enter_code():, this means you need the code and have to type it correctly. If it's False, then the program would skip this and won't ask you to type anything. If it's True, you need to type the correct code in-order to win.
def main() -> None:
    #This basically runs the whole game, it checks which room your in currently and also runs the room's function. It progresses as you go through the game.
    # "visited.append(current_room)" means to add the rooms name to the list every time we go to a new round, so it keeps track of it prints the result at the end.

    global moves
    while not game_over:
        visited.append(current_room)
        if current_room == "Wreckers base":
            wreckers_base()
        elif current_room == "Escape":
            escape()
        elif current_room == "Venice":
            venice()
        elif current_room == "Boat":
            boat()
        elif current_room == "Rooftop":
            rooftop()
        elif current_room == "Wrecker Ambush":
            wrecker_ambush()
        elif current_room == "Train Station":
            train_station()
        elif current_room == "Paris":
            paris()
        elif current_room == "Eiffel Tower":
            eiffel_tower()
        elif current_room == "Final battle":
            final_battle()
        moves += 1
    print("Total moves you made:", moves)
    print("Rooms visited in the game:", ", ".join(visited))


main()
#"join(visited))" basically gets the room names, and combines them into one pieces of text, with commas inbetween.
