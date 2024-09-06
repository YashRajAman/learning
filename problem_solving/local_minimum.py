grid = [
    [1, 2, 1],
    [2, 1, 2],
    [1, 2, 1]
]

grid = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

def numCells(grid):

    cells = 0
    rows = len(grid)
    cols = len(grid[0])
    counter = 0
    for x in range(rows):
        for y in range(cols):
            truce = []
            counter += 1
            self = grid[x][y]
            
            ulimit = [[x-1 if x > 0 else x],[y-1 if y > 0 else 0, y+1 if y==0 else y+3]]
            blimit = [[x+1 if x<rows-1 else x],[y-1 if y > 0 else 0, y+1 if y==0 else y+3]]
            slimit = [[x],[y-1 if y > 0 else 0, y+1 if y==0 else y+3]]

            upper_values = grid[x-1 if x > 0 else x][y-1 if y > 0 else 0: y+2 if y==0 else y+3] if x>0 else [self]
            bottom_values = grid[x+1 if x<rows-1 else x][y-1 if y > 0 else 0: y+2 if y==0 else y+3] if x<rows-1 else [self]
            self_values = grid[x][y-1 if y > 0 else 0: y+2 if y==0 else y+3]


            if min(upper_values) < self:
                truce.append(False)

            if min(bottom_values) < self:
                truce.append(False)

            if min(self_values) < self:
                truce.append(False)


            # if self-1 in upper_values:
            #     truce.append(False)
            
            # if self-1 in bottom_values:
            #     truce.append(False)

            # if self-1 in self_values:
            #     truce.append(False)

            print(f"{self} -> {upper_values}, {self_values}, {bottom_values}, {truce}")
            if truce==[False, False, False]:
                cells += 1
    print(counter)
    return cells

print(numCells(grid))

            