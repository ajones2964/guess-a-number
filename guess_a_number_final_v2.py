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
##############

def done():
    global annoyance, guesses
    if guesses >= guess_limit:
        print("You're Cheating.. I don't want to play with you!")
        rt = input("Do you want to play again?")
        rt = rt.lower()
        if rt == "yes":
            play()
        elif rt == "no":
            print("Oh well.. you just get to sit here until you close it out")
            input()
            guesses = 7
            show_credits()
            exit
        else:
            print("I don't give second tries to those who aren't serious..")
            input()
            guesses = 7
            show_credits()
            exit
    elif annoyance > 4:
        input("You're honestly the worst person to play this game yet.. You should be ashamed..")
        input("I wont even give you another chance.. just get out and turn the computer off..")
        input()
        guesses = 7
        show_credits()
        exit
    else:
        rt = input("Do you want to play again?")
        print()
        rt = rt.lower()
        if rt == "yes":
            show_credits()
            start()
        elif rt == "no":
            input("Well.. you just get to sit here until you close this out")
            guesses = 7
            show_credits()
            exit
        else:
            input("I don't give second tries to those who aren't serious..")
            guesses = 7
            show_credits()
            exit
            
           
def low_hig():
    global guesses, sn, act_high, act_low
    a1 = input("Oh? Is it lower or higher?")
    print()
    a1 = a1.lower()
    if a1 == "lower":
        if guesses < 6:
            act_high = sn
            sn = math.ceil((act_low+act_high)/2) - 1
        guesses = guesses + 1
    elif a1 == "higher":
        guesses = guesses + 1
        act_low = sn
        sn = math.ceil((act_low+act_high)/2) + 1
    else:
        low_high_annoy()
        

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
        print("I give up.. you're hopeless. I quit")
        print()
        annoyance = annoyance + 1
        done()
        

def check_guess():
    a1 = input("Is your number " + str(sn) + "?")
    print()
    a1 = a1.lower()
    if a1 == "no":
        low_hig()
    elif a1 == "yes":
        print("woo")
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
        print("I really don't want to do this anymore..")
        print()
        annoyance = annoyance + 1
        done()
        

def play():
    global plays
    while guesses < guess_limit:
        plays = plays + 1
        check_guess()
        
def start():
    global annoyance, plays
    start = input("Think of a number between 1 and 100, and i'll guess it. Type start to Start.")
    start = start.lower()
    if start == "start":
        print("Have fun!")
        print()
        play()
    else:
        annoyance = annoyance + 1
        print("Wow.. Can't even follow the directions.. you're stupid.")
        print()
        play()

def splash():
    print ("""  __                                                   (๏_๏)/            
 /__      _   _  _    /\    |\ |     ._ _  |_   _  ._  /( )
 \_| |_| (/_ _> _>   /--\   | \| |_| | | | |_) (/_ |    / \\
                                                      """)
def show_credits():
    if plays <= 1:
        print("""################
#   This Rad   #
# Program Was  #
#   Made By    #
#              #
# Ashton Jones #
################
""")
    else:
        pass
splash()
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



        
