# Example usage in main.py
from src.game import Game


def main():
    # Create and setup the game
    game = Game(width=100, height=100)

    # Register cell kinds - stick to one set of names to avoid confusion
    game.add_kind("empty", "black", hotness=5)  # We'll use "empty" consistently
    game.add_kind("alive", "white", hotness=2)
    game.add_kind("zombie", "green", hotness=1)
    
    # No need to register "dead" separately if we're using "empty"

    # Randomize the field
    game.randomize()

    # Define rules using the clean syntax
    def life_rules(cell):
        if cell == "empty" and cell.around("alive") == 3:
            return "alive"
        elif cell == "alive" and (cell.around("alive") < 2 or cell.around("alive") > 3):
            return "zombie"
        elif cell == "zombie":
            return "empty"  # Return "empty" instead of "dead" for consistency
        return cell

    # Run the simulation
    game.run(life_rules)


if __name__ == "__main__":
    main()