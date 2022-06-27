import random 
import time
def get_user_input(rnd_num):
    while True:
        print(f"\nRound {rnd_num}\n")
        if rnd_num == 1:
            time.sleep(.4)
            print("It's best of 3!")
        time.sleep(.65)
        user_input = input("Choose:\n1. Rock\n2. Paper\n3. Scissors\n")
        user_input = user_input.upper()
        if user_input == "ROCK" or user_input == "PAPER" or user_input == "SCISSORS":
            break
        else:
            print("Please input either Rock, Paper, or Scissors")
    return user_input

def get_computer_output():
    random_number = random.randrange(1,3)
    if random_number == 1:
        computer_output = "ROCK"
    if random_number == 2:
        computer_output = "PAPER"
    if random_number == 3:
        computer_output = "SCISSORS"
    return computer_output

def showdown(user_choice, computer_choice):
    if user_choice == "ROCK":
        if computer_choice == "ROCK":
            return "DRAW"
        if computer_choice == "PAPER":
            return "LOST"
        if computer_choice == "SCISSORS":
            return "WON"
    
    if user_choice == "PAPER":
        if computer_choice == "ROCK":
            return "WON"
        if computer_choice == "PAPER":
            return "DRAW"
        if computer_choice == "SCISSORS":
            return "LOST"
    
    if user_choice == "SCISSORS":
        if computer_choice == "ROCK":
            return "LOST"
        if computer_choice == "PAPER":
            return "WON"
        if computer_choice == "SCISSORS":
            return "DRAW"

def output_score(user_choice, computer_choice, result, user_score, computer_score):
    print(f"You: {user_choice}!")
    time.sleep(1)
    print(f"Computer: {computer_choice}!")
    time.sleep(.5)
    if result == "WON":
        print("You won!\n")
        user_score += 1
    if result == "LOST":
        print("Oh no!  You lost!\n")
        computer_score += 1
    if result == "DRAW":
        print("It was a Draw!\n")
    time.sleep(1)
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}\n")
    return [user_score, computer_score]
    
def end_game(user_score, computer_score):
    if user_score == 2:
        print("Good job!  You won!")
        time.sleep(.5)
    elif computer_score == 2:
        print("Darn! It looks like you lost!")
        time.sleep(.5)
    while True:
        loop = input("Would you like to play again?  Y/N? ")
        if loop.upper() == "Y":
            print("Restarting...")
            time.sleep(1)
            return True
        elif loop.upper() == "N":
            print("Goodbye!")
            return False
        else:
            print("Please input either Y or N.")

def main():
    loop = True
    while loop:
        user_score = 0
        computer_score = 0
        score_list = [user_score, computer_score]
        rnd_num = 1
        while user_score < 2 and computer_score < 2:
            user_choice = get_user_input(rnd_num)
            computer_choice = get_computer_output()
            result = showdown(user_choice, computer_choice)
            score_list = output_score(user_choice, computer_choice, result, user_score, computer_score)
            user_score = score_list[0]
            computer_score = score_list[1]
            rnd_num += 1
            time.sleep(1)
        loop = end_game(user_score, computer_score)


main()