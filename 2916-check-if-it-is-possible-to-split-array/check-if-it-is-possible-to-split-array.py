class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)

        if n in {1,2}:
            return True

        def check_split(li):
            return len(li) == 1 or sum(li) >= m

        memo = {}

        def split_rec(li):
            nn = len(li)

            if nn in {1, 2}:
                return True

            if li in memo:
                return memo[li]

            for i in range(1, nn):
                left, right = li[:i], li[i:]
                if check_split(left) and check_split(right):
                    if split_rec(left) and split_rec(right):
                        memo[li] = True
                        return True

            memo[li] = False
            return False

        return split_rec(tuple(nums))
                
                
                
                
                