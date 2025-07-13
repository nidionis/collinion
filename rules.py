# welcome in this
def setup(game):
    game.add_kind("dead", "black", hotness=1)
    game.add_kind("alive", "white", hotness=2)
    game.add_kind("zombie", "green")
    # Note:
    # an hotness N gives N more chance to set this kind of
    # cell than a default one when randomized
    return game #and leave this line

# Avalaible methods returning a neighbors count:
#   - around("type")
#   - side_up("type")
#   - side_down("type")
#   - side_left("type")
#   - side_right("type")
#   - cell_up("type")
#   - cell_down("type")
#   - cell_right("type")
#   - cell_left("type")
#   - cell_up_right("type")
#   - cell_up_left("type")
#   - cell_down_right("type")
#   - cell_down_left("type")

def rules(cell):
    if cell.side_up("alive") == 3:
        return "zombie"
    if cell.around("alive") == 3:
        return "alive"
    elif cell == "alive":
        if cell.around("alive") < 2 or cell.around("alive") > 3:
            return "dead"
    if cell == "zombie":
        return "dead"

# now ./run.py it !
# maybe some confing available in the config folder