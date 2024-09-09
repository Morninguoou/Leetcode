class Solution(object):
    def searchMatrix(self, matrix, target):
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if  matrix[r][c] == target:
                    return True
        return False