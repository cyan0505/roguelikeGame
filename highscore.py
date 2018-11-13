import time
import character
import os
from operator import itemgetter


def print_highscore():
    os.system("clear")
    with open("top_list.csv", "r") as current_top:
        current_top = current_top.readline().split(";")
        current_top = [score.split(",") for score in current_top]

    for i in range(15):
        try:
            print("{}. {}: {}".format((i+1), current_top[i][0], current_top[i][1]))
        except IndexError:
            pass

    input("Press Enter to continue...")
    os.system("clear")


def update_highscore(time):
    stats = character.get_stats()
    name = stats["Name"]
    player_score = [name, 1/time * 10000]

    with open("top_list.csv", "r") as current_top:
        current_top = current_top.readline().split(";")
        current_top = [score.split(",") for score in current_top]

    current_top.append(player_score)

    for i in current_top:
        i[1] = int(i[1])

    current_top.sort(key=itemgetter(1), reverse=True)

    with open("top_list.csv", "w") as file:
        to_save = ""
        for score in current_top:
            score = [score[0], str(score[1])]
            to_save += ",".join(score) + ";"

        to_save = to_save[:-1]
        file.write(to_save)


if __name__ == "__main__":
    print_highscore()
