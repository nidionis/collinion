
# welcome

def setup(game):
    game.add_kind("dead", "black", hotness=1)
    game.add_kind("alive", "white", hotness=2)
    #game.add_kind("zombie", "green")
    #game.add_kind("water", "blue",)
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
#   - up("type")
#   - down("type")
#   - right("type")
#   - left("type")
#   - up_right("type")
#   - up_left("type")
#   - down_right("type")
#   - down_left("type")

# Some config in the confi folder

def hello_world(cell):
    if cell.around("alive") == 3:
        return "alive"
    if cell.around("alive") < 2 or cell.around("alive") > 3:
        return "dead"

# now
# ./run
# it in your terminal !

######################################################################

# excepting functions:
#   - "setup"
#   - or using _ in their names
# all functions
# will be applied to the matrix
# in ALPHABETICAL ORDER
#
# uncomment next function to implement gravity
# (and run it)

# def a_gravity(cell):
#     if cell.up("alive") and cell == "dead":
#         return "alive"
#     if cell == "alive"  and cell.down("dead"):
#         return "dead"
