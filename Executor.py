import sys
from Game import GameFirstMode
from Game import GameSecondMode


class Executor:
    """
    Execution class for roulette game
    """
    def __init__(self, players, games, mode):
        """
        Constructor.
        :param players: number of players
        :param games: number of games
        :param mode: mode number
        """
        self.players = players
        self.games = games
        self.mode = mode

    def run(self):
        """
        Main function of class, run game depending of mode
        :return:
        """

        if self.mode == 1:
            game = GameFirstMode(self.players, self.games, self.mode)
            game.run()
        elif self.mode == 2:
            game = GameSecondMode(self.players, self.games, self.mode)
            game.run()
        else:
            print("Bad mode!")
            exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Wrong number of arguments")
        exit(1)

    try:
        n_players = int(sys.argv[1])
        n_games = int(sys.argv[2])
        n_mode = int(sys.argv[3])

        executor = Executor(n_players, n_games, n_mode)
        executor.run()

    except ValueError:
        print("Not an integer!")
        exit(1)
