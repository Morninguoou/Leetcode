class Solution:
    def spiralOrder(self, matrix):
        res = []
        if len(matrix) == 0:
            return res
        row = 0
        col = 0
        row_end = len(matrix)-1 
        col_end = len(matrix[0])-1
        while (row <= row_end and col <= col_end):
            for i in range(col,col_end+1):
                res.append(matrix[row][i])
            row += 1
            for i in range(row,row_end+1):
                res.append(matrix[i][col_end])
            col_end -= 1
            if (row <= row_end):
                for i in range(col_end,col-1,-1):
                    res.append(matrix[row_end][i])
                row_end -= 1
            if (col <= col_end):
                for i in range(row_end,row-1,-1):
                    res.append(matrix[i][col])
                col += 1
        return res