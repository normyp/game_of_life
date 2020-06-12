import model

cell = model.cell

grid = [[cell['status'],cell['status'],cell['status'],cell['status'],cell['status']],
        [cell['status'],cell['status'],cell['status'],cell['status'],cell['status']],
        [cell['status'],cell['status'],cell['status'],cell['status'],cell['status']]]
user_input = ""

"""for i in range(0, 5): #sets up grid
    for j in range(0, 5):
        grid.append(["0"])"""

grid[0][2] = 1
grid[1][2] = 1
grid[2][2] = 1

#while(user_input != 1):
for i in range(0, len(grid)): #prints grid
    print(grid[i])

model.generate(grid)

for i in range(0, len(grid)): #prints grid
    print(grid[i])

