import functions
import plot
import rogue
import highscore
import os


def main():
    os.system("clear")
    choice = ""
    while choice != "3":
        os.system("clear")
        plot.main_menu()
        choice = functions.getch()
        if choice == "1":
            rogue.game()
        elif choice == "2":
            highscore.print_highscore()
        elif choice == "0":
            plot.about()


if __name__ == "__main__":
    main()
