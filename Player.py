class ValueNotInRange(Exception):
    """Raised when the input is not in range"""
    pass


class Player:
    """
    Player object class
    """
    def __init__(self):
        """
        Constructor.
        Initialize name of player with input.
        Initialize win_game and lose_game lists with empty list
        """
        self._name = input("Name of player: ")
        self._win_game = []  # games in which player win
        self._lose_game = []  # games in which player lose

    def set_win_game(self, win_game):
        self._win_game.append(win_game)

    def set_lose_game(self, lose_game):
        self._lose_game.append(lose_game)

    def get_win_game(self):
        return self._win_game

    def get_lose_game(self):
        return self._lose_game

    def get_name(self):
        return self._name


class PlayerFirstMode(Player):
    def __init__(self):
        """
        Constructor with initialization of parent class
        Initialize bets variable to store bets
        """
        super().__init__()
        self.__bets = []

    def make_bets(self):
        """
        Get bets from player input
        :return: bets
        """
        bets = input("Player " + self._name + " bet numbers(separated by space in range ) [1-36]: ")
        bets = bets.split(" ")

        print("bets= " + str(bets))

        try:
            for i in range(len(bets)):
                bets[i] = int(bets[i])
                if bets[i] < 1 or bets[i] > 36:
                    raise ValueNotInRange
        except ValueError:
            print("Not an integer!")
            exit(1)
        except ValueNotInRange:
            print("One of values is not in range!")
            exit(1)

        bets = set(bets)
        bets = list(bets)

        self.__bets = bets

    def get_bets(self):
        return self.__bets


class PlayerSecondMode(Player):
    def __init__(self):
        """
        Constructor with initialization of parent class
        Initialize bets variable to store bets
        """
        super().__init__()
        self.__bets = {}

    def make_bets(self, game):
        """
        Get bets from player input
        :return: bets
        """
        bets = input("Bet numbers for player: " + self._name + " in game number: " + str(game) +
                     " (separated by space in range [1-36]): ")
        bets = bets.split(" ")

        try:
            for i in range(len(bets)):
                bets[i] = int(bets[i])
                if bets[i] < 1 or bets[i] > 36:
                    raise ValueNotInRange
        except ValueError:
            print("Not an integer!")
            exit(1)
        except ValueNotInRange:
            print("One of values is not in range!")
            exit(1)

        bets = set(bets)
        bets = list(bets)

        self.__bets[game] = bets

    def get_bets(self):
        return self.__bets
