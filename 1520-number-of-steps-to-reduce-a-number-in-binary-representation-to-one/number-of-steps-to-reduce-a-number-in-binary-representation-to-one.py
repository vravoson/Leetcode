class Solution:
    def numSteps(self, s: str) -> int:
        n = sum([2**i*int(d) for i,d in enumerate(s[::-1])])
        res = 0
        while n != 1:
            if n%2 == 1:
                n += 1
            else:
                n //=2
            res += 1
        return res
        

        