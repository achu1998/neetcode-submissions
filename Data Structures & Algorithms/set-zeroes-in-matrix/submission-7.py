class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        rowZero = False
        colZero = False

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    if c > 0: 
                        matrix[r][0] = 0
                    else:
                        colZero = True    
                    if r > 0:
                        matrix[0][c] = 0
                    else:
                        rowZero = True

        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if colZero:
            for r in range(row):
                matrix[r][0] = 0
                            
        if rowZero:
            for c in range(col):
                matrix[0][c] = 0                        

        