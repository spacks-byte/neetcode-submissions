class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        if not grid:
            return

        yLen = len(grid)
        xLen = len(grid[0])
        queue = deque()

        for y in range(yLen):
            for x in range(xLen):
                if grid[y][x] == 0:
                    queue.append((y,x))
                    
        row = 0
        col = 0
        while queue:
            row, col = queue.popleft()
            
            if col < (xLen-1):
                if grid[row][col+1] > 0 and grid[row][col+1] == 2147483647:
                    grid[row][col+1] = grid[row][col] + 1
                    queue.append((row,col+1))
            if col > 0:
                if grid[row][col-1] > 0 and grid[row][col-1] == 2147483647:
                    grid[row][col-1] = grid[row][col] + 1
                    queue.append((row,col-1))
            if row < (yLen-1):
                if grid[row+1][col] > 0 and grid[row+1][col] == 2147483647:
                    grid[row+1][col] = grid[row][col] + 1
                    queue.append((row+1,col))
            if row > 0:
                if grid[row-1][col] > 0 and grid[row-1][col] == 2147483647:
                    grid[row-1][col] = grid[row][col] + 1
                    queue.append((row-1,col))

