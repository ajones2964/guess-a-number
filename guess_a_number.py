import random

# config
low = 1
high = 100
limit = 10

# start game
rand = random.randint(low,high)
print("I'm thinking of a number from 1 to 100.");

guess = -1
tries = 0

while guess != rand and tries < 10:
    guess = input("Take a guess: ")
    guess = int(guess)
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

    tries += 1

# Ending
if guess == rand:
    print("You win")
else:
    print("You're dumb, the number i was thinking of is " + str(rand) + ".")
