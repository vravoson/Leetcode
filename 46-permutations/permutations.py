class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 1:
            return [nums]
        
        def perm_rec(nums, acc):
            
            if len(nums) == 0:
                return acc
            

            last_elem = nums.pop()
            n = len(acc)
            to_append = []
            for li in acc:
                n = len(li)
                for i in range(n+1):
                    perm = li[:i] + [last_elem] + li[i:]
                    to_append.append(perm)

            return perm_rec(nums, to_append)
        
        return perm_rec(nums[1:], [[nums[0]]])
