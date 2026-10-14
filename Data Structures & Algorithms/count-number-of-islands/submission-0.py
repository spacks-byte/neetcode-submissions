class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        total = 0

        yMax = len(grid)-1
        xMax = len(grid[0])-1

        def dfs(x, y):
            grid[y][x] = "0"
            if y > 0:
                if grid[y-1][x] == "1":
                    dfs(x, y-1)
            if y < yMax:
                if grid[y+1][x] == "1":
                    dfs(x, y+1)
            if x > 0:
                if grid[y][x-1] == "1":
                    dfs(x-1, y)
            if x < xMax:
                if grid[y][x+1] == "1":
                    dfs(x+1, y)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    total += 1
                    dfs(x, y)

        return total