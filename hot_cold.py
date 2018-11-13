import random
import plot

def hot_cold_game():
    """ 
    Hot and cold game for final boss
    """

    guess_number = 10

    random_number_list = []

    while len(random_number_list) < 3:

        random_number = random.randint(1, 9)
        random_number = str(random_number)

        if random_number not in random_number_list:
            random_number_list.append(random_number)

    print(random_number_list)

    while guess_number > 0:

        user_answer = list(input("Please guess a number: "))

        if len(user_answer) == 3:

            if user_answer == random_number_list:
                plot.alladin_defeat()
                guess_number = 0
            else:
                if user_answer[0] == random_number_list[0]:
                    print("Hot")
                
                elif user_answer[0] == random_number_list[1] or user_answer[0] == random_number_list[2]:
                    print("Warm")
                
                elif user_answer[0] not in random_number_list:
                    print("Cold")
            
                if user_answer[1] == random_number_list[1]:
                    print("Hot")
                
                elif user_answer[1] == random_number_list[0] or user_answer[1] == random_number_list[2]:
                    print("Warm")
                
                elif user_answer[1] not in random_number_list:
                    print("Cold")
                    
                if user_answer[2] == random_number_list[2]:
                    print("Hot")
                
                elif user_answer[2] == random_number_list[1] or user_answer[2] == random_number_list[0]:
                    print("Warm")
                
                elif user_answer[2] not in random_number_list:
                    print("Cold")

            guess_number -= 1

        else:
            print("3 digit")

if __name__ == "__main__":
    hot_cold_game()