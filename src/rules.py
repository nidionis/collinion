from game import Game

def setup():
    game = Game()

    # an hotness N gives N more chance to set this kind of
    # cell than a default one when randomized
    game.add_kind("dead", "black", hotness=5)
    game.add_kind("alive", "white", hotness=2)
    game.add_kind("zombie", "green")

    game.randomize()
    return game

def rules(cell):
    if cell == "dead" and cell.around("alive") == 3:
        return "alive"
    elif cell == "alive": # and...
        if cell.around("alive") < 2 or cell.around("alive") > 3:
            return "zombie"
    elif cell == "zombie":
        return "dead"
