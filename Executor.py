import sys
from Game import GameFirstMode
from Game import GameSecondMode

class Executor():
    def __init__(self, players, games, mode):
        self.players = players
        self.games = games
        self.mode = mode

    def run(self):
        if self.mode == 1:
            game = GameFirstMode(players, games, mode)
            game.run()
        elif self.mode == 2:
            game = GameSecondMode(players, games, mode)
            game.run()
        else:
            print("Bad mode!")
            exit(1)

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Wrong number of arguments")
        exit(1)

    try:
        players = int(sys.argv[1])
        games = int(sys.argv[2])
        mode = int(sys.argv[3])
    except:
        print("Not an integer!")
        exit(1)

    exec = Executor(players, games, mode)
    exec.run()