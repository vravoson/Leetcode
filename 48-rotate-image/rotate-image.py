class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        set_seen = set()
        m = len(matrix)
        for i in range(m):
            for j in range(m):
                if not((i,j) in set_seen) and not((j,m-1-i) in set_seen) and not((m-i-1, m-j-1) in set_seen) and not((m-j-1, i) in set_seen):

                    (matrix[i][j],
                    matrix[j][m-i-1],
                    matrix[m-i-1][m-j-1],
                    matrix[m-j-1][i]
                    ) = (
                    matrix[j][m-i-1],
                    matrix[m-i-1][m-j-1],
                    matrix[m-j-1][i],
                    matrix[i][j])
                    
                    set_seen.add((i,j))
                    set_seen.add((j,m-1-i))
                    set_seen.add((m-i-1, m-j-1))
                    set_seen.add((m-j-1, i))
        del set_seen
        matrix_2 = [x[::-1] for x in matrix[::-1]]
        for i in range(m):
            for j in range(m):
                matrix[i][j] = matrix_2[i][j]
        return matrix
        