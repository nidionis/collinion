# welcome
# A line starting by # is a comment (not executed)

# define your kinds
def setup(game):
    game.add_kind("dead", "black", weight=0)
    game.add_kind("alive", "white", hotness=2)
    game.add_kind("zombie", "green", hotness=0)

def zombies(cell):
    if cell.around("alive") == 3:
        return "alive"
    if cell == "alive":
        if cell.around("alive") < 2 or cell.around("alive") >= 4:
            return "zombie"
    if cell == "zombie":
        return "dead"

