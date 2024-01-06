class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        res = [nums[0]]*n
        for i in range(1,n):
            res[i] = max(res[i-1]+nums[i], nums[i])
        return max(res)