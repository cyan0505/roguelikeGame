""" Module handling players stats """

import functions
import inventory
import time
import os
import copy


def create_character():
    """
    Function used to create new character
    """

    skill_points = 10
    stats = {"Strength": 5, "Agility": 5, "Endurance": 5, "Experience": 0, "Gold": 0}
    created = False

    while not created:
        os.system("clear")
        handle_stat_management()
        current_stats(stats)
        print("Skill points:", skill_points)

        choice = functions.getch().lower()

        if choice == "s" and skill_points > 0:
            skill_points -= 1
            stats["Strength"] += 1

        elif choice == "a" and skill_points > 0:
            skill_points -= 1
            stats["Agility"] += 1

        elif choice == "e" and skill_points > 0:
            skill_points -= 1
            stats["Endurance"] += 1

        elif choice == "f" and skill_points == 0:
            print("Great! Last thing. What's your name?")
            name = input()
            stats["Name"] = name
            stats["Weapon"] = "Stick"
            stats["HP"] = stats["Endurance"] * 15

            if name == "OnePunchMan":
                stats = god_mode_on()

            save_stats(stats)

            eq = {"Apple": ("POTION", 3)}
            inventory.save_inventory(eq)
            created = True

        elif choice == "t":
            stat_tutorial()
            input("Press Enter to continue...")

        elif choice == "x":
            skill_points = 10
            stats = {"Strength": 5, "Agility": 5, "Endurance": 5, "Experience": 0, "Gold": 0}


def handle_stat_management():
    """
    Function prints all possible actions in stat management
    """

    print("Press keys: S, A, E, F, T or X to choose following actions:")
    print("S. Increase Strength by 1")
    print("A. Increase Agility by 1")
    print("E. Increase Endurance by 1")
    print("F. Finish creation")
    print("T. Show info about stats")
    print("X. Reverse all changes to default state")


def stat_tutorial():
    """
    Function prints info about stats in game
    """

    print("Strength determines your Damage!")
    print("1 strength point gives you +3 attack")
    print()
    print("Agility determines your Defence!")
    print("1 agility point gives you +3 defence")
    print()
    print("Endurance determines your Health Points!")
    print("1 endurance point gives you +15 Health Points")


def god_mode_on():
    """
    Function used to set base stats to incredibly high
    """

    char_info = {"Name": "OnePunchMan", "Strength": 100, "Agility": 100, "Endurance": 100,
                 "Experience": 0, "Gold": 1000000, "Weapon": "Fist", "HP": 1500}

    return char_info


def current_stats(stats):
    """
    Function used to print current stats. Used in stat management
    """

    print("~" * 30)
    print("Strength", str(stats["Strength"]))
    print("Agility", str(stats["Agility"]))
    print("Endurance", str(stats["Endurance"]))
    print("~" * 30)


def change_exp_and_gold(exp, gold):
    """
    Function used to increase amount of experience points and gold
    """
    stats = get_stats()
    stats["Gold"] += gold
    stats["Experience"] += exp

    save_stats(stats)

    if stats["Experience"] >= 100:
        stats["Experience"] -= 100
        stats = level_up(stats)


def change_hp(change):
    """
    Changes current Health points of player
    """

    stats = get_stats()
    stats["HP"] += change
    save_stats(stats)


def level_up(stats):
    """
    Function used to manage stats. Player has to spend 3 points to finish level-up process

    Args:
        stats: Dict. containing current players stats
    """

    done = False
    skill_points = 3
    stats_copy = copy.copy(stats)

    while not done:
        os.system("clear")
        print("LEVEL UP!")
        handle_stat_management()
        current_stats(stats_copy)
        print("Skill points:", skill_points)

        choice = functions.getch().lower()

        if choice == "s" and skill_points > 0:
            skill_points -= 1
            stats_copy["Strength"] += 1

        elif choice == "a" and skill_points > 0:
            skill_points -= 1
            stats_copy["Agility"] += 1

        elif choice == "e" and skill_points > 0:
            skill_points -= 1
            stats_copy["Endurance"] += 1

        elif choice == "f" and skill_points == 0:
            done = True

        elif choice == "t":
            stat_tutorial()
            input("Press Enter to continue...")

        elif choice == "x":
            skill_points = 3
            stats_copy = copy.copy(stats)

    save_stats(stats_copy)



def save_stats(char_data):
    """
    Function used to save player stats to csv file
    """

    stats = change_dict_to_save_list(char_data)
    with open("char_save.csv", "w") as csv:
        csv.write(";".join(stats))


def change_dict_to_save_list(stats):
    """
    Function used to change "stats" dictionary to a list
    """

    char_data = [stats["Name"], str(stats["Strength"]), str(stats["Agility"]), str(stats["Endurance"]),
                 str(stats["Experience"]), str(stats["Gold"]), stats["Weapon"], str(stats["HP"])]
    return char_data


def get_stats():
    """
    Function used to load stats from csv file
    """

    with open("char_save.csv", "r") as csv:
        stats = csv.readline().split(";")

    char_info = {"Name": stats[0], "Strength": int(stats[1]), "Agility": int(stats[2]), "Endurance": int(stats[3]),
                 "Experience": int(stats[4]), "Gold": int(stats[5]), "Weapon": stats[6], "HP": int(stats[7])}

    return char_info


def get_battle_stats():
    """
    Function used to get stats which are used in combat.py module
    """

    stats = get_stats()
    weapon_damage = inventory.check_weapon_damage(stats["Weapon"])
    battle_stats = copy.copy(stats)
    battle_stats["Strength"] += weapon_damage

    return battle_stats


def show_stats():
    raw_stats = get_battle_stats()
    to_print_sheet = "| {:12} | {:<7} |"

    stats_to_print = dict()
    stats_to_print["HP"] = str(raw_stats["HP"]) + "/" + str(raw_stats["Endurance"] * 15)
    stats_to_print["Damage"] = str(raw_stats["Strength"] * 3)
    stats_to_print["Defence"] = str(raw_stats["Agility"] * 3)
    stats_to_print["Experience"] = str(raw_stats["Experience"]) + "/100"
    stats_to_print["Gold"] = str(raw_stats["Gold"])

    for info in stats_to_print:
        print(to_print_sheet.format(info, stats_to_print[info]))


if __name__ == "__main__":
    create_character()

    change_exp_and_gold(150, 50)
    print(get_battle_stats)
    stats = get_battle_stats()

    for stat in stats:
        print(stat, stats[stat])
