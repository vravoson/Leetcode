class Solution:
    def chalkReplacer(self, li: List[int], k: int) -> int:
        k %= sum(li)  
        for i, usage in enumerate(li):
            if k < usage:  # find the student where the chalk runs out
                return i
            k -= usage
        return 0
