# Guess a Number, by Ashton Jones
import math
global sn, guesses, low, high, annoyance, plays
### Config ###
low = 1
high = 100
##############

####Values####
act_low = low
act_high = high
sn = math.ceil((low+high)/2)
guess_limit = math.ceil(math.log((high - low + 1), 2))
guesses = 0
annoyance = 0
plays = 0
running = 0
name = ""
##############

def done():
    global annoyance, guesses, playing
    if guesses <= guess_limit:
        print("You're Cheating " + name + ".. I don't want to play with you!")
        rt = input("Do you want to play again?")
        rt = rt.lower()
        if rt == "yes" or rt == "y":
            play()
        elif rt == "no" or rt == "n":
            print("Oh well.. you just get to sit here until you close it out")
            show_credits()
            input()
            playing = 0
            quit()
        else:
            print("I don't give second tries to those who aren't serious..")
            show_credits()
            input()
            playing = 0
            quit()
    elif annoyance >= 4:
        input(name + ".. you're honestly the worst person to play this game yet.. You should be ashamed..")
        input("I wont even give you another chance.. just get out and turn the computer off..")
        show_credits()
        input()
        playing = 0
        quit()
    else:
        rt = input("Do you want to play again?")
        print()
        rt = rt.lower()
        if rt == "yes" or rt == "y":
            start()
        elif rt == "no" or rt == "no":
            input("Well.. you just get to sit here until you close this out")
            show_credits()
            input()
            playing = 0
            quit()
        else:
            input("I don't give second tries to those who aren't serious..")
            show_credits()
            playing = 0
            quit()
            
           
def low_hig():
    global guesses, sn, act_high, act_low, guess_limit
    a1 = input("Oh? Is it lower or higher?")
    print()
    a1 = a1.lower()
    if guesses < guess_limit:
        if a1 == "lower" or a1 == "l":
            act_high = sn
            sn = math.floor((act_low+act_high)/2)
            guesses = guesses + 1
        elif a1 == "higher" or a1 == "h":
            guesses = guesses + 1
            act_low = sn
            sn = math.ceil((act_low+act_high)/2)
        else:
            low_high_annoy()
    else:
        done()
        

def low_high_annoy():
    global annoyance
    if annoyance == 0:
        print("Only type higher or lower please..")
        print()
        annoyance = annoyance + 1
    elif annoyance == 1:
        annoyance = annoyance + 1
        print("Seriously? type higher or lower.")
        print()
    elif annoyance == 2:
        annoyance = annoyance + 1
        print("I bet you're just doing this to annoy me..")
        print()
    elif annoyance == 3:
        print("You truly are pathetic..")
        print()
    elif annoyance == 4:
        print("I give up.. you're hopeless " + name + ". I quit")
        print()
        annoyance = annoyance + 1
        done()
        

def check_guess():
    global guesses
    a1 = input("Is your number " + str(sn) + "?")
    print()
    a1 = a1.lower()
    if a1 == "no" or a1 == "n":
        low_hig()
    elif a1 == "yes" or a1 == "y":
        guesses = guesses + 1
        if guesses <= 1:
            print("woo")
            print("I guessed your number in " + str(guesses) + " try")
            print()
        else:
            print("woo")
            print("I guessed your number in " + str(guesses) + " tries.")
            print()
        done()
    else:
        check_guess_annoy()
        

def check_guess_annoy():
    global annoyance
    if annoyance == 0:
        print("Once again, type yes or no as a response please..")
        print()
        annoyance = annoyance + 1
    elif annoyance == 1:
        print("You must be more stupid than I thought.. it's a YES or NO question.")
        print()
        annoyance = annoyance + 1
    elif annoyance == 2:
        print("It's a yes or no question dude..")
        print()
        annoyance = annoyance + 1
    elif annoyance == 3:
        annoyance = annoyance + 1
        print("You're STILL being this stupid? I'll say it one more time, YES or NO..")
        print()
    elif annoyance == 4:
        print("I really don't want to do this anymore " + name + "..")
        print()
        annoyance = annoyance + 1
        done()
        

def play():
    global plays, playing, guesses, guess_limit
    while playing == 1 and guesses < guess_limit:
        plays = plays + 1
        check_guess()
    done()
        
def start():
    global annoyance, plays, playing
    start = input("Think of a number between " + str(low) + " and " + str(high) + " and i'll guess it. Type start to Start.")
    start = start.lower()
    if start == "start":
        print("Have fun!")
        print()
        playing = 1
        play()
    else:
        annoyance = annoyance + 1
        print("Wow.. Can't even follow the directions.. you're stupid.")
        print()
        playing = 1
        play()

def splash():
    print ("""  __                                                   (๏_๏)/            
 /__      _   _  _    /\    |\ |     ._ _  |_   _  ._  /( )
 \_| |_| (/_ _> _>   /--\   | \| |_| | | | |_) (/_ |    / \\
                                                      """)

def show_credits():

    print("""################
#   This Rad   #
# Program Was  #
#   Made By    #
#              #
# Ashton Jones #
################""")


splash()
name = input("What is your name?")
high = int(input("Choose your high (EX: 100)"))
low = int(input("Choose your low (EX: 1)"))
start()
#            ,---,_ 
#         ,'" -o.  `. 
#        (,----      `. 
#             \        \ 
#             ;      __ --._ 
#           ," \` \`-`,--._ `. 
#          /     ` ` /        `. 
#         : (       (           \ 
#         :  \       \           \ 
#          \  \       \           \ 
#           \  \     , \.          ; 
#            \  \   :   `:.        | 
#             `. \  :    `::.     ,| 
#              ` \  \     \ `---'  \ 
#                  :-|\  __ `. `.`.  \ 
#                  | | `| \"" `       \ 
#    __,------- ,--; |,-' |\_.__\      \ 
#  -"          (  / (  /- |__    `. `-.' 
#  ----""""""`----.__`_`     `-._  `-' 
#                      `--.__    `-. 
#                            `-.    `. 
#                                `.
#        The Crow of good code



        
