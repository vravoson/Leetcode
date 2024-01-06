class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ones_row = [sum(x) for x in grid]
        ones_col = [sum([grid[i][j] for i in range(m)]) for j in range(n)]
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = 2*(ones_row[i] + ones_col[j]) - m - n
        return res
        