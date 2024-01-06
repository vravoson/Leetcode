class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        sort_nums = sorted(nums)
        res = []
        for i in range(n//2+1):
            if i< n-1-i:
                res.append(sort_nums[i])
                res.append(sort_nums[n-1-i])
            elif i == n-1-i:
                res.append(sort_nums[i])
        return res
        
        