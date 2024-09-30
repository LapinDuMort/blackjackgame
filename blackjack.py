import random  
import time



deck_of_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
global pot
pot = None     
hand = []
dealer_hand = []
card = []
hand_value = 0
dealer_hand_value = 0
bet = 0
changed_pot = 0

def setpot():
    global pot
    pot = 100
    return pot

def adjustpotwin():
    global pot
    global bet
    pot = pot + bet
    return pot

def adjustpotblackjack():
    global pot
    global bet
    pot = pot + bet*0.5
    return pot

def adjustpotlose():
    global pot
    global bet
    pot = pot - bet
    return pot

def deal(deck_of_cards):

    for draw in range (2):
        random.shuffle(deck_of_cards)
        card = deck_of_cards.pop()
        if card == 1:
            card = "A"
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        return card
      
def handtotal():
    hand_value = 0
    for i in hand:
        if i == "J":
            hand_value += 10
        elif i == "Q":
            hand_value += 10
        elif i == "K":
            hand_value += 10
        elif i == "A":
            if hand_value >= 11:
                hand_value += 1
            else:
                hand_value += 11
        else:
            hand_value += i
    return hand_value

def dealerhandtotal():
    dealer_hand_value = 0
    for i in dealer_hand:
        if i == "J":
            dealer_hand_value += 10
        elif i == "Q":
            dealer_hand_value += 10
        elif i == "K":
            dealer_hand_value += 10
        elif i == "A":
            if dealer_hand_value >= 11:
                dealer_hand_value += 1
            else:
                dealer_hand_value += 11
        else:
            dealer_hand_value += i
    return dealer_hand_value

def newgame():
    print("Starting a new game!")
    time.sleep(2)
    global deck_of_cards
    deck_of_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
    random.shuffle(deck_of_cards)
    global hand
    hand = []
    global dealer_hand 
    dealer_hand = []
    global card 
    card = []
    global hand_value 
    hand_value = 0
    global dealer_hand_value 
    dealer_hand_value = 0

    return deck_of_cards, hand, dealer_hand, card, hand_value, dealer_hand_value
   
def hit():
    print("Hit!")
    time.sleep(1)
    hand.append(deal(deck_of_cards))
    return hand, hand_value
    
def dealerhit():

    dealer_hand_value = dealerhandtotal()
    while dealer_hand_value < 17:
        print("The dealer hits!")
        time.sleep(1)
        dealer_hand.append(deal(deck_of_cards))
        dealer_hand_value = dealerhandtotal()
        print(f"The dealer's new hand is {dealer_hand}, with a value of {dealer_hand_value}.")
        time.sleep(1)
    if dealer_hand_value > 21:
        print(f"The dealer has busted! Congratulations, you win {bet*2} chips! Would you like to [P]lay again?")
        adjustpotwin()
        userchoice2()
    elif dealer_hand_value >= 17:
        print(f"The dealer sticks on {dealer_hand_value}!")
        handcheck()
        
    return dealer_hand, dealer_hand_value

def handcheck():
    hand_value = handtotal()
    dealer_hand_value = dealerhandtotal()
    if hand_value and dealer_hand_value <= 21:
        if dealer_hand_value > hand_value:
            print("The dealer has won this round! Unlucky! Would you like to [P]lay again?")
            adjustpotlose()
            userchoice2()
        elif dealer_hand_value == hand_value:
            print("A tie! All money returned. Would you like to [P]lay again?")
            userchoice2()
        elif dealer_hand_value < hand_value:
            print(f"You have won! You win {bet*2} chips! Would you like to [P]lay again?")            
            adjustpotwin()
            userchoice2()
        else:
            print("Something has gone wrong! We will dispose of this dealer and get you a new one.")
            newgame()

def userchoice():
    userchoice = 0

    while userchoice != "H" and userchoice != "S" and userchoice != "P" and userchoice != "X":
        userchoice = input("Type [H] to hit, [S] to stand, [P] to play again or [X] to quit: ")
        userchoice = userchoice.upper()
    if userchoice == "H":
        time.sleep(1)
        hit()
        
    elif userchoice == "S":
        time.sleep(1)
        stand()
        
    elif userchoice == "P":
        time.sleep(2)
        newgame()
        gamestart()
        
    elif userchoice == "X":
        print("Thanks for playing!")
        time.sleep(2)
        quit()
    else:
        "Invalid choice! Please type [H] to hit, [S] to stand, [P] to play again or [X] to quit."

def userchoice2():
    userchoice = 0

    while userchoice != "P" and userchoice != "X":
        userchoice = input("Type [P] to play again or [X] to quit: ")
        userchoice = userchoice.upper()
    if userchoice == "P":
        time.sleep(2)
        newgame()
        gamestart()
        
    elif userchoice == "X":
        print("Thanks for playing!")
        time.sleep(2)
        quit()

    else:
        "Invalid choice! Please type [H] to hit, [S] to stand, [P] to play again or [X] to quit."

def stand():
    hand_value = handtotal()
    print(f"Standing on a hand of {hand_value}! Good Luck!")
    time.sleep(1)
    print(f"Dealer reveals their face-down card!")
    time.sleep(1)
    dealer_hand_value = dealerhandtotal()
    print(f"The dealer's starting hand is {dealer_hand}, with a value of {dealer_hand_value}.")
    time.sleep(1)
    if dealer_hand_value == 21:
        print("The dealer got blackjack! Unlucky! Would you like to [P]lay again?")
        adjustpotlose()
        userchoice2()
    elif dealer_hand_value >= 17:
        print(f"The dealer sticks on {dealer_hand_value}!")
        handcheck()
    else:
        dealerhit()

def makebet():
    global bet
    bet = 0
    global pot
    if pot == None:
        setpot()
        print(f"Your current pot is {pot}.")

    elif pot <= 0:
        print("Oops! You've run out of money! We'll be sending the collection agents to your home shortly.")
        time.sleep(3)
        quit()

    else:
        print(f"Your current pot is {pot}.")

    while True:
        try:
            bet = int(input("How much would you like to bet: "))
            break
        except ValueError:
            print("Not a valid amount! Please enter an integer as your bet: ")
            
    while bet > pot or bet == 0:
        if bet > pot:
            bet = int(input("You can't bet more money than you have! How much would you like to bet?: "))
        elif bet == 0:
            bet = int(input("You can't bet 0! How much would you like to bet?: "))
    if bet == pot:
        print("Going all in!")
    
    print(f"You have bet {bet} chips! Good luck!")

def gamestart():
    print("""Welcome to Robyn's Casino! Let's play some blackjack!
--------------------------------------------------------
          """)
    time.sleep(1)
    
    makebet()
    
    time.sleep(1)

    dealer_hand.append(deal(deck_of_cards))
    dealer_hand.append(deal(deck_of_cards))
    print(f"The dealer's starting hand is {dealer_hand[0]}, X")

    time.sleep(1)

    hand.append(deal(deck_of_cards))
    hand.append(deal(deck_of_cards))
    print(f"Your starting hand is: {hand}")
    hand_value = handtotal()
    print(f"Your starting hand value is: {hand_value}")

    time.sleep(1)
    
    if hand_value == 21:
        print(f"Blackjack! Congratulations, you win {bet*1.5} chips! Would you like to [P]lay again?")
        adjustpotblackjack()
        userchoice2()
    else:
        userchoice()
    hand_value = handtotal()
    time.sleep(1)
    print(f"Your hand is: {hand}")
    print(f"Your current hand value is: {hand_value}")
    while hand_value < 21:
        userchoice()
        hand_value = handtotal()
        print(f"Your hand is: {hand}")
        print(f"Your current hand value is: {hand_value}")
    if hand_value == 21:
        print("Congrats! Sticking on 21!")
        stand()
    else:
        print(f"Oops! You busted with a value of {hand_value}. Would you like to [P]lay again?")
        adjustpotlose()
        userchoice2()




gamestart()