import random
import math

# config
low = 1
high = 10
limit = math.ceil(math.log(high, 2))


# helper functions
def show_start_screen():
    print("!@#!@#!@#!@#!@#!@#!@#!@#!@#")
    print("!   Grand Number Thing    #")
    print("!@#!@#!@#!@#!@#!@#!@#!@#!@#")

def show_credits():
    print("This awesome game was created by a loser with a jacket.")
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print()
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")
    print("You have " + str(limit) + " guesses.")

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print()
        print("You guessed too low.")
    elif guess > rand:
        print()
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print()
        print("You win!")
    else:
        print("You are such a loser! The number was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print()
            print("You dunce, use 'y' or 'n'.")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



