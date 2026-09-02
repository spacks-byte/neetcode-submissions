import itertools
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            numbersInRow = list(filter(lambda x : x != '.', row))
            if len(set(numbersInRow)) < len(numbersInRow):
                return False
        for column in list(zip(*board)):
            numbersInCol = list(filter(lambda x : x != '.', column))
            if len(set(numbersInCol)) < len(numbersInCol):
                return False

        for boxH in range(3):
            for boxV in range(3):
                x = boxH * 3
                y = boxV * 3
                minibox = [row[x:x+3] for row in board[y:y+3]]
                boxNumbers = list(filter(lambda x : x != '.', list(itertools.chain.from_iterable(minibox))))
                if len(set(boxNumbers)) < len(boxNumbers):
                    return False

        
        return True


        
        