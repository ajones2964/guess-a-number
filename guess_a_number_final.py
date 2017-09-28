import math
### Function That Keeps Game Running ###
annoyance = 0
def running():
    global sn, guesses, low, high, annoyance
    guesses = 0
    annoyance = 0

### Config ###
    low = 1
    high = 100
    sn = high / 2
    guess_limit = math.ceil(math.log((high - low + 1), 2))
 
### Determine Endings ###
    def done():
        global annoyance, guesses
        if guesses >= guess_limit:
            print("You're Cheating.. I don't want to play with you!")
            rt = input("Do you want to play again?")
            rt = rt.lower()
            if rt == "yes":
                running()
            elif rt == "no":
                print("Oh well.. you just get to sit here until you close it out")
                input()
            else:
                print("I don't give second tries to those who aren't serious..")
        elif annoyance > 4:
            input("You're honestly the worst person to play this game yet.. You should be ashamed..")
            input("I wont even give you another chance.. just get out and turn the computer off..")
            input()
            guesses = 7
            exit
        else:
            rt = input("Do you want to play again?")
            print()
            rt = rt.lower()
            if rt == "yes":
                running()
            elif rt == "no":
                input("Oh well.. you just get to sit here until you close it out")
                guesses = 7
                exit
            else:
                input("I don't give second tries to those who aren't serious..")
                guesses = 7
                exit
               
### Game Loop: Taking input ###
    while guesses <= 6:
        def low_hig():
            global sn, guesses, low, high, annoyance
            a1 = input("Oh? Is it lower or higher?")
            print()
            a1 = a1.lower()
            if a1 == "lower":
                if guesses < 6:
                    high = sn
                guesses = guesses + 1
            elif a1 == "higher":
                guesses = guesses + 1
                low = sn + 1
            else:
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

### Determining Guesses ###
        sn = (low+high)//2
        a1 = input("Is your number " + str(sn) + "?")
        print()
        a1 = a1.lower()
        if a1 == "no":
            low_hig()
        elif a1 == "yes":
            print("woo")
            done()
        else:
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
### End of Loop ###
            

    
### Starting Line Of Text ###
start = input("Think of a number between 1 and 100, and i'll guess it. Type start to Start.")
start = start.lower()
if start == "start":
    print("Have fun!")
    print()
else:
    annoyance = annoyance + 1
    print("Wow.. Can't even follow the directions.. you're stupid.")
    print()
running()
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



            
