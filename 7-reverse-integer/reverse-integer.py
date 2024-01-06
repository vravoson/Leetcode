class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            res = -int(''.join(list(str(x))[1:][::-1]))
            if res < -2**31:
                return 0
            return res
        res =  int(''.join(list(str(x))[::-1]))
        if res > 2**31-1:
            return 0
        return res