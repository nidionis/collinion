# Example usage in main.py
from rules import rules, setup

def main():
    game = setup()
    game.run(rules)


if __name__ == "__main__":
    main()