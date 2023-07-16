from card.cardvalue import CardValue
from card.card import Card
from card.cardcolor import CardColor
from random import randint

class Deck:
    def __init__(self, number_of_cards, cards = []):
        self.number_of_cards = number_of_cards
        self.cards = cards

    def __str__(self):
        t = '\n=====================================\n\n[INFO] DECK:\n\n'
        index = 0
        c =''
        for card in self.cards:
            index += 1
            c = f'{c}\n\t{card.value.name} of {card.color.name}'
        return f"{t}\tCards in the deck: {index} {c}\n\n=====================================\n"
    
class FullDeck(Deck):
    def __init__(self, nb_players):
        self.number_of_cards = 52
        self.isFull = True
        self.full_deck = []
        self.nb_players = nb_players
        self.initFullDeck()
        self.newFullDeck()

    def initFullDeck(self):
        card_colors = [CardColor.CLUB, CardColor.HEART, CardColor.SPADE, CardColor.DIAMOND]
        self.isFull = True
        index = 0
        for i in range(self.nb_players):
            #define color
            if i > len(card_colors) - 1: 
                index = int(i - (len(card_colors) * int(i / len(card_colors))))
            else:
                index = i

            c = card_colors[index]
            #init cards
            for value in CardValue:
                self.full_deck.append(Card(color=c, value=value))

    def newFullDeck(self):
        self.isFull = True
        self.cards = self.full_deck.copy()

    def giveCards(self, number):
        cards = []

        for n in range(number):
            card_number = randint(0, len(self.cards)-1)
            c = self.cards[card_number]
            cards.append(c)
            self.cards.remove(c)
            self.number_of_cards -= 1

        return Deck(number_of_cards=number, cards=cards)

    def __str__(self):
        return super().__str__()

