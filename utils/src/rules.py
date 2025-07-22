def setup(game):
    game.add_kind("empty", "black", weight=0)
    game.add_kind("cloud", "white", weight=-1)
    game.add_kind("water", "blue", hotness=1)
    game.add_kind("grass", "green", weight=2, hotness=1)
    game.add_kind("dirt", "brown", weight=3, hotness=1)

    game.set_border("DOWN", "dirt")   # earth bottom
    game.set_border("UP", "cloud")   # sky top

def __flow_along(cell):
    if cell.down() >= cell:
        if cell.right() < cell:
            return cell.right()
    if cell.left() > cell:
        if cell.left() >= cell.down_left():
            return cell.left()
    return cell


def a_gravity(cell):
    if cell.down().weight() < cell.weight():
        return cell.down()
    if cell.up().weight() > cell.weight():
        return cell.up()
    return __flow_along(cell)


def b_cloud_rain(cell):
    if cell == "empty" and cell.around("empty") == 8:
        return "cloud"
    if cell == "cloud":
        if cell.around("cloud") or cell.around("water"):
            return "water"

def c_water_to_grass(cell):
    if cell == "water" and cell.down() == "dirt":
        return "grass"

def d_grass_decay(cell):
    if cell == "grass" and not cell.around("water"):
        return "dirt"
    if cell == "water":
        if cell.around("grass"):
            return "cloud"

def f_spawn(cell):
    if cell == "dirt":
        if cell.side_down("dirt") == 3:
            return "empty"


