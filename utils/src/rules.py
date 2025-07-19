# welcome
# A line starting by # is a comment (not executed)

# define your kinds
def setup(game):
    game.add_kind("empty", "black")
    game.add_kind("alive", "white", hotness=2)
    game.add_kind("water", "blue", hotness=0)

    # Note:
    # an hotness N gives N more chance to set this kind of
    # cell than a default one when randomized

    #optional
    game.set_border("UP", "water") # make rain if gravity
    #game.set_border("LEFT", "alive")
    #game.set_border("RIGHT", "alive")
    #game.set_border("DOWN", "empty")

def hello_world(cell):
    if cell.around("alive") == 3:
        return "alive"
    if cell == "alive":
        if cell.around("alive") < 2 or cell.around("alive") >= 4:
            return "empty"

# ./run
# it in your terminal !

# Avalaible methods returning a neighbors count:
#   - around("type")
#
#   - side_up("type")
#   - side_down("type")
#   - side_left("type")
#   - side_right("type")

#   keywords:
#   - up()
#   - down()
#   - right()
#   - left()
#   - up_right()
#   - up_left()
#   - down_right()
#   - down_left()

# Note:
# You are not moving cells but stransforming themself

######################################################################

# excepting function "setup"
# all functions
# will be applied to the matrix
# in ALPHABETICAL ORDER                    

#def a_gravity(cell):
#    if cell == "empty":
#        return cell.up()
#    if cell.down("empty"):
#        return "empty"

# the matrix is modified by a_gravit BEFORE due to alphabetial order of functions
# (and that matters)


