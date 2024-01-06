class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 1 if nums[0] == target else 0
        res = 0
        hash_table = {0}
        cum_sum = 0
        for i in range(n):
            cum_sum += nums[i]
            if cum_sum - target in hash_table:
                res += 1
                hash_table = {0}
                cum_sum = 0
            else:
                hash_table.add(cum_sum)
        return res

        