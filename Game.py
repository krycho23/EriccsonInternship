import random
from tabulate import tabulate
from Player import PlayerFirstMode
from Player import PlayerSecondMode

class Game():
    def __init__(self, players_number, game_number, mode):
        self.win_number = {}  # dictionary game:win number
        self.game_number = game_number
        self.players_number = players_number
        self.mode = mode

class GameFirstMode(Game):

    def __init__(self, players_number, game_number, mode):
        super().__init__(players_number, game_number, mode)

    def generatePlayers(self):
        players = []
        for player in range(self.players_number):
            player = PlayerFirstMode()
            players.append(player)

        return players

    # check win lose for concrete player bets
    def checkWinLoseGames(self, player):

        for key, value in self.win_number.items():
            if player.getBets().count(value) > 0:
                player.setWin_game(key)
            else:
                player.setLose_game(key)

    def display(self, players):

        # Prepare elements to print in table
        games_table = []
        players_table = []

        keys = self.win_number.keys()
        sorted_keys = sorted(keys)

        for key in sorted_keys:
            element = [key, self.win_number[key]]
            games_table.append(element)

        for player in players:
            player_row = [player.getName()]
            player_row.append(str(player.getBets())[1:-1])
            player_row.append(str(player.getWin_game())[1:-1])
            player_row.append(str(player.getLose_game())[1:-1])
            players_table.append(player_row)

        print()
        print("TOTAL NUMBER OF PLAYERS: " + str(self.players_number))
        print("TOTAL NUMBER OF GAMES: " + str(self.game_number))
        print()
        print("RESULTS")
        print(tabulate(games_table, headers=["GAME", "WIN NUMBER"]))
        print()
        print(tabulate(players_table, headers=["PLAYER", "BET", "WIN", "LOSE"]))
        print()

    def run(self):

        players = self.generatePlayers()
        for player in players:
            player.makeBets()
            for game in range(int(self.game_number)):
                self.win_number[game + 1] = random.randint(1, 36)

        for player in players:
            self.checkWinLoseGames(player)

        self.display(players)

class GameSecondMode(Game):

    def __init__(self, players_number, game_number, mode):
        super().__init__(players_number, game_number, mode)

    def generatePlayers(self):
        players = []
        for player in range(self.players_number):
            player = PlayerSecondMode()
            players.append(player)

        return players

    # check win lose for concrete player bets, different bets in each game
    def checkWinLoseGames(self, player, game):

        for key, value in self.win_number.items():
            if player.getBets()[key].count(value) > 0:
                player.setWin_game(key)
            else:
                player.setLose_game(key)

    def display(self, players):

        print()
        print("TOTAL NUMBER OF PLAYERS: " + str(self.game_number))
        print("TOTAL NUMBER OF GAMES: " + str(self.players_number))
        print()

        winners = {k + 1: [] for k in range(self.game_number)}
        all_bets = {k+1: [] for k in range(self.game_number)}

        for game in range(1,self.game_number+1):
            for player in players:
                all_bets[game].extend(player.getBets()[game])
            all_bets[game] = set(all_bets[game])

        for game in range(1,self.game_number+1):
            for player in players:
                if player.getWin_game().count(game) > 0:
                    winners[game].append(player.getName())

        for key in range(1,self.game_number+1):
            print("GAME NUMBER: " + str(key))
            print("BET NUMBERS: " + str(all_bets[key])[1:-1])
            print("WIN NUMBER: " + str(self.win_number[key]))
            winners_str = str(winners[key])
            winners_str = winners_str.replace("'", "")
            print("WINNERS: " + winners_str[1:-1])
            print()

    def run(self):

        players = self.generatePlayers()
        for game in range(int(self.game_number)):
            self.win_number[game + 1] = random.randint(1, 36)
            for player in players:
                player.makeBets(game+1)

        for player in players:
            self.checkWinLoseGames(player, game+1)

        self.display(players)

