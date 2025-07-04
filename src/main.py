# Example usage in main.py
from rules import rules, setup
from game import Game

def main():
    game = Game()
    game = setup(game)
    game.randomize()
    game.run(rules)


if __name__ == "__main__":
    main()