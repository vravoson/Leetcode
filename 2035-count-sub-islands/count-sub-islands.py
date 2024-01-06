class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid1), len(grid1[0])
        
        def mask_island(x,y, mask):
            if x >= 0 and x < n and y >= 0 and y < m:
                if grid2[x][y] == 1:
                    grid2[x][y] = mask
                    if grid1[x][y] == 1:
                        grid1[x][y] = mask
                    mask_island(x+1, y, mask)
                    mask_island(x-1, y, mask)
                    mask_island(x, y+1, mask)
                    mask_island(x, y-1, mask)
        
        def dico_mask(grid, mask_max):
            dico_out = dict(zip(range(2, mask_max), [0]*(mask_max-2)))
            for i in range(n):
                for j in range(m):
                    if grid[i][j] >= 2:
                        dico_out[grid[i][j]] += 1
            return dico_out
                
        res = 0
        mask = 2
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1 and grid1[i][j] == 1:
                    mask_island(i,j, mask)
                    mask += 1
        
        dico_g1 = dico_mask(grid1, mask)
        dico_g2 = dico_mask(grid2, mask)

        for key,_ in dico_g1.items():
            if dico_g1[key] == dico_g2[key] and dico_g1[key] > 0:
                res += 1

        return res
        


