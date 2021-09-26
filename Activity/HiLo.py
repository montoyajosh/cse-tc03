import random
import os
import sys
# I intended to skip the classes for our group work or group meeting 
# so we can try working together but they didn't formed a plan to meet.
def rules():
    # will be shown once per run of the code
    os.system("cls")
    sys.stdout.write("\033[1;36m")
    print('''Greetings! Here is mechanics of this game:
    1. There are 13 cards in the deck.
    2. You have 300 points in the start of the game.
    3. The dealer will draw a card and show it to you. The
        player will if the next card will be higher or lower.
    4. The dealer will show the next card. You will earn
        100 points for guessing it right and lose 75 points
        for guessing wrong.
Goodluck...''')
    sys.stdout.write("\033[0;0m")
    return

def deal_card (current_card): 
    # my deal_card and get_card is the same...
    while True:
        rnum=random.randrange(1,13)
        if current_card != rnum:
            break
        else:
           continue
    return rnum
        
def get_score(current_card, next_card, life_points, guess):
    # it computes the points
    correct_ans = 100
    wrong_ans = 75
    if current_card < next_card:
        if guess.lower() == "h":
            life_points += correct_ans
            sys.stdout.write("\033[0;32m")
            print("Dealer: It's higher. Your guess was right. ")
            sys.stdout.write("\033[0;0m")
            return life_points
        elif guess.lower != "h":
            life_points -= wrong_ans
            sys.stdout.write("\033[1;31m")
            print("Dealer: It's higher. Your guess was wrong. ")
            sys.stdout.write("\033[0;0m")
            return life_points
    elif current_card > next_card:
        if guess.lower() == "l":
            life_points += correct_ans
            sys.stdout.write("\033[0;32m")
            print("Dealer: It's lower. Your guess was right. ")
            sys.stdout.write("\033[0;0m")
            return life_points
        elif guess.lower != "l":
            life_points -= wrong_ans
            sys.stdout.write("\033[1;31m")
            print("Dealer: It's lower. Your guess was wrong. ")
            sys.stdout.write("\033[0;0m")
            return life_points

def determiner(guess):
    # to make h - higher and l - lower
    if guess == 'h':
        return "higher"
    else:
        return "lower"    

def start_game(first_time):
    # Main funtion of the game
    if first_time == 0:
        first_time = rules()
        first_time = 1
    input("Press Enter to start...")
    os.system("cls")
    highest_points= 300
    life_points= 300
    while True:
        print(f"Your current points: {life_points}.\n")
        current_card= int(deal_card(0))
        print(f"Dealer: The card is {current_card}")
        guess = input("Dealer: Will the next card be higher or lower? [h/l]  ")
        word = determiner(guess)
        print(f"You: I'll bet {word}")
        next_card = int(deal_card(current_card))
        print(f"Dealer: The card is {next_card}")
        life_points = get_score(current_card, next_card, life_points, guess)
        if int(life_points) > highest_points:
            highest_points = life_points
        if int(life_points) <= 0:
            print(f'''-----Game Over-----
    Highest point: {highest_points} points''')
            life_points = 300
            break 
        else:
            input("Press enter to continue")
            os.system("cls")
            continue
    player= input("Do you want to play again? [yes/no]  ")
    if player.lower() == "yes":
        return first_time
    else:
        exit()


if __name__ == "__main__":
    instruction = 0
    while True:
        instruction = start_game(instruction)