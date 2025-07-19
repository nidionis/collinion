# Example usage in main.py
from rules import setup
from game import Game
import argparse

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Cellular Automaton Simulation")
    parser.add_argument("--zoom", type=int, default=10, help="Cell size in pixels")
    args = parser.parse_args()
    
    print("""Controls:
    - UP/DOWN: Adjust simulation speed (auto-detects maximum speed)
    - P or F: Toggle performance display
    - R: Reset to default speed
    - Q/SPACE/RETURN: Quit
    """)
    
    # Create game with command line options
    game = Game(zoom=args.zoom)
    setup(game)
    game.setup()
    game.run()