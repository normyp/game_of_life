# Any live cell with two or three live neighbours survives.
# grid of 0's and 1's to represent dead or alive cells

cell = {
    "status": '0',
    "cell_neighbours": 3
}
grid = [[cell["status"],0,0],[0,0,0],[0,0,0]]

def generate(grid):
    return [[0,1,0],[0,1,0],[0,1,0]]

def is_alive(cell):
    if cell['status'] == '1':
        if cell["cell_neighbours"] == 2 or cell["cell_neighbours"] == 3:
            cell['status'] = '1'  # Any live cell with two or three live neighbours survives.
        else:
            cell['status'] = '0'
    else:
        if cell["cell_neighbours"] == 3:
            cell['status'] = '1' # Any dead cell with three live neighbours becomes a live cell.
        else:
            cell['status'] = '0'

print(generate(grid))
is_alive(grid)
