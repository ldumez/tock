from json import load as jload
from game.gameexceptions import GameConfigurationError, GameException, GameConfigurationFileError
from player.playerexceptions import PlayerException
from player.player import Player
from team.team import Team
from team.teamexceptions import TeamException
from random import randint
from pawn.pawn import Pawn
from pawn.pawnexceptions import PawnException

class Game:

    def __init__(self, configuration):
        #Configure the game
        self.teams = []
        self.players = []
        self.nb_teams = 0
        self.nb_players = 0
        self.current_team = 0

        self.global_configuration = configuration['global_configuration']
        self.number_of_pawns_by_players = self.global_configuration['number_of_pawns_by_players']

        try:
            try:
                self.players_configuration = configuration['players_configuration']
            except Exception:
                raise GameConfigurationFileError
            
            self.parseAndCheckConfiguration()

            if self.nb_players != self.global_configuration['number_of_players']:
                raise GameException("Number of player unconsistant.")

            try:
                self.assignPawns()
            except PawnException:
                raise GameException

        except GameConfigurationError as e:
            print(e)
            raise GameException
        except GameConfigurationFileError as e:
            print(e)
            raise GameException

        self.defineFirstTeam()

    def __str__(self) -> str:
        s = '\n=====================================\n\n[INFO] GAME:\n\n'
        for team in self.teams:
            s += f'\t{team.name}:\n'
            for player in team.players:
                s += f'\t\t{player.name}\n'
        s += '\n=====================================\n'
        return s



    def defineFirstTeam(self):
        self.first_team = randint(0, len(self.teams)-1)
        for t in self.teams:
            t.defineFirstPlayer()

    def teamToPlay(self):
        self.current_team += 1
        if self.current_team > self.nb_teams-1:
            self.current_team = 0

    def parseAndCheckConfiguration(self):
        self.nb_players = len(self.players_configuration)        
        player_names = []
        player_colors = []
        for player in self.players_configuration:
            #check mandatory fields
            try:
                name_field = player["name"]
                color_field = player["color"]
                team_field  = player["team"]
            except KeyError as ke:
                raise GameConfigurationError(f"{ke} is missing")

            #check if the player name already exist in the game
            if name_field in player_names:
                raise GameConfigurationError(f"Player {name_field} already exist")
            else:
                player_names.append(name_field)

            #check if the player color already exist in the game
            if color_field in player_colors:
                raise GameConfigurationError(f"Color {color_field} already exist")
            else:
                player_colors.append(color_field)

            
            #manage team
            team_found = False
            for t in self.teams:
                if team_field == t.name:
                    try:
                        p = Player(name=name_field, color=color_field)
                        t.addPlayer(p)
                        self.players.append(p)
                        team_found = True
                    except TeamException as e:
                        print(e)
                        raise GameException

            if not team_found:
                team = Team(team_field)
                try:
                    p = Player(name=name_field, color=color_field)
                    team.addPlayer(p)
                    self.players.append(p)
                    self.teams.append(team)
                    self.nb_teams += 1
                except TeamException as e:
                    print(e)
                    raise GameException


        #check if at least two teams are configured
        if len(self.teams) < 2:
            raise GameConfigurationError(f"Only one team configured")
        
        #check if all teams have the same number of players
        excepted_nb_of_player = self.teams[0].nb_players
        for t in self.teams:
            if excepted_nb_of_player != t.nb_players:
                raise GameConfigurationError(f"Teams don't contain the same number of players")

    def assignPawns(self):
        for player in self.players:
            for n in range(self.number_of_pawns_by_players):
                player.addPawn(Pawn(n))
