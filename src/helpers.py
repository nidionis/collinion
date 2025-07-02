def around(cell, matrix, cell_type):
    return matrix.count_neighbors(cell.x, cell.y, cell_type)
