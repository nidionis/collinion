from src.field import Field
from src.display import Display
from src.helpers import around
from src.kinds import Kinds

def rules(cell, field):
    alive_neighbors = around(cell, field, "alive")
    
    if cell.kind == "empty" and alive_neighbors == 3:
        return "alive"
    elif cell.kind == "alive" and (alive_neighbors < 2 or alive_neighbors > 3):
        return "dead"
    #return "zombie"
    #elif cell.kind == "zombie":
    #    return "dead"
    return cell.kind

def main():
    # Initialize cell kind registry with hotness values
    print("Initializing cell kinds...")
    kinds = Kinds()
    kinds.add("dead", "black", hotness=5)  # 0 hotness means won't appear randomly
    kinds.add("alive", "white", hotness=2)
    kinds.add("zombie", "green", hotness=3)
    field = Field(kinds, 100, 100)
    display = Display(field, kinds)
    display.run(rules)



if __name__ == "__main__":
    main()
