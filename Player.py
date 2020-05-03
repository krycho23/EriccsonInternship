class ValueNotInRange(Exception):
   """Raised when the input is not in range"""
   pass


class Player():
    def __init__(self):
        self._name = input("Name of player: ")
        self._win_game = []  # games in which player win
        self._lose_game = []  # games in which player lose

    def setWin_game(self, win_game):
        self._win_game.append(win_game)

    def setLose_game(self, lose_game):
        self._lose_game.append(lose_game)

    def getWin_game(self):
        return self._win_game

    def getLose_game(self):
        return self._lose_game

    def getName(self):
        return self._name

class PlayerFirstMode(Player):
    def __init__(self):
        super().__init__()
        self.__bets = []

    def makeBets(self):
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

        # remove repetition
        bets = set(bets)
        bets = list(bets)

        self.__bets = bets

    def getBets(self):
        return self.__bets

class PlayerSecondMode(Player):
    def __init__(self):
        super().__init__()
        self.__bets = {}  # bets for mode 2 dictionary game: bets

    def makeBets(self,game):
        bets = input("Player " + self._name + " bet numbers(separated by space in range ) [1-36]: ")
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

        # remove repetition
        bets = set(bets)
        bets = list(bets)

        self.__bets[game] = bets

    def getBets(self):
        return self.__bets