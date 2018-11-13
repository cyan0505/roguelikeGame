import random
import character
import inventory
import os


enemies = ["""

                                                                _( (~\\
        _ _                          /                          ( \> > \\
    -/~/ / ~\                       :;                \       _  > /(~\/
    || | | /\ ;\                     |l      _____     |;     ( \/    > >
    _\\)\)\)/ ;;;                   `8o  __-~     ~\   d|      \      //
    ///(())(__/~;;\                    "88p;.  -. _\_;.oP       (_._/ /
    (((__   __ \\   \                  `>,% (\  (\./)8"         ;:'  i
    )))--`.'-- (( ;,8 \               ,;%%%:  ./V^^^V'          ;.   ;.
    ((\   |   /)) .,88  `: ..,,;;;;,-::::::'_::\   ||\         ;[8:   ;
    )|  ~-~  |(|(888; ..``'::::8888oooooo.  :\`^^^/,,~--._    |88::  |
    |\ -===- /|  \8;; ``:.      oo.8888888888:`((( o.ooo8888Oo;:;:'  |
    |_~-___-~_|   `-\.   `        `o`88888888b` )) 888b88888P""'     ;
    ; ~~~~;~~         "`--_`.       b`888888888;(.,"888b888"  ..::;-'
    ;      ;              ~"-....  b`8888888:::::.`8888. .:;;;''
        ;    ;                 `:::. `:::OOO:::::::.`OO' ;;;''
    :       ;                     `.      "``::::::''    .'
        ;                           `.   \_              /
    ;       ;                       +:   ~~--  `:'  -';
                                    `:         : .::/ 
        ;                            ;;+_  :::. :..;;;
                                    ;;;;;;,;;;;;;;;,;""",

           """   
                                            __----~~~~~~~~~~~------___
                                      .  .   ~~//====......          __--~ ~~
                      -.            \_|//     |||\\  ~~~~~~::::... /~
                   ___-==_       _-~o~  \/    |||  \\            _/~~-
           __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
       _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
     .~       .~       |   \\ -_    /  /-   /   ||      \   /
    /  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
    |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\\
             '         ~-|      /|    |-~\~~       __--~~
                         |-~~-_/ |    |   ~\_   _-~            /\\
                              /  \     \__   \/~                \__
                          _--~ _/ | .-~~____--~-/                  ~~==.
                         ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                    -_     ~\      ~~---l__i__i__i--~~_/
                                    _-~-__   ~)  \--______________--~~
                                  //.-~~~-~_--~- |-------~~~~~~~~
                                         //.-~~~--\ """,

           """
                                 _.--""-._
     .                         ."         ".
    / \    ,^.         /(     Y             |      )\\
    /  `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
    |       :|    `>   '.     l_..-------.._l      .'
    |     __l;__ .'      "-.__.||_.-'v'-._||`"----"
    \  .-' | |  `              l._       _.'
     \/    | |                   l`^^'^^'j
           | |                _   \_____/     _
           j |               l `--__)-'(__.--' |
           | |               | /`---``-----'"1 |  ,-----.
           | |               )/  `--' '---'   \'-'  ___  `-.
           | |              //  `-'  '`----'  /  ,-'   I`.  \\
        _  L |_            //  `-.-.'`-----' /  /  |   |  `. \\
         '._' / \         _/(  `/   )- ---' ;  /__.J   L.__.\ :
         `._;/7(-.......'  /        ) (     |  |            | |
         `._;l _'--------_/        )-'/     :  |___.    _._./ ;
           | |                 .__ )-'\  __  \  \  I   1   / /
           `-'                /   `-\-(-'   \ \  `.|   | ,' /
                              \__  `-'    __/  `-. `---'',-'
                                 )-._.-- (        `-----'
                             """,
           """
                             
          \ \\|||///               \ \\|||///                \ \\|||///
        .  =======              .  =======               .  =======
       / \| O   O |            / \| O   O |             / \| O   O |
       \ /  \\ _'/              \ /  \\ _'/               \ /  \\ _'/
        #   _| |_               #   _| |_                #   _| |_
       (#) (     )             (#) (     )              (#) (     )
        #\//|* *|\\             #\//|* *|\\              #\//|* *|\\
        #\/(  *  )/             #\/(  *  )/              #\/(  *  )/
        #   =====               #   =====                #   =====
        #   (\ /)               #   (\ /)                #   (\ /)
        #   || ||               #   || ||                #   || ||
       .#---'| |----.          .#---'| |----.           .#---'| |----.
        #----' -----'           #----' -----'            #----' -----'""",
           """
                                         _
                       \"-._ _.--"~~"--._
                        \   "            ^.    ___
                        /                  \.-~_.-~
                 .-----'     /\/"\ /~-._      /
                /  __      _/\-.__\L_.-/\     "-.
               /.-"  \    ( ` \_o>"<o_/  \  .--._\\
              /'      \    \:     "     :/_/     "`
                      /  /\ "\    ~    /~"
                      \ I  \/]"-._ _.-"[
                   ___ \|___/ ./    l   \___   ___
              .--v~   "v`   `-.__   __.-' ) ~v"   ~v--.
           .-{   |               "~"               |   }-.
          /   \  |                                 |  /   \\
         ]     \ |  |           |    |           | | /     [
         /\     \|  |           |    |           | |/     /\\
        /  ^._  _K.__\ ________/      \_________/_,K_  _.^  \\
       /   /  "~/  "\                           /"  \~"  \   \\
      /   /    /     \ _          :          _ /     \    \   \\
    .^--./    /       Y___________l___________Y       \    \.--^.
    [    \   /        |        [/    ]        |        \   /    ]
    |     "v"         l________[____/]________j         }r"     /
    }------t          /                       \       /`-.     /
    |      |         Y                         Y     /    "-._/
    }-----v'         |         :               |     7-.     /
    |   |_|          |         l               |    / . "-._/
    l  .[_]          :          \              :  r[]/_.  /
     \_____]                     "--.             "-.____/""",
           """              
                            _ |||||||| _
                            \\\  |   |//
                             \_   \  ./
                  .--.         \   \/           .--.
                  ||||_        /\.  `\         _||||
                  |  ||      ./  /\   \        ||  |
                  |  /     ./   /  \   `\      \   |
                  |  |    /    /    `\   \      \  |
      .--.        |  |   /   ./  ___  \   \     |  |       .--.
     //| \        |  |   |   |.-'''\``\\   |    |  |       / |\\
     \\\| \       |  |   |   /    __|__|   |    |  |      /  ///
      ``\  \      |  |   |  `.   /     \   |    |  |     /  /''
         \  \     `   \  |   |(\/ o  o |   |   /   '    /  .'
         `   `     \   \ |   |`\    u  |   | ./   /    /   /
          \   `_    \   `\    \ \  -- /    |/    /    /   /
           \    `---.\    \    \/`-._/\   //    /   _/   /
            \_        `  _-    /       ` .-  .-----'    /
              `---.___ /'                     \        /
                     ./                        \------'
                    /    .-'\            |/\    \\
                 _./    /'  /             \ `\   `-.
            __.-'     /'   |  o   |  \   o |  `\    `-._
    ____.--'     __.-'      \    /    \___/     `_._    `--._____
   /===.____.---'            |           |          `----.____===\\
                             \           /
                             |           |
                           /              \ __.-----.__
                       ____--           -'  ___.       )
                   _.-'          \    /  _-'           /
                 ./     _.-_._  __/-./--'          _.-'
                 (            `-.______     ___.--'/
                  \_                   `---'  ___/'
                    `--._______.-------------/"""]


def skeleton():
    """
    Function generates monster statiscs for skeletons

    Returns: monster statistics as dictionary and monster graphic, monster name,
    monster experience worth, gold reward as variable
    """

    os.system("clear")
    graphic = enemies[2]
    monster_stats = {"Attack": random.randint(15, 25), "Defence": random.randint(5, 15), "HP": random.randint(50, 150)}
    exp = random.randint(35, 50)
    gold = random.randint(10, 20)
    print(graphic)
    monster_name = "Skeleton Warrior"
    print(monster_name)
    print(monster_stats)
    return monster_stats, graphic, monster_name, exp, gold


def minotaur():
    """
    Function generates monster statiscs for minotaur

    Returns: monster statistics as dictionary and monster graphic, monster name,
    monster experience worth, gold reward as variable
    """

    os.system("clear")
    graphic = enemies[0]
    monster_stats = {"Attack": random.randint(25, 35), "Defence": random.randint(
        15, 25), "HP": random.randint(150, 250)}
    exp = random.randint(35, 50)
    gold = random.randint(10, 20)
    print(graphic)
    monster_name = "Hellish Minotaur"
    print(monster_name)
    print(monster_stats)
    return monster_stats, graphic, monster_name, exp, gold


def dragon():
    """
    Function generates monster statiscs for dragon

    Returns: monster statistics as dictionary and monster graphic, monster name,
    monster experience worth, gold reward as variable
    """

    os.system("clear")
    graphic = enemies[1]
    monster_stats = {"Attack": random.randint(35, 45), "Defence": random.randint(
        25, 35), "HP": random.randint(250, 350)}
    gold = random.randint(10, 20)
    exp = random.randint(35, 50)
    print(graphic)
    monster_name = "Red Dragon"
    print(monster_name)
    print(monster_stats)
    return monster_stats, graphic, monster_name, exp, gold


def bandits():
    """
    Function generates enemies statiscs for bandits

    Returns: monster statistics as dictionary and monster graphic, monster name,
    monster experience worth, gold reward as variable
    """

    os.system("clear")
    graphic = enemies[3]
    monster_stats = {"Attack": 50, "Defence": 40, "HP": 400}
    gold = random.randint(10, 20)
    exp = 100
    print(graphic)
    monster_name = "Band of sneaky bandits"
    print(monster_name)
    print(monster_stats)
    return monster_stats, graphic, monster_name, exp, gold


def alladin_hum():
    """
    Function generates enemy statiscs for alladin

    Returns: monster statistics as dictionary and monster graphic, monster name,
    monster experience worth, gold reward as variable
    """

    os.system("clear")
    graphic = enemies[4]
    monster_stats = {"Attack": 60, "Defence": 50, "HP": 500}
    gold = random.randint(10, 20)
    exp = 100
    print(graphic)
    monster_name = "Alladin the Prince of Thieves"
    print(monster_name)
    print(monster_stats)
    return monster_stats, graphic, monster_name, exp, gold
