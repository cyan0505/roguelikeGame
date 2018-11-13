import character
import random


POTIONS = ["Apple", "Cake", "Bread", "Meat", "Health Potion"]
WEAPONS = ["Iron Sword", "Stick", "Wooden Sword"]
ARTIFACTS = ["Boat", "Minotaur key", "Dragon key", "Sword of a Thousand Truths"]


def load_inventory():
    """
    Converts csv file into dictionary and returns it

    Returns:
        inventory: Dictionary representing players equipment
    """

    inventory = dict()
    with open("player_inventory.csv", "r") as items:
        items = items.readline().split(",")

    name = 0
    type_ = 1
    quantity = 2

    for item in items:
        item = item.split("_")
        inventory[item[name]] = [item[type_], int(item[quantity])]

    return inventory


def save_inventory(inventory):
    """
    Function used to save current inventory (dict) to a csv file

    Args:
        inventory: dictionary with structure: {"Name": (type, quantity)}
    """

    to_save_table = []
    type_ = 0
    quantity = 1

    for item in inventory:
        if inventory[item][quantity] >= 1:
            to_save_table.append("_".join([item, inventory[item][type_], str(inventory[item][quantity])]))

    with open("player_inventory.csv", "w") as save_file:
        save_file.write(",".join(to_save_table))


def add_to_inventory(items):
    """
    Function used to add new items to inventory

    Args:
        items: list of items to add
    """

    quantity = 1

    inventory = load_inventory()

    for item in items:
        if item in inventory:
            inventory[item][quantity] += 1

        else:
            type_ = check_items_type(item)
            inventory[item] = [type_, 1]

    save_inventory(inventory)


def add_to_inventory_random_item():
    """
    Function used to choose random item, and add it to inventory
    """

    list_of_items = POTIONS[:]
    list_of_items.extend(WEAPONS)
    item = random.choice(list_of_items)
    add_to_inventory([item])

    print("You have picked up a/an", item + "!")
    input("Press ENTER to continue...")


def check_items_type(item):
    """
    Function checks type of item

    Args:
        item: name of item to check

    Returns:
        type (string) of an item
    """

    if item in POTIONS:
        return "POTION"

    elif item in WEAPONS:
        return "WEAPON"

    elif item in ARTIFACTS:
        return "ARTIFACT"

    else:
        return "UNKNOWN"


def check_item_healing(item):
    """
    Function used to check how much HP item will restore

    Args:
        item: name of item to check

    Returns:
        integer- how much hp will be restored
    """

    item = item.upper()

    if item == "APPLE":
        return 5

    elif item == "BREAD":
        return 10

    elif item == "CAKE":
        return 15

    elif item == "MEAT":
        return 25

    else:
        return 50


def check_weapon_damage(weapon):
    """
    Function used to check how much damage weapon will deal

    Args:
        weapon: name of weapon to check

    Returns:
        integer- how much damage will be dealt
    """

    weapon = weapon.upper()

    if weapon == "STICK":
        return 0

    elif weapon == "WOODEN SWORD":
        return 5

    elif weapon == "IRON SWORD":
        return 10

    else:
        return 9001


def use_item():
    """
    Function manages item usage

    Returns:
        healed_hp: integer representing total hp restored
    """

    inventory = load_inventory()
    usable_items = set()   # items in inventory

    for item in inventory:
        if "POTION" in inventory[item]:
            usable_items.add(item.upper())

    ordered = dict()
    for i, item in enumerate(usable_items):
        print(str(i+1) + ".", item, "heals for", check_item_healing(item), "HP")
        ordered[str(i+1)] = item
    print("0. Abort")

    choice = input("Type in number of item you want to use and press ENTER! ")
    while choice not in ordered and choice != "0":
        choice = input("Type in a valid number! ")

    if choice == "0":
        return 0

    else:
        choice = ordered[choice]    # Switches number to item name
        return use_chosen_from_inventory(choice)


def use_chosen_from_inventory(choice):
    # Load current HP and inventory
    player_stats = character.get_stats()
    missing_hp = (player_stats["Endurance"] * 15) - player_stats["HP"]
    inventory = load_inventory()

    # Checks healing (you can not have more HP that maxHP)
    item_healing = check_item_healing(choice)
    healed_hp = min([missing_hp, item_healing])

    # Updates stats and inventory
    character.change_hp(healed_hp)

    quantity_index = 1
    inventory[choice.title()][quantity_index] -= 1
    save_inventory(inventory)

    return healed_hp


def change_weapon():
    """
    Function used to manage weaponry
    """

    inventory = load_inventory()
    weapons = set()   # weapons in inventory

    for item in inventory:
        if "WEAPON" in inventory[item]:
            weapons.add(item.upper())

    for item in weapons:
        print(item, "increases your damage by",  check_weapon_damage(item), "!")

    choice = input("Type in name of item you want to use!")

    if choice.upper() in weapons:
        swap_weapons(choice, inventory)
    else:
        print("There's no such weapon in your inventory!")


def swap_weapons(choice, inventory):
    """
    Function swaps weapons- one in inventory and one in players "hand"

    Args:
        choice: weapon choosed to equip
        inventory: current players inventory
    """

    quantity_i = 1

    player_stats = character.get_stats()
    player_weapon = player_stats["Weapon"]

    inventory[choice.title()][quantity_i] -= 1
    save_inventory(inventory)
    add_to_inventory([player_weapon])

    player_stats["Weapon"] = choice.title()
    character.save_stats(player_stats)


def show_inventory():
    """
    Function used to print out inventory
    """
    inventory = load_inventory()

    type_index = 0
    quantity_index = 1

    for item in inventory:
        print(item, inventory[item][type_index], inventory[item][quantity_index])

    input("\nPress ENTER to continue ")


def item_in_inventory(item):
    """
    Function used to check if "Sword of a Thousand Truths" is in inventory

    Returns boolean
    """

    inventory = load_inventory()
    print("item in inv", item in inventory)
    return item in inventory


if __name__ == "__main__":
    add_to_inventory(["Meat", "Cake", "Iron Sword", "Boat"])
    use_item()
