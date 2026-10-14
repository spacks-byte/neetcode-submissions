class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        if not grid:
            return -1

        yLen = len(grid)
        xLen = len(grid[0])
        time = 0
        queue = deque()
        bananas = 0
        
        for y in range(yLen):
            for x in range(xLen):
                if grid[y][x] == 2:
                    queue.append((y,x))
                elif grid[y][x] == 1:
                    bananas += 1
                    
        row = 0
        col = 0
        while queue:
            row, col = queue.popleft()
            if max(time, grid[row][col]) > 2:
                time = max(time, grid[row][col])
            
            if col < (xLen-1):
                if grid[row][col+1] == 1:
                    grid[row][col+1] = grid[row][col] + 1
                    bananas -= 1
                    queue.append((row,col+1))
            if col > 0:
                if grid[row][col-1] == 1:
                    grid[row][col-1] = grid[row][col] + 1
                    bananas -= 1
                    queue.append((row,col-1))
            if row < (yLen-1):
                if grid[row+1][col] == 1:
                    grid[row+1][col] = grid[row][col] + 1
                    bananas -= 1
                    queue.append((row+1,col))
            if row > 0:
                if grid[row-1][col] == 1:
                    grid[row-1][col] = grid[row][col] + 1
                    bananas -= 1
                    queue.append((row-1,col))
        if bananas:
            return -1
        return time - 2 if time else 0