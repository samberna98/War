#  File: War.py
#  Description: Program that simulates two people playing the War cardgame
#  Date Created: 9/24/17
#  Date Last Modified: 10/6/17
import random, math

class Card:

    def __init__(self, suit, rank): # creates card with specified suit and rank

        self.s = str(suit)
        self.r = str(rank)
        self.value = 0
        if(self.r == "A"):
            self.value = 14
        elif(self.r == "K"):
            self.value = 13
        elif (self.r == "Q"):
            self.value = 12
        elif (self.r == "J"):
            self.value = 11
        else:
            self.value = int(self.r)

    def __str__(self):
        return(self.r + self.s)

class Deck:
    
    def __init__(self): # creates deck containing 52 normal cards, no jokers
        self.cardList = [Card("C",2), Card("C",3), Card("C",4), Card("C",5), Card("C",6), Card("C",7), Card("C",8), Card("C",9), Card("C",10), Card("C","J"), Card("C","Q"), Card("C","K"), Card("C","A"), Card("D",2), Card("D",3), Card("D",4), Card("D",5), Card("D",6), Card("D",7), Card("D",8), Card("D",9), Card("D", 10), Card("D","J"), Card("D","Q"), Card("D", "K"), Card("D","A"), Card("H",2), Card("H",3), Card("H",4), Card("H",5), Card("H",6), Card("H",7), Card("H",8), Card("H",9), Card("H",10), Card("H","J"), Card("H","Q"), Card("H","K"), Card("H","A"), Card("S",2), Card("S",3), Card("S",4), Card("S",5), Card("S",6), Card("S",7), Card("S",8), Card("S",9), Card("S",10), Card("S","J"), Card("S","Q"), Card("S","K"), Card("S","A")]   

    def shuffle(self): # shuffles deck randomly
        random.shuffle(self.cardList)

    def dealOne(self, other): # deals card to the specified Player object
        other.hand.append(self.cardList[0])
        self.cardList.remove(self.cardList[0])
        other.handTotal+=1
        
    def __str__(self): # prints card deck 

        line = " "
        x = 0
        z = 0
        while x < 4:
            y = 0
            while y < 13:
                line += (str(self.cardList[z]) + " ")
                y+=1
                z += 1
            line += " \n "
            x+=1

        return line
                
        
class Player:

    def __init__(self): # creates player with an empty hand
        self.hand = []
        self.handTotal = 0

    def __str__(self): # prints the player's hand 

        ln = int(math.ceil(len(self.hand)/13))
        results = "  "
        x = 0
        z = 0
        tot = len(self.hand)
        
        while x < ln:
            y = 0
            if tot >= 13:
                while y < 13:
                    results += (str(self.hand[z]) + " ")
                    y+=1
                    z+=1
                    tot-=1
            else:
                while y < tot:
                    results += (str(self.hand[z]) + " ")
                    z+=1
                    tot -=1
            
            results += "\n  "
            x+=1
        return results

    def handNotEmpty(self): # checks to see if the players hand strength is not zero, 0 = no cards left, loses game
        if self.handTotal > 0:
            return True
        else:
            return False

def playGame(other, firstPlayer, secondPlayer): # method that executes and displays the game
    
    roundCount = 1
    y = 0
        
    while firstPlayer.handTotal > 0 and secondPlayer.handTotal> 0:
        print("\nRound ",roundCount,":")
        print("Player 1 plays: ", firstPlayer.hand[y])
        print("Player 2 plays: ", secondPlayer.hand[y], "\n")
            
        x = 0                       
        if (firstPlayer.hand[x].value == secondPlayer.hand[x].value):
            print("\nWar starts: ", firstPlayer.hand[x], " = ", secondPlayer.hand[x])
            other.cardList.append(firstPlayer.hand[x])
            firstPlayer.hand.pop(x)
            other.cardList.append(secondPlayer.hand[x])
            secondPlayer.hand.pop(x)
            print("Player 1 puts ", firstPlayer.hand[x], " face down.")
            other.cardList.insert(x+1,firstPlayer.hand[x])
            firstPlayer.hand.pop(x)
            print("Player 2 puts ", secondPlayer.hand[x], " face down.")
            other.cardList.append(secondPlayer.hand[x])
            secondPlayer.hand.pop(x)
            print("Player 1 puts ", firstPlayer.hand[x], " face down.")
            other.cardList.insert(x+2, firstPlayer.hand[x])
            firstPlayer.hand.pop(x)
            print("Player 2 puts ", secondPlayer.hand[x], " face down.")
            other.cardList.append(secondPlayer.hand[x])
            secondPlayer.hand.pop(x)
            print("Player 1 puts ", firstPlayer.hand[x], " face down.")
            other.cardList.insert(x+3, firstPlayer.hand[x])
            firstPlayer.hand.pop(x)
            print("Player 2 puts ", secondPlayer.hand[x], " face down.")
            other.cardList.append(secondPlayer.hand[x])
            secondPlayer.hand.pop(x)
            print("Player 1 puts ", firstPlayer.hand[x], " face up.")
            print("Player 2 puts ", secondPlayer.hand[x], " face up.\n")
            

            if (firstPlayer.hand[x].value > secondPlayer.hand[x].value):
                print("Player 1 wins round ", roundCount, ": ", firstPlayer.hand[x], " > ", secondPlayer.hand[x], "\n")
                other.cardList.insert(x+4, firstPlayer.hand[x])
                firstPlayer.hand.pop(x)
                other.cardList.append(secondPlayer.hand[x])
                secondPlayer.hand.pop(x)
                firstPlayer.hand += other.cardList
                other.cardList = []
                firstPlayer.handTotal = len(firstPlayer.hand)
                secondPlayer.handTotal = len(secondPlayer.hand)
                print("Player 1 now has ", firstPlayer.handTotal, " card(s) in hand:")
                print(firstPlayer)
                print("Player 2 now has ", secondPlayer.handTotal, " card(s) in hand:")
                print(secondPlayer)

            else:
                print("Player 2 wins round ", roundCount, ": ", secondPlayer.hand[x], " > ", firstPlayer.hand[x], "\n")
                other.cardList.insert(x+4, firstPlayer.hand[x])
                firstPlayer.hand.pop(x)
                other.cardList.append(secondPlayer.hand[x])
                secondPlayer.hand.pop(x)
                secondPlayer.hand += other.cardList
                other.cardList = []
                firstPlayer.handTotal = len(firstPlayer.hand)
                secondPlayer.handTotal = len(secondPlayer.hand)
                print("Player 1 now has ", firstPlayer.handTotal, " card(s) in hand:")
                print(firstPlayer)
                print("Player 2 now has ", secondPlayer.handTotal, " card(s) in hand:")
                print(secondPlayer)

        elif (firstPlayer.hand[x].value > secondPlayer.hand[x].value):
            print("Player 1 wins round ", roundCount, ": ", firstPlayer.hand[x], " > ", secondPlayer.hand[x], "\n")
            other.cardList.append(firstPlayer.hand[x])
            firstPlayer.hand.pop(x)
            other.cardList.append(secondPlayer.hand[x])
            secondPlayer.hand.pop(x)
            firstPlayer.hand += other.cardList
            other.cardList = []
            firstPlayer.handTotal = len(firstPlayer.hand)
            secondPlayer.handTotal = len(secondPlayer.hand)
            print("Player 1 now has ", firstPlayer.handTotal, " card(s) in hand:")
            print(firstPlayer)
            print("Player 2 now has ", secondPlayer.handTotal, " card(s) in hand:")
            print(secondPlayer)

        elif (firstPlayer.hand[x].value < secondPlayer.hand[x].value):
            print("Player 2 wins round ", roundCount, ": ", secondPlayer.hand[x], " > ", firstPlayer.hand[x],"\n")
            other.cardList.append(firstPlayer.hand[x])
            firstPlayer.hand.pop(x)
            other.cardList.append(secondPlayer.hand[x])
            secondPlayer.hand.pop(x)
            secondPlayer.hand += other.cardList
            other.cardList = []
            firstPlayer.handTotal = len(firstPlayer.hand)
            secondPlayer.handTotal = len(secondPlayer.hand)
            print("Player 1 now has ", firstPlayer.handTotal, " card(s) in hand:")
            print(firstPlayer)
            print("Player 2 now has ", secondPlayer.handTotal, " card(s) in hand:")
            print(secondPlayer)

        else:
            break
     
        roundCount += 1
        
            
        
def main():

    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    
    random.seed(15)                 # leave this in for grading purposes
    cardDeck.shuffle()              # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)                 # print the deck so we can see that your shuffle worked

    
    player1 = Player()              # create a player
    player2 = Player()              # create another player

    for i in range(26):             # deal 26 cards to each player, one at 
       cardDeck.dealOne(player1)    #   a time, alternating between players
       cardDeck.dealOne(player2)

    print("Initial Hands:")
    print("Player1: ")
    print(player1)
    print("Player2:")
    print(player2) 
        
    playGame(cardDeck,player1,player2)

    if player1.handNotEmpty():
        print("\n\nGame over.  Player 1 wins!")
    else:
        print("\n\nGame over.  Player 2 wins!")

    print ("\n\nFinal hands:")    
    print ("Player 1:   ")
    print (player1)                 # printing a player object should print that player's hand
    print ("\nPlayer 2:")
    print (player2)                 # one of these players will have all of the cards, the other none
    
main()
