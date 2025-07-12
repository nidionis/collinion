
def setup(game):
    game.add_kind("dead", "black", hotness=1)
    game.add_kind("alive", "white", hotness=2)
    game.add_kind("zombie", "green")
    # Note:
    # an hotness N gives N more chance to set this kind of
    # cell than a default one when randomized
    return game #and leave this line

def rules(cell):
    if cell.side_up("alive") == 3:
        return "zombie"
    if cell.around("alive") == 3:
        return "alive"
    elif cell == "alive": # and...
        if cell.around("alive") < 2 or cell.around("alive") > 3:
            return "dead"
    if cell == "zombie":
        return "dead"

#def rules(cell):
#    if cell == "dead" and cell.around("alive") == 3:
#        return "alive"
#    elif cell == "alive": # and...
#        if cell.around("alive") < 2 or cell.around("alive") > 3:
#            return "zombie"
#    elif cell == "zombie":
#        return "dead"
#    return cell
