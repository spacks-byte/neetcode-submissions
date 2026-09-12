class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)
        indexRow = -1
        while left < right:
            middle = (left + right)//2
            if target > matrix[middle][-1]:
                left = middle + 1
            elif target < matrix[middle][0]:
                right = middle
            else:
                indexRow = middle
                break
        
        if indexRow == -1:
            return False
        
        left = 0
        right = len(matrix[indexRow])
        
        while left < right:
            middle = (left + right)//2
            if target == matrix[indexRow][middle]:
                return True
            elif target > matrix[indexRow][middle]:
                left = middle + 1
            else:
                right = middle
        
        return False