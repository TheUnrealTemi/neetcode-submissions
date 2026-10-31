class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        rowBeg, rowEnd = 0, len(matrix) -1 
        colBeg, colEnd = 0, len(matrix[0]) - 1

        while rowBeg <= rowEnd and colBeg <= colEnd:
            for i in range(colBeg, colEnd+1):
                res.append(matrix[rowBeg][i])
            rowBeg += 1
            for i in range(rowBeg, rowEnd+1):
                res.append(matrix[i][colEnd])
            colEnd -= 1

            if rowBeg <= rowEnd:
                for i in range(colEnd, colBeg - 1, -1):
                    res.append(matrix[rowEnd][i])
                rowEnd -= 1
            if colBeg <= colEnd:
                for i in range(rowEnd, rowBeg -1, -1):
                    res.append(matrix[i][colBeg])
                colBeg += 1 


        return res