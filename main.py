from src.matrix import Matrix
from src.display import Display
from src.helpers import around
from src.kinds import Kinds

def rules(cell, matrix):
    alive_neighbors = around(cell, matrix, "alive")
    
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
    kinds = Kinds()
    kinds.add("dead", "black", hotness=5)  # 0 hotness means won't appear randomly
    kinds.add("alive", "white", hotness=2)
    kinds.add("zombie", "green", hotness=3)
    counts = {"dead": 0, "alive": 0, "zombie": 0, "null": 0,}
    for i in range(100000):
        kind = kinds.rand()
        counts[str(kind)] += 1
    print(counts)

if __name__ == "__main__":
    main()
