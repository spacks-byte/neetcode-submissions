class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        total = 0

        yMax = len(grid)-1
        xMax = len(grid[0])-1

        def dfs(x, y) -> int:
            grid[y][x] = 0
            subTotal = 0
            if y > 0:
                if grid[y-1][x] == 1:
                    subTotal += dfs(x, y-1)
            if y < yMax:
                if grid[y+1][x] == 1:
                    subTotal += dfs(x, y+1)
            if x > 0:
                if grid[y][x-1] == 1:
                    subTotal += dfs(x-1, y)
            if x < xMax:
                if grid[y][x+1] == 1:
                    subTotal += dfs(x+1, y)
            return 1 + subTotal

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    total = max(total, dfs(x,y))

        return total