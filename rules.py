# welcome
# A line starting by # is a comment (not executed)

# define your kinds
def setup(game):
    game.add_kind("dead", "black", hotness=10)
    game.add_kind("alive", "white", hotness=15)
    game.add_kind("zombie", "green")
    game.add_kind("water", "blue")
    return game
    # Note:
    # an hotness N gives N more chance to set this kind of
    # cell than a default one when randomized

def hello_world(cell):
    if cell.around("alive") == 3:
        return "alive"
    if cell == "alive":
        if cell.around("alive") < 2 or cell.around("alive") >= 4:
            return "zombie"
    if cell == "zombie":
        return "dead"

# ./run
# it in your terminal !

# Avalaible methods returning a neighbors count:
#   - around("type")
#   - side_up("type")
#   - side_down("type")
#   - side_left("type")
#   - side_right("type")
#   - up("type")
#   - down("type")
#   - right("type")
#   - left("type")
#   - up_right("type")
#   - up_left("type")
#   - down_right("type")
#   - down_left("type")

######################################################################

# excepting function "setup"
# all functions
# will be applied to the matrix
# in ALPHABETICAL ORDER                    
# uncomment next function to implement gravity

#def a_gravity(cell):
#    if cell.up("alive") and cell == "dead":
#        return "alive"
#    if cell == "alive"  and cell.down("dead"):
#        return "dead"

# the matrix is modified by a_gravit BEFORE due to alphabetial order of functions
# (and that matters)
