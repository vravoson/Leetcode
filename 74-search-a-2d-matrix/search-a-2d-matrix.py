class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        concat = []

        for i in range(n):
            concat += matrix[i]

        N = n*m
        
        if target == concat[N//2]:
            return True
        
        elif target < concat[N//2]:
            l,r = 0, N//2
        else:
            l,r = N//2, N-1
        
        while l<r:
            
            if r-l == 1:
                return concat[r] == target or concat[l] == target

            mid = (l+r)//2
            if target == concat[mid]:
                return True
            elif target < concat[mid]:
                l,r = l, mid
            else:
                l,r = mid, r
        
        return False


        
        
        
