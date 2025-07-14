# Example usage in main.py
from rules import setup
from game import Game

if __name__ == "__main__":
    print("press q to quit")
    game = Game()
    setup(game)
    game.setup()
    game.run()