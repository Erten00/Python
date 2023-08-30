import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

grid_size = (50, 50)

grid = np.random.choice([0, 1], size=grid_size)

def update(frameNum, img, grid, grid_size):
    new_grid = grid.copy()

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):

            neighbors_sum = int(np.sum(grid[max(0, i-1):min(grid_size[0], i+2), max(0, j-1):min(grid_size[1], j+2)])) - grid[i, j]
            
            if grid[i, j] == 1 and (neighbors_sum < 2 or neighbors_sum > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors_sum == 3:
                new_grid[i, j] = 1
    
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='gray')

ani = animation.FuncAnimation(fig, update, fargs=(img, grid, grid_size), frames=100, interval=200, save_count=50)

plt.show()