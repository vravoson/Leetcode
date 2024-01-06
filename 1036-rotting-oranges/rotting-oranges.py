class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        def count_orange(grid):
            output = [0]*3
            for i in range(n):
                for j in range(m):
                    output[grid[i][j]] += 1
            return output
        
        count_init = count_orange(grid)
        
        if count_init[1] == 0:
            return 0
        elif count_init[2] == 0 and count_init[1] > 0:
            return -1
        else:
            step = 0
            list_rotten = set()
            list_fresh = set()
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 2:
                        list_rotten.add((i,j))
                    if grid[i][j] == 1:
                        list_fresh.add((i,j))
                    
            
            iternum = 0
            while len(list_fresh)>0 and iternum <= n*m:
                step += 1
                iternum += 1
                to_delete = set()
                to_add = set()
                for elem in list_fresh:
                    i,j = elem[0], elem[1]
                    if (i+1,j) in list_rotten:
                        to_add.add((i,j))
                        to_delete.add((i,j))
                    elif (i-1,j) in list_rotten:
                        to_add.add((i,j))
                        to_delete.add((i,j))
                    elif (i,j+1) in list_rotten:
                        to_add.add((i,j))
                        to_delete.add((i,j))
                    elif (i,j-1) in list_rotten:
                        to_add.add((i,j))
                        to_delete.add((i,j))
                if len(to_delete) == 0:
                    return -1
                for item in to_delete:
                    list_fresh.remove(item)
                for item in to_add:
                    list_rotten.add(item)
            if iternum == n*m:
                return -1
            return step
            
                    

            
            
            
            
        