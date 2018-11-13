import random
import character
import inventory
import os
import enemies
import functions
import plot


os.system("clear")


def combat(monster):
    """
    Function manages whole combat system, reads player and enemy statisctics and calls
    other functions to return combat rewards (such as experiece, items and gold)
    """

    win = True
    monster_stats, graphic, monster_name, exp, gold = monster

    player_stats = character.get_battle_stats()
    player_stats = convert_stats(player_stats)
    player_damage = player_stats["Attack"] - monster_stats["Defence"]
    monster_damage = monster_stats["Attack"] - player_stats["Defence"]

    while monster_stats["HP"] > 0 and player_stats["HP"] > 0:

        handle_graphics(graphic, monster_name, monster_stats, player_stats)
        combat_action = functions.getch()

        if combat_action == "1":

            if player_damage > 0:
                monster_stats["HP"] -= player_damage

            if monster_damage > 0 and monster_stats["HP"] > 0:
                player_stats["HP"] -= monster_damage

        elif combat_action == "2":
            player_stats["HP"] += inventory.use_item()

        elif combat_action == "3":
            character.change_hp(-10)
            return not win

    return resolve_encounter(player_stats["HP"], exp, gold, monster_name)


def resolve_encounter(player_hp, exp, gold, monster_name):
    win = True

    default_hp = character.get_stats()["HP"]
    lost_hp = default_hp - player_hp

    if player_hp <= 0:
        character.change_hp(-lost_hp)
        plot.bye_bye()

    else:
        if monster_name == "Alladin the Prince of Thieves":
            plot.alladin_transformation()
        else:
            print("""Monster defeated!

            "Your rewards are: Experience - {0} Gold - {1}""".format(exp, gold))
            character.change_exp_and_gold(exp, gold)
            character.change_hp(-lost_hp)
            usable = ["Apple", "Cake", "Bread", "Meat", "Health Potion"]
            loot = random.choice(usable)
            inventory.add_to_inventory([loot])

            return win


def convert_stats(player_stats):
    player_health = player_stats["HP"]
    player_damage = player_stats["Strength"] * 3
    player_deffence = player_stats["Agility"] * 3

    return {"HP": player_health, "Attack": player_damage, "Defence": player_deffence}


def handle_graphics(graphic, monster_name, monster_stats, player_stats):
    os.system("clear")
    print(graphic)
    print(monster_name)
    print(monster_stats)
    print()
    print(player_stats)
    print("""Choose combat action:

                    (1) Attack
                    (2) Use item
                    (3) Run away""")


def combat_in_level(level):

    if level == 1:
        return combat(enemies.skeleton())

    elif level == 2:
        return combat(enemies.minotaur())

    elif level == 3:
        return combat(enemies.dragon())

    elif level == 4:
        return plot.bandit_camp_begin()

    elif level == 5:
        return plot.bandit_camp_alladin()


if __name__ == "__main__":
    combat_in_level(1)
