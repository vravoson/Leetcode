class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = nums[-1]
        for i in range(len(nums)-1):
            res = min(res, abs(nums[i]-nums[i+1]))
        return res
        