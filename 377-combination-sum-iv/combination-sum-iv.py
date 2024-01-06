class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @lru_cache(maxsize=None)
        def dp(remaining):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0

            res = 0
            for num in nums:
                res += dp(remaining - num)

            return res

        return dp(target)

        