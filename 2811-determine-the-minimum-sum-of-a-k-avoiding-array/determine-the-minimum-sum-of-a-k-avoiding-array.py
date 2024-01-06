class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        
        def complete_set(s, max_elem, k):
            if max_elem >= k:
                return max_elem + 1 # new elem to add, new max_elem
            
            max_elem += 1
            while k - max_elem>0 and k-max_elem in s:
                max_elem += 1
            
            return max_elem
        
        if n == 1:
            return 1
        
        if k == 1:
            return (n+1)*n//2
        
        res = 1
        s = set([1])
        max_elem = 1
        
        for i in range(n-1):
            max_elem = complete_set(s, max_elem, k)
            s.add(max_elem)
            
        return sum(s)
        
        
        