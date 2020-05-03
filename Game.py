import random
from tabulate import tabulate
from Player import PlayerFirstMode
from Player import PlayerSecondMode


class Game:
    """
    Main class of game
    """
    def __init__(self, players_number, game_number, mode):
        """
        Constructor.
        :param players_number: number of players
        :param game_number: number of games
        :param mode: mode number
        """

        self.win_number = {}  # dictionary game:win number
        self.game_number = game_number
        self.players_number = players_number
        self.mode = mode


class GameFirstMode(Game):
    def __init__(self, players_number, game_number, mode):
        super().__init__(players_number, game_number, mode)

    def generate_players(self):
        """
        Generate players
        :return: list of players objects
        """
        players = []
        for player in range(self.players_number):
            player = PlayerFirstMode()
            players.append(player)

        return players

    def check_win_lose_game(self, player):
        """
        Check wins and loses of player in game and store it in lists
        :param player: player object
        :return:
        """
        for key, value in self.win_number.items():
            if player.get_bets().count(value) > 0:
                player.set_win_game(key)
            else:
                player.set_lose_game(key)

    def display(self, players):
        """
        Display results
        :param players: player object
        :return:
        """
        games_table = []
        players_table = []

        keys = self.win_number.keys()
        sorted_keys = sorted(keys)

        for key in sorted_keys:
            element = [key, self.win_number[key]]
            games_table.append(element)

        player_row = []
        for player in players:
            player_row.append(player.getName())
            player_row.append(str(player.get_bets())[1:-1])
            player_row.append(str(player.get_win_game())[1:-1])
            player_row.append(str(player.get_lose_game())[1:-1])
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
        """
        Main function
        :return:
        """
        players = self.generate_players()
        for player in players:
            player.make_bets()
            for game in range(int(self.game_number)):
                self.win_number[game + 1] = random.randint(1, 36)

        for player in players:
            self.check_win_lose_game(player)

        self.display(players)


class GameSecondMode(Game):

    def __init__(self, players_number, game_number, mode):
        super().__init__(players_number, game_number, mode)

    def generate_players(self):
        """
        Generate players
        :return: list of players objects
        """
        players = []
        for player in range(self.players_number):
            player = PlayerSecondMode()
            players.append(player)

        return players

    def check_win_lose_game(self, player):
        """
        Check wins and loses of player in game and store it in lists
        :param player: player object
        :return:
        """
        for key, value in self.win_number.items():
            if player.get_bets()[key].count(value) > 0:
                player.set_win_game(key)
            else:
                player.set_lose_game(key)

    def display(self, players):
        """
        Display results
        :param players: player object
        :return:
        """
        print()
        print("TOTAL NUMBER OF PLAYERS: " + str(self.game_number))
        print("TOTAL NUMBER OF GAMES: " + str(self.players_number))
        print()

        winners = {k + 1: [] for k in range(self.game_number)}
        all_bets = {k+1: [] for k in range(self.game_number)}

        for game in range(1, self.game_number+1):
            for player in players:
                all_bets[game].extend(player.get_bets()[game])
            all_bets[game] = set(all_bets[game])

        for game in range(1, self.game_number+1):
            for player in players:
                if player.get_win_game().count(game) > 0:
                    winners[game].append(player.getName())

        for key in range(1, self.game_number+1):
            print("GAME NUMBER: " + str(key))
            print("BET NUMBERS: " + str(all_bets[key])[1:-1])
            print("WIN NUMBER: " + str(self.win_number[key]))
            winners_str = str(winners[key])
            winners_str = winners_str.replace("'", "")
            print("WINNERS: " + winners_str[1:-1])
            print()

    def run(self):
        """
        Main function
        :return:
        """
        players = self.generate_players()
        for game in range(int(self.game_number)):
            self.win_number[game + 1] = random.randint(1, 36)
            for player in players:
                player.make_bets(game+1)

        for player in players:
            self.check_win_lose_game(player)

        self.display(players)
