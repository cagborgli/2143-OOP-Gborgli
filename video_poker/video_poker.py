#christopher Gborgli
#Video Poker Program

import random
import sys
import os

  
"""
@Class Card 
@Description:
    
"""
class Card(object):
    suits = ['spade','heart','diamond','club']

    def __init__(self, suit='', rank=0):
        self.suit = suit         
        self.rank = rank

    def __str__(self):
        return ("(suit:%s , rank:%s , card_image:%s)") % (self.suit, self.rank, self.card_image)
           
    def __cmp__(self,other):
        t1 = self.suit,self.rank
        t2 = other.suit,other.rank
        return int(t1[1])<int(t2[1])
   
    def __lt__(self,other):
        return self.__cmp__(other)
"""
@Class Deck 
@Description:
    This class represents a deck of cards. 
@Methods:
    pop_cards() - removes a card from top of deck
    add_card(card) - adds a card to bottom of deck
    shuffle() - shuffles deck
    sort() - sorts the deck based on value, not suit (could probaly be improved based on need)
"""       
class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(2,15):
                self.cards.append(Card(suit,rank))
                
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return " ".join(res)
    
    def pop_card(self):
        return self.cards.pop(0)
        
    def add_card(self,card):
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards = sorted(self.cards)

       
"""
@Class: Hand 
@Extends: Deck
@Description:
    This class represents a hand of cards 
@Methods:
    get_cards() - gets a card from hand
    add_card(card) - adds a card to hand
    replaceCard() - replaces a card in the hand
    sortHand() - sorts the hand
    getPosition() - gets the index of card 
""" 
class Hand(object):
    def __init__(self,label=''):
        self.cards = []
        self.label = label
        self.rankCount = {}     # Used to calculate pairs, three of a kind, etc.
        self.suitCount = {}     # Used to calculate flush
        
    def addCard(self,card):
        
        if not card.suit in self.suitCount:
            self.suitCount[card.suit] = 1
        else:
            self.suitCount[card.suit] += 1
            
        if not card.rank in self.rankCount:
            self.rankCount[card.rank] = 1
        else:
            self.rankCount[card.rank] += 1  
            
        self.cards.append(card)
        
    def getCards(self):

        return self.cards
   
    def sortHand(self):
        self.cards = sorted(self.cards)
        
    def replaceCard(self,id,card):
        print(self.rankCount)
        print(self.suitCount)
        print(id)
        self.cards[id] = card
        
    def getPosition(self,card):
        return self.cards.index(card)
        
        
    def trashHand(self):
        self.cards = []
        self.rankCount = {}     # Used to calculate pairs, three of a kind, etc.
        self.suitCount = {}     # Used to calculate flush     
"""
@Class Video Poker 
@Description:
    This class handles all things video poker 
@Methods:
    deal() - deals a set number of cards 
    Score() - processes hand to see what hand possibilities there are and returns the score if any
    getCard() - gets card from the deck
    RoyalFlush() - checks for  A, K, Q, J, 10, all the same suit
    FourAcesorEight() - checks for four Eights or four Aces
    StraightFlush() - checks for Five cards in a sequence and all in the same suit.
    FourSevens() - checks for four sevens
    FourofaKind() - checks for All four cards of the same rank. 
    FullHouse() -checks for Three of a Kind with a pair
    Flush() - checks for Any five cards of the same suit, but not in a sequence.
    Straight() - checks for Five cards in a sequence, but not of the same suit.
    Threeofakind() - checks for three cards of the same rank
    TwoPairs() - checks for two different pairs
    Pair() - checks for Two cards of the same rank. Must be Jacks or better.
""" 
class VideoPoker(object):
    def __init__(self):
        self.score=0
        self.deck = Deck()

    def deal(self,number=5):
        hand = Hand()
        self.deck.shuffle()
        for i in range(0,number):
            hand.addCard(self.deck.pop_card())         
        return hand
        
    def getCard(self):
        return self.deck.pop_card()
            
    def Score(self,hand):
            if self.RoyalFlush(hand):
                self.score +=800
                return self.score
            if self.FourAcesorEight(hand):
                self.score +=80
                return self.score
            if self.StraightFlush(hand):
                self.score +=50
                return self.score
            if self.FourSevens(hand):
                self.score +=50
                return self.score
            if self.FourofaKind(hand):
                self.score +=25
                return self.score
            if self.FullHouse(hand):
                self.score +=8
                return self.score
            if self.Flush(hand):
                self.score +=5
                return self.score
            if self.Straight(hand):
                self.score +=4
                return self.score
            if self.Threeofakind(hand):
                self.score +=3
                return self.score
            if self.TwoPairs(hand):
                self.score +=2
                return self.score
            if self.Pair(hand):
                self.score +=1
                return self.score

            return 0

    def RoyalFlush(self,hand):
        if self.RoyalFlush(hand) and self.Astraight(hand):
            return True
        
    def FourAcesorEight(self):
        if 14 in hand.rankCount:
            if hand.rankCount[14]==4:
                return True
        if 8 in hand.rankCount:
            if hand.rankCount[8]==4:
                return True
    
    def StraightFlush(self,hand):
        if self.StraightFlush(hand) and self.RoyalFlush(hand):
            return True
    
    def FourSevens(self,hand):
        if 7 in hand.rankCount:
            if hand.rankCount[7]==4:
                return True

    def FourofaKind(self,hand):
        for kind4 in hand.rankCount:
            if hand.rankCount[kind4]==4:
                return True

    def FullHouse(self,hand):
        if self.Threeofakind(hand) and self.Pair(hand):
            return True

    def Flush(self,hand):
        if len(hand.suitCount)==1:
            return True

    def Straight(self,hand):
        a =(hand.cards[4].rank - hand.cards[0].rank)
        if a ==4 and len(hand.rankCount)==5:
            return True

    def Threeofakind(self,hand):
        for kind3 in hannd.rankCount:
            if hand.rankCount(kind3)==3:
                return True

    def TwoPairs(self,hand):
        if len(hand.rankCount) ==3:
            return True

    def Pair(self,hand):
        if len(hand.rankCount) ==4:
            for pair in hand.rankCount:
                if pair > 10 and hand.rankCount(pair) ==2:
                    return True

    def Astraight(self,hand):
        if hand.cards[4].rank==14:
            if hand.cards[4].rank - hand.cards[0]==4:
                if len(hand.rankCount)==5:
                    return True

class Game_driver(VideoPoker):
    def __init__(self):
        self.hand=[]
        super().__init__()

    def menu(self):
        game_menu= True
        while game_menu:
            print("""
            1.New Game
            2.Play Again
            3.Exit/Quit
            """)
            game_menu=input("Select what you would like to do ")

            if game_menu=="1":
                print("\nWe are going to play a New Game\n")
                self.deck=Deck()
                Game_driver.menu2(self)

            elif game_menu=="2":
                print("\nGreat!! Lets Play Again\n")
                Game_driver.menu2(self)
            elif game_menu=="3":
                print("\n It was fun playing \n") 
                game_menu=False
            else:
                print("\n Not Valid Choice Try again")

    def menu2(self):
        option=None
        print("**Feeling Lucky with your Hand, Enter(1) \n")
        print("**Do you want to swap 1 card?, Enter(2) \n")
        print("**Not confident with your Hand?Lets change all then ,Enter(3)")

        option=input()
           
        if option=="1":
            option=False        
        elif option=="2":
            pass
        elif option=="3":
            pass


if __name__=='__main__':
    game = Game_driver()
    game.menu() 
