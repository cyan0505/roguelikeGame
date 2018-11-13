import os
import time
import inventory
import character
import functions
import plot
import maps
import highscore


def game():
    """Initialaze and handles gameplay
    """

    plot.prologue()
    start_time = time.time()
    player = maps.START[:]
    level = 1
    map_ = maps.load_map_for_level(level)

    character.create_character()
    health = character.get_stats()["HP"]
    game_over = False

    while health > 0 and not game_over:

        os.system('clear')
        maps.print_map(map_, level, player)

        player = functions.player_move(map_, level, player)

        if functions.is_next_level(level, player):
            level += 1
            map_ = maps.load_map_for_level(level)

        if inventory.item_in_inventory("Sword of a Thousand Truths"):
            game_over = True

        health = character.get_stats()["HP"]

    game_total_time = int(time.time() - start_time)

    if health <0:
        plot.bye_bye()
    
    if health > 0:
        plot.epilogue()
        highscore.update_highscore(game_total_time)

    highscore.print_highscore()


if __name__ == "__main__":
    game()
