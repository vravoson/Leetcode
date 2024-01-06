class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zeros = 0
        if 0 in nums:
            nums2 = nums.copy()
            nums2.remove(0)
            if 0 in nums2:
                count_zeros = 2
            else:
                count_zeros = 1
        if count_zeros == 2:
            return [0]*len(nums)
        elif count_zeros == 1:
            prod = 1
            for elem in nums2:
                prod *= elem
            return [0 if x!= 0 else int(prod) for x in nums]
        if count_zeros == 0:
            prod = 1
            for elem in nums:
                prod *= int(elem)
            return [int(prod/num) for num in nums]