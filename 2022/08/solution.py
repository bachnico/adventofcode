import numpy as np

file_handler = open("./input.txt")
input_raw = file_handler.read().splitlines()


input_numbers = [[*string] for string in input_raw]

grid = np.asarray(input_numbers, dtype=np.int32)
         
#################################
# Part 1
#################################

isVisible = np.full_like(grid, False, dtype="bool")

isVisible[:, 0] = True
isVisible[:, -1] = True
isVisible[0, :] = True
isVisible[-1, :] = True

for x in range(grid.shape[0]):
    for y in range(grid.shape[1]):
        top = np.max(grid[0:y, x], initial=0)
        bottom = np.max(grid[y+1:, x], initial=0)
        left = np.max(grid[y, 0:x], initial=0)
        right = np.max(grid[y, x+1:], initial=0)
        
        if left < grid[y,x] or right < grid[y,x] or top < grid[y,x] or bottom < grid[y,x]:
            isVisible[y,x] = True


print("Solution Part 1:", np.sum(np.sum(isVisible)))   

#################################
# Part 2
#################################

def countUntilLarger(list, value):
    count = 0
    for x in list:
        count += 1
        if x >= value:
            break
        
    return count

scenicScores = np.full_like(grid, 0)

for x in range(len(input_numbers)):
    for y in range(len(input_numbers[0])):
        top = countUntilLarger(np.flip(grid[0:y, x]), grid[y,x])
        bottom = countUntilLarger(grid[y+1:, x], grid[y,x])
        left = countUntilLarger(np.flip(grid[y, 0:x]), grid[y,x])
        right = countUntilLarger(grid[y, x+1:], grid[y,x])
        
        scenicScores[y,x] = top * bottom * left * right

print("Solution Part 2:", np.max(scenicScores))