class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        yMax = len(board)
        xMax = len(board[0])

        def dfs(x, y, board):
            board[y][x] = "E"

            if y > 0:
                if board[y-1][x] == "O":
                    dfs(x, y-1, board)
            if y < yMax-1:
                if board[y+1][x] == "O":
                    dfs(x, y+1, board)
            if x > 0:
                if board[y][x-1] == "O":
                    dfs(x-1, y, board)
            if x < xMax-1:
                if board[y][x+1] == "O":
                    dfs(x+1, y, board)
            return

        for y in range(yMax):
            for x in range(xMax):
                if (y==0 or y==(yMax-1) or x==0 or x==(xMax-1)) and board[y][x] == "O":
                    dfs(x,y, board)

        for y in range(yMax):
            for x in range(xMax):
                if board[y][x] == "O":
                    board[y][x] = "X"
                elif board[y][x] == "E":
                    board[y][x] = "O"
