class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            print(i)
            if nums[i] <= nums[(i-1) % n] and nums[i] <= nums[(i+1) % n]:
                return nums[i]