import sys
import character

RED = "\033[1;31m"
GREEN = "\033[42m"
BLUE = "\033[44m"
GREY = "\033[1;30;40m"
RESET = "\033[0;0m"

GRASS = "▒"
WATER = "░"
ROCK = "▓"
TOWER = "♜"
SHOP = "$"
SAILOR = "⚓"
BOSS = "B"

FORBIDDEN_TO_MOVE = [ROCK, TOWER]
NPC = ["☠", "☣", "☘", SAILOR, SHOP, BOSS]
ENEMIES = ["☣", "☠"]
ITEMS = ["☘"]

# player start
START = [14, 12]

# maps in game  (30 x 90)
MAPS = [{"name": "map1.txt", "header": "Unconquered mountains", "portal": [4, 78]},
        {"name": "map2.txt", "header": "Wild river", "portal": [9, 14]},
        {"name": "map3.txt", "header": "Faraway island", "portal": [24, 12]}]


def load_map(filename):
    """
    Function loads map from .csv file

    Returns:
        map_: table representing background
    """

    with open(filename, "r") as csvfile:
        csvfile = csvfile.readlines()

    map_ = []
    for line in csvfile:
        map_.append(list(line.replace("\n", "")))

    return map_


def load_map_for_level(level):
    """
    Function load map for given level of game

    Args:
        level: level of game

    Returns:
        map_: table representing background
    """

    return load_map(MAPS[level-1]["name"])


def print_map(map_, level, player):
    """
    Function prints map with player location marked and print player menu

    Args:
        map_: table representing background
        level: level of game
        player: list containing players coordinates [y, x]
    """

    print("***", MAPS[level - 1]["header"], "***")

    player_y = player[0]
    player_x = player[1]

    for y in range(len(map_)):
        for x in range(len(map_[y])):

            if x == player_x and y == player_y:
                sys.stdout.write(RESET + BLUE)
                print("*", end="")

            else:
                if map_[y][x] == WATER:
                    sys.stdout.write(RESET + BLUE)
                elif map_[y][x] == GRASS:
                    sys.stdout.write(RESET + GREEN)
                elif map_[y][x] == ROCK:
                    sys.stdout.write(RESET + GREY)
                elif map_[y][x] == "☠" or map_[y][x] == "☣":
                    sys.stdout.write(RESET + RED)
                elif map_[y][x] == "☘":
                    sys.stdout.write(RESET + GREEN)
                elif map_[y][x] == "Ω":
                    sys.stdout.write(GREEN + GREEN)
                elif map_[y][x] == TOWER:
                    sys.stdout.write(RESET + GREEN)

                print(map_[y][x], end="")

        sys.stdout.write(RESET)
        print()

    character.show_stats()
    print("I. Open inventory")
    print("U. Use item")
    print("Y. Change weapon")
    print("If you want to exit type '0'.")


def paste_grass(map_, y, x):
    """
    Function place grass where item on map was hidden

    Args:
        map_: table representing background
        y: y coordinate of player to check
        x: x coordinate of player to check

    Returns:
        map_: table representing background
    """

    map_[y][x] = GRASS
    map_[y][x+1] = GRASS
    print('grass')

    return map_


