def setup(game):
    game.add_kind("empty", "black", weight=0)
    game.add_kind("cloud", "white", weight=-1)
    game.add_kind("water", "blue", hotness=1)
    game.add_kind("grass", "green", weight=2, hotness=1)
    game.add_kind("dirt", "brown", weight=3, hotness=1)

    game.set_border("DOWN", "dirt")   # earth bottom
    game.set_border("UP", "cloud")   # sky top

def bb_cloud_rain(cell):
    if cell == "cloud":
        if cell.around("cloud") or cell.around("water"):
            return "water"

def a_flow_along(cell):
    if cell == "cloud":
        return cell
    if cell.up() == cell:
        if cell.right() < cell:
            return cell.right()
    if cell.left() > cell:
        if cell.left() == cell.up_left():
            return cell.left()

def b_gravity(cell):
    if cell.down().weight() < cell.weight():
        return cell.down()
    if cell.up().weight() > cell.weight():
        return cell.up()

def c_water_to_grass(cell):
    if cell == "water" and cell.down() == "dirt":
        return "grass"

def d_grass_decay(cell):
    if cell == "grass" and not cell.around("water"):
        return "dirt"
    if cell == "water":
        if cell.around("grass"):
            return "cloud"

