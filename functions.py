import os
import sys
import maps
import character
import inventory
import combat


def getch():
    """
    Function takes user input
    Returns:
        ch: key pressed by user (letters and digits only)
    """

    import tty
    import termios

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch


def is_barrier(map_, y, x):
    """
    Function checks if player move is possible
    Args:
        map_: table representing background
        y: y coordinate of player to check
        x: x coordinate of player to check
    Returns:
        string, 'barrier', 'npc' or 'no'
    """

    if y == -1 or y == len(map_) or x == -1 or x == len(map_[0]):
        return "barrier"
    elif map_[y][x] in maps.FORBIDDEN_TO_MOVE:
        return "barrier"
    elif map_[y][x] == maps.WATER:
        if inventory.item_in_inventory("Boat"):
            return "no"
        else:
            return "barrier"
    elif map_[y][x] in maps.NPC:
        return "npc"
    else:
        return "no"


def player_interaction(item_to_interact, level):
    """
    Function calls functions of player interaction
    Args:
        item_to_interact: char, item to interact with
        level: int, level of game
    Returns:
        is_item_to_hide: boolean, 'True' if item have to be hide after interaction 
    """

    if item_to_interact == maps.ENEMIES[0]:
        is_item_to_hide = combat.combat_in_level(level)

    elif item_to_interact == maps.ENEMIES[1]:
        is_item_to_hide = combat.combat_in_level(level + 1)

    elif item_to_interact == maps.BOSS:   # Boss
        is_item_to_hide = combat.combat_in_level(5)

    elif item_to_interact in maps.ITEMS:
        inventory.add_to_inventory_random_item()
        is_item_to_hide = True

    elif item_to_interact == maps.SHOP:
        speak_with_merchant()
        is_item_to_hide = False

    elif item_to_interact == maps.SAILOR:
        speak_with_sailor()
        is_item_to_hide = False

    return is_item_to_hide


def player_move(map_, level, player):
    """
    Function moves player in requested direction if possible or interact with inventory
    Args:
        map_: table representing background
        level: int, level of game
        player: list containing players coordinates [y, x]
    Returns:
        player: list containing new players coordinates [y, x]
    """

    move = getch()
    move = move.lower()

    next_move_y = player[0]
    next_move_x = player[1]

    if move == "s":
        next_move_y += 1
    elif move == "w":
        next_move_y -= 1
    elif move == "a":
        next_move_x -= 1
    elif move == "d":
        next_move_x += 1
    elif move == "i":
        inventory.show_inventory()
    elif move == "u":
        inventory.use_item()
    elif move == "y":
        inventory.change_weapon()
    elif move == "0":
        sys.exit("Exit")

    barrier = is_barrier(map_, next_move_y, next_move_x)

    if barrier == "npc":
        if player_interaction(map_[next_move_y][next_move_x], level):
            maps_ = maps.paste_grass(map_, next_move_y, next_move_x)

    elif barrier == "no":
        player[0] = next_move_y
        player[1] = next_move_x

    return player


def is_next_level(level, player):
    """
    Function checks if level have to be changed
    Args:
        level: int, level of game
        player: list containing players coordinates [y, x]
    Returns:
        boolean, 'True' if level have to be increment
    """

    if level == 1 and player == maps.MAPS[0]["portal"]:
        return True
    elif level == 2 and player == maps.MAPS[1]["portal"]:
        return True
    else:
        return False


def speak_with_merchant():
    """
    Function manages shops- Allows player to buy items
    """
    os.system("clear")
    player = character.get_stats()

    print("Hello there traveler! Do you want to buy an item?")
    shop = merchant_items()

    name_i = 0
    price_i = 1

    for item in sorted(shop):
        print(item + ".", shop[item][name_i] + " - " + str(shop[item][price_i]), "Heals for " +
              str(inventory.check_item_healing(shop[item][name_i])))

    print("\nYour gold:", str(player["Gold"]))

    choosen_item = input("Type in number of item you want to buy, or choose '0' leave. Press ENTER to confirm. ")
    while choosen_item not in shop and choosen_item != "0":
        choosen_item = input("Type in a valid number! ")

    if choosen_item == "0":
        print("OK. Bye!")

    else:
        if shop[choosen_item][price_i] > player["Gold"]:
            print("You do not have enough money!")

        else:
            inventory.add_to_inventory([shop[choosen_item][name_i]])
            character.change_exp_and_gold(0, int(-shop[choosen_item][price_i]))
            print("Here you go!")

    input("Press ENTER to continue ")


def merchant_items():
    """
    Function creates merchant items
    Returns:
        shop: Dictionary representing merchants items
    """

    shop = dict()
    shop["1"] = ("Apple", 5)
    shop["2"] = ("Bread", 9)
    shop["3"] = ("Cake", 12)
    shop["4"] = ("Meat", 20)
    shop["5"] = ("Health Potion", 30)

    return shop


def speak_with_sailor():
    """
    Function handles interaction with sailor
    """
    print("*Crazy sailor looks at you and asks*")
    print("Do you know da wae?")
    answer = input("Your answer: ").upper()
    if answer == "UM":
        print("She is QUEEN")
        print("*CLICKING SOUND*")
        inventory.add_to_inventory(["Boat"])
    
    else:
        print("SHE DOES NOT KNOW DA WAE SPIT ON HER SPIT MY BROTHAS")

    input("Press ENTER to continue...")

