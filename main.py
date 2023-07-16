from typing import Any
from board.board import Board
from game.game import Game
from deck.deck import Deck, FullDeck
from json import load as jload

TURN_BY_FULL_DECK = 3

class Main:
    def __init__(self, conf_name, conf_file):
        try:
            self.configuration = self.parseConfiguration(conf_name, conf_file) 
        except Exception as e:
            print (e)
            raise Exception(f'[ERROR]: Fail to loqd the configuration {self.configuration}')
        self.game = Game(configuration=self.configuration)
        self.board = Board(configuration=self.configuration)
        if self.game.nb_players != self.board.nb_players:
            print("[ERROR]: The number of player must be consistant with the board")
            raise Exception
        
        self.board.configureTeamsAndPlayers(self.game.teams)
        self.full_deck = FullDeck(self.game.nb_players)
        self.turn_index = 0
        self.turn_deck_index = 0

    def giveDeck(self):
        nb_cards = 4
        for player in self.game.players:
            if self.turn_deck_index == 0:
                nb_cards = 5

            player.addDeck(self.full_deck.giveCards(nb_cards))

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(self.game)
        print(self.board)
        print(self.full_deck)
        
        for i in range(TURN_BY_FULL_DECK*3):
            self.giveDeck()
            self.turn_deck_index += 1
            if self.turn_deck_index >= TURN_BY_FULL_DECK:
                self.full_deck.newFullDeck()
                self.turn_deck_index = 0


    def parseConfiguration(self, conf_name, conf_file):
        try:
            c_file = open(conf_file)
            c = jload(c_file)['game_confgurations']
            for conf in c:
                if conf['name'] == conf_name:
                    return conf
        except Exception as e:
            raise Exception('[ERROR]: Bad configuration')

main = Main(conf_name="4 Players", conf_file="configurations/gameconf.json")
main()

