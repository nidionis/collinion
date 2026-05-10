# here a prototype of a world

def setup(game):
    game.add_kind("empty", "black", weight=0)
    game.add_kind("cloud", "white", weight=-1)
    game.add_kind("water", "blue", hotness=1)
    game.add_kind("grass", "green", weight=2, hotness=1)
    game.add_kind("wood", "brown", weight=3, hotness=1)
    game.add_kind("dirt", "orange", weight=4, hotness=1)

    game.set_border("DOWN", "dirt")   # earth bottom
    game.set_border("UP", "cloud")   # sky top

def a_flow_along(cell):
    if cell == "cloud":
        return cell
    if cell.side_down(cell) >= 2:
        if cell.up() == cell:
            if cell.right() == "empty" or cell.left() == "empty":
                return "empty"

def b_cloud_rain(cell):
    if cell == "cloud":
        if cell.around("cloud") + cell.around("water") >= 3:
            return "water"

def c_gravity(cell):
    if cell.down().weight() < cell.weight():
        return cell.down()
    if cell.up().weight() > cell.weight():
        return cell.up()

def d_water_to_grass(cell):
    if cell == "water":
        if cell.around("wood"):
            return "grass"

def e_grass_to_wood(cell):
    if cell == "grass":
        if cell.around("grass") >= 2:
            if cell.around("wood") == 1:
                if not cell.around("water"):
                    return "wood"

def f_grass_decay(cell):
    if cell == "water":
        if cell.around("grass"):
            return "cloud"
