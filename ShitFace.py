import random
Suit = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "x", "j", "q", "k")
#For this game having different suits does not matter
# x = 10 // J = Jack // Q = queen // K = king //  M = Joker
# I decided to use single characters to define cards, i thought it would be clearer

deck = list(Suit * 4)
# Composing the deck with 4 suits

deck.append("M")
deck.append("M")
# Adding Jokers

random.shuffle(deck)
#shuffling the deck!

Hand = [deck[x:x+15] for x in range(0, len(deck), 15)]
Hand_Player1 = list(Hand[0])
Hand_Player2 = list(Hand[1])
Hand_Player3 = list(Hand[2])
SecretCards = list(Hand[3])
# In this game you distribute the whole deck to the players. 15 cards to hand and 3 secret cards.
# Each player receives 3 "secret cards" they cannot look at!
# I Think the best way would be to handle the secret cards is to keep a pool of 9 cards separated.
# when a player is allowed to use one of their 3 secret cards, a random one from the pool will be picked.
# nontheless i coded below distribution of th secret cards

SC_distribution = [SecretCards[x:x+3] for x in range(0, len(SecretCards), 3)]
SC_Player1 = SC_distribution[0]
SC_Player2 = SC_distribution[1]
SC_Player3 = SC_distribution[2]
#now everybody has 15 + 3 cards

print("Player 1's hand: " + str(Hand_Player1))
print("Player 1's secret cards: " + str(SC_Player1))
print("Player 2's hand: " + str(Hand_Player2))
print("Player 2's secret cards: " + str(SC_Player2))
print("Player 3's hand: " + str(Hand_Player3))
print("Player 3's secret cards: " + str(SC_Player3))
# here i print out all the cards to check if everything goes right

Player1 = str(Hand_Player1 + SC_Player1)
Player2 = str(Hand_Player2 + SC_Player2)
Player3 = str(Hand_Player3 + SC_Player3)
# here i define the players and i think this will be needed to define winning condition later on.
# you win when you are out of cards
# print(G1)
# print(G2)
# print(G3)


Name_Player1 = input("What is your name, Player 1? ")
Name_Player2 = input("What is your name, Player 2? ")
Name_Player3 = input("What is your name, Player 3? ")
#here i ask players name to personalize the game!

print("Welcome to ShitFace " + Name_Player1 + "! You are playing against: " + Name_Player2 + " and " + Name_Player3)
print("You have 3 secret cards on the board and the following in your hand " + str(Hand_Player1))
# I welcomw the player and provide the information needed to start the game!
# needs to be done for different players

print("Choose 3 cards to put on the board! ")
#the first phase of the game is about choosing 3 cards from your hand and playing them

RevealedCards_Player1 = list()
Count_RC_Player1 = 0
Count_Limit = 3
#This counts that the Player plays 3 cards!


#The 3 cards need to be different from each other, and ofcourse they need to be in your hand to be played.
#so this are the condition within a whileloop:

while Count_RC_Player1 != Count_Limit:
    if Count_RC_Player1 == 0:
        Select_Cards_Player1 = input("Input your first card! ")
        Check_Hand = Hand_Player1.count(Select_Cards_Player1)
        Check_RC_Player1 = RevealedCards_Player1.count(Select_Cards_Player1)
#if player chose 0 cards, ask to pick 1

        if Select_Cards_Player1 != 0:
                if Count_RC_Player1 != 1:
                    RevealedCards_Player1.append(Select_Cards_Player1)
                    Hand_Player1.remove(Select_Cards_Player1)
                    Count_RC_Player1 += 1
                    print("Now you have: " + str(Hand_Player1) + "On the Board you have 3 secret cards and " + str(RevealedCards_Player1))
#if the card is approved, add a +1 to the counter and asks the player for the next

                else:
                    print("You must choose cards that are different from each other! Pick another one")
#if the card was already chosen, the software will ask for another one. (i know its useless for the first one)

        else:
            print("You don't own this card! choose another one!")
#the software will check if the player owns the card ! if the player does not own it, a new one is asked!

    if Count_RC_Player1 == 1:
        Select_Cards_Player1 = input("Input your second Card! ")
        Check_Hand = Hand_Player1.count(Select_Cards_Player1)
        Check_RC_Player1 = RevealedCards_Player1.count(Select_Cards_Player1)
        if Check_Hand != 0:
            if Check_RC_Player1 != 1:
                RevealedCards_Player1.append(Select_Cards_Player1)
                Hand_Player1.remove(Select_Cards_Player1)
                Count_RC_Player1 += 1
                print("Now you have: " + str(Hand_Player1) + "In banco hai 3 carte coperte e " + str(RevealedCards_Player1))
            else:
                print("You must choose cards that are different from each other! Pick another one")
        else:
            print("You don't own this card! choose another one!")
    if Count_RC_Player1 == 2:
        Select_Cards_Player1 = input("Input your third card! ")
        Check_Hand = Hand_Player1.count(Select_Cards_Player1)
        Check_RC_Player1 = RevealedCards_Player1.count(Select_Cards_Player1)
        if Check_Hand != 0:
            if Check_RC_Player1 != 1:
                RevealedCards_Player1.append(Select_Cards_Player1)
                Hand_Player1.remove(Select_Cards_Player1)
                Count_RC_Player1 += 1
                print("Now you have: " + str(Hand_Player1) + "In banco hai 3 carte coperte e " + str(RevealedCards_Player1))
            else:
                print("You must choose cards that are different from each other! Pick another one")
        else:
            print("You don't own this card! choose another one!")
else:
    print("Well done! you chose your 3 cards and Shitface can begin!")

#The process is repeated until the player has picked 3 cards
