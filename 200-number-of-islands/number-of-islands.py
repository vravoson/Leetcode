class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        res = 0

        def dfs(i,j):
            if i>= 0 and j>= 0 and i<n and j<m:
                if grid[i][j] == '1':
                    grid[i][j] = '2'
                    dfs(i+1, j)
                    dfs(i-1, j)
                    dfs(i, j-1)
                    dfs(i, j+1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i,j)
        
        return res

        