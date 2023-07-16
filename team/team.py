from team.teamexceptions import TeamException
from player.player import Player
from random import randint

class Team:
    def __init__(self, name) -> None:
        self.players = []
        self.name = name
        self.nb_players = 0
        self.first_player = 0
        self.current_player = 0

    def addPlayer(self, player):
        if (type(player) != Player):
            raise TeamException("Only Player type can be added in a team.")
        else:
            self.players.append(player)
            self.nb_players += 1

    def defineFirstPlayer(self):
        self.first_player = randint(0, self.nb_players-1)
        self.currentPlayer = self.first_player
        
    def playerToPlay(self):
        self.current_player += 1
        if self.current_player > self.nb_players-1:
            self.current_player = 0
