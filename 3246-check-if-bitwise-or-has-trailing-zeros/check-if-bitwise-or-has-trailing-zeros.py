class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        for i in range(n-1):
            for j in range(i+1,n):
                bit_or = bin(nums[i]|nums[j])[-1]
                if bit_or == '0':
                    print(bin(nums[i]|nums[j]))
                    return True
        return False
        