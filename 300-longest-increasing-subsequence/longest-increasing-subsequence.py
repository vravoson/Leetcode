class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # optimal substructure: li[i]: longest increasing subseq.
        # if for subarray ending at index i
        n = len(nums)
        li = [1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    li[i] = max(li[i], li[j]+1)
        return max(li)
        