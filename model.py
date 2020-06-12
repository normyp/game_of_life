# Any live cell with two or three live neighbours survives.
# grid of 0's and 1's to represent dead or alive cells
GRID_SIZE_X = 3
GRID_SIZE_Y = 5
cell = {
    "status": 0,
    "cell_neighbours": 3
}


# changes status of all the cells
def generate(grid):
    newgrid = grid.copy()
    for x in range(0, GRID_SIZE_X):
        for y in range(0, GRID_SIZE_Y):
            if grid[x][y] == 1:
                if countLiveNeighbours(x, y, grid) == 2 or countLiveNeighbours(x, y, grid) == 3:
                    setTileAlive(x, y, newgrid)  # Any live cell with two or three live neighbours survives.
                else:
                    setTileDead(x, y, newgrid)
            else:
                if countLiveNeighbours(x, y, grid) == 3:
                    setTileAlive(x, y, newgrid)  # Any dead cell with three live neighbours becomes a live cell.
                else:
                    setTileDead(x, y, newgrid)
    grid = newgrid


def setTileAlive(x, y, grid):
    grid[x][y] = 1


def setTileDead(x, y, grid):
    grid[x][y] = 0


def getTile(x, y, grid, grid_size_x, grid_size_y):
    if (x >= 0 and y >= 0 and x <= grid_size_x-1 and y <= grid_size_y-1):  # Checks to see if the co-ordinates are in the grid or not
        return grid[x][y]
    else:
        return 0


# Count live neighbours of the cell at x,y
def countLiveNeighbours(x, y, grid, grid_size_x, grid_size_y):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y:
                continue
            count += getTile(i, j, grid, grid_size_x, grid_size_y)
    return count

# print(generate(grid))
# is_alive(grid)
