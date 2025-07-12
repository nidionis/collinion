# Example usage in main.py
from rules import rules, setup
from game import Game

def main():
    game = Game()
    game = setup(game) #add kinds made by user
    game.setup() # make grid and Display class
    game.run(rules)


if __name__ == "__main__":
    main()