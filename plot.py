import os
import time
import combat
import enemies
import hot_cold
import inventory


def main_menu():
    """
    Function handle main menu screen
    """
    
    print("""
                 (                                                              
                 )\ )                    (                        )             
                (()/( (  (         (     )\ )         (    (   ( /(    (   (    
                 /(_)))\))(    (   )(   (()/(   (    ))\  ))\  )\())  ))\  )(   
                (_)) ((_)()\   )\ (()\   ((_))  )\  /((_)/((_)((_)\  /((_)(()\  
                / __|_(()((_) ((_) ((_)  _| |  ((_)(_)) (_))  | |(_)(_))   ((_) 
                \__  \\ V  V // _ \| '_|/ _` |  (_-</ -_)/ -_) | / / / -_) | '_| 
                |___/ \_/\_/ \___/|_|  \__,_|  /__/\___|\___| |_\_\ \___| |_| )""")
    for i in range(3):
        print()
    print("""                                           Main menu:

                                         (1) Play
                                         (2) Highscores
                                         (3) Exit
                                         
                                         (0) About authors""")


def prologue():
    """ 
    Story telling function
    """

    os.system("clear")
    print("You are waking up alone in the dark...")
    time.sleep(2)
    print("You noticed all your equipment is gone, and slowly starting to remeber events of last night.")
    time.sleep(2)
    print("Yesterday you were attacked by bandits, just a while after dusk.")
    time.sleep(2)
    print("You realize that the legendary Sword of a Thousand Thruths, betrusted on you by your father,"
          " has been stolen by the bandits.")
    time.sleep(2)
    print()
    print("You have to get it back!")
    time.sleep(2)
    print()
    print("Now go and slay the bandit lord! Take what is yours!")
    time.sleep(2)
    input("Press Enter to continue...")


def epilogue():
    """ 
    Story telling function
    """

    os.system("clear")
    print("Congratulation oh mighty Hero!")
    time.sleep(2)
    print("You defefted Alladin the Prince of Thieves, and got back Sword of a Thousand Thruths.")
    time.sleep(2)
    print("Now you can finally rest in peace.")
    time.sleep(1)
    for i in range(3):
        print(".")
        time.sleep(1)
    print("Forever...")
    time.sleep(1)
    print()
    input("Press Enter to continue...")


def bandit_camp_travel():
    """ 
    Story telling function (begins bandit camp event)
    """

    os.system("clear")
    print("You are about to sail to the Bandit Camp.")
    time.sleep(2)
    print("After starting this event you will have to face very powerful enemies, without ability to escape.")
    time.sleep(2)
    player_choice = input("Are you sure you want to go to Bandit Camp? y/n ")
    if player_choice == y:
        bandit_camp_bagin()


def bandit_camp_begin():
    """ 
    Story telling function (starts combat with bandits)
    """

    bandits = enemies.bandits()
    os.system("clear")
    print("After almost 10 hours of rowing, you finally arrive to partly sunken, bandit cave.")
    time.sleep(2)
    print("You stepped out of the boat and try to tie boats rope to big rock on a shore.")
    time.sleep(2)
    print("Suddenly you hear bandits war cry: Kill the intruder!!!!")
    time.sleep(2)
    print("You turn back to face this new danger!")
    print()
    input("Press Enter to continue...")
    combat.combat(bandits)


def bandit_camp_alladin():
    """ 
    Story telling function (starts combat with alladin)
    """

    alladin_hum = enemies.alladin_hum()
    os.system("clear")
    print("YOU BLOODY BASTARD!! YOU KILLED MY COMRADES!!")
    time.sleep(1)
    for i in range(2):
        print(".")
        time.sleep(1)
    print("You won't leave this cave alive! I am Alladin the Prince of Thieves!")
    time.sleep(2)
    print("Prepare to die!!!!!!!!!!!")
    print()
    input("Press Enter to continue...")
    return combat.combat(alladin_hum)


def alladin_transformation():
    """ 
    Story telling function (last fight in the game)
    """

    os.system("clear")
    print("Argh....!")
    time.sleep(1)
    print("You are quite strong my friend...")
    time.sleep(2)
    print("But it is not even my final form!")
    time.sleep(2)
    print("Long time has passed since i had a worthy opponent.")
    time.sleep(2)
    print("Now you will feel my true power!!!")
    time.sleep(3)
    for i in range(10):
        os.system("clear")
        print(enemies.enemies[4])
        time.sleep(0.1)
        os.system("clear")
        print(enemies.enemies[5])
        time.sleep(0.1)
    print()
    print("We are playing hot and cold game")
    input("Press Enter to continue...")
    hot_cold.hot_cold_game()


def alladin_defeat():
    """ 
    Story telling function, the fall of Alladin
    """

    print("Ahhhh you are as smart as you are strong!!!")
    time.sleep(2)
    print("No one ever defeated me in Hot and Cold game...")
    time.sleep(2)
    print("Now i have to commit suicide... Oh, your sword is back there.")
    print("*Sword of a Thousand Truth was added to your inventory*")
    inventory.add_to_inventory(["Sword of a Thousand Truths"])
    input("Press Enter to continue...")


def about():
    """
    Info about authors
    """

    os.system("clear")
    print("Authors:")
    print()
    print("(1) Angelika Nieduziak  -  level designer")
    print()
    print("(2) Wojciech Makieła  -  character artist and inventory developer")
    print()
    print("(3) Dawid Grygier  -  story writer and combat mechanics inventor")
    print()
    input("Press Enter to continue...")



def bye_bye():
    """
    Game over function, handles players death
    """

    os.system("clear")
    print("Your opponent was too strong...")
    time.sleep(1)
    print("You've should be better prepared...")
    time.sleep(2)
    print()
    print()
    for i in range(20):
        os.system("clear")
        print("""
                        *             )            (     
        (       (     (  `         ( /(            )\ )  
        )\ )    )\    )\))(  (     )\())(   (  (  (()/(  
        (()/( ((((_)( ((_)()\ )\   ((_)\ )\  )\ )\  /(_)) 
        /(_))_)\ _ )\(_()((_|(_)    ((_|(_)((_|(_)(_))   
      (_)) __(_)_\(_)  \/  | __|  / _ \ \ / /| __| _ \  
        | (_ |/ _ \ | |\/| | _|  | (_) \ V / | _||   /  
         \___/_/ \_\|_|  |_|___|  \___/ \_/  |___|_|_\ """)
        time.sleep(0.05)
        os.system("clear")
        print("""
                        *             )            (     
        (       (     (  `         ( /(            )\ )  
        )\ )    )\    )\))(  (     )\())(   (  (  (()/(  
        (()/( ((((_)( ((_)()\ )\   ((_)\ )\  )\ )\  /(_)) 
         /(_))_)\ _ )\(_()((_|(_)    ((_|(_)((_|(_)(_))   
      (_)) __(_)_\(_)  \/  | __|  / _ \ \ / /| __| _ \  
        | (_ |/ _ \ | |\/| | _|  | (_) \ V / | _||   /  
         \___/_/ \_\|_|  |_|___|  \___/ \_/  |___|_|_\ """)
        time.sleep(0.05)
        os.system("clear")
        print("""
                        *             )            (     
        (       (     (  `         ( /(            )\ )  
        )\ )    )\    )\))(  (     )\())(   (  (  (()/(  
         (()/( ((((_)( ((_)()\ )\   ((_)\ )\  )\ )\  /(_)) 
         /(_))_)\ _ )\(_()((_|(_)    ((_|(_)((_|(_)(_))   
      (_)) __(_)_\(_)  \/  | __|  / _ \ \ / /| __| _ \  
        | (_ |/ _ \ | |\/| | _|  | (_) \ V / | _||   /  
         \___/_/ \_\|_|  |_|___|  \___/ \_/  |___|_|_\ """)
        os.system("clear")
        time.sleep(0.05)
        print("""
                        *             )            (     
        (       (     (  `         ( /(            )\ )  
         )\ )    )\    )\))(  (     )\())(   (  (  (()/(  
         (()/( ((((_)( ((_)()\ )\   ((_)\ )\  )\ )\  /(_)) 
         /(_))_)\ _ )\(_()((_|(_)    ((_|(_)((_|(_)(_))   
      (_)) __(_)_\(_)  \/  | __|  / _ \ \ / /| __| _ \  
        | (_ |/ _ \ | |\/| | _|  | (_) \ V / | _||   /  
         \___/_/ \_\|_|  |_|___|  \___/ \_/  |___|_|_\ """)
        os.system("clear")
        time.sleep(0.05)
        print("""
                        *             )            (     
         (       (     (  `         ( /(            )\ )  
         )\ )    )\    )\))(  (     )\())(   (  (  (()/(  
         (()/( ((((_)( ((_)()\ )\   ((_)\ )\  )\ )\  /(_)) 
         /(_))_)\ _ )\(_()((_|(_)    ((_|(_)((_|(_)(_))   
      (_)) __(_)_\(_)  \/  | __|  / _ \ \ / /| __| _ \  
        | (_ |/ _ \ | |\/| | _|  | (_) \ V / | _||   /  
         \___/_/ \_\|_|  |_|___|  \___/ \_/  |___|_|_\ """)
        time.sleep(0.05)


if __name__ == "__main__":
    bandit_camp_alladin()
