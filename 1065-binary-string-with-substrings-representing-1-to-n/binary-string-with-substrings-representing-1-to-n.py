class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1,n+1):
            bin_i = bin(i)[2:]
            if not(bin_i in s):
                return False
        return True
            
        