class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)

        nums_bin = [bin(x).replace('0b', '') for x in nums]
        nums_bin = ['0'*(32-len(y)) + y for y in nums_bin]

        res = 0

        for i in range(32):
            bit_val = [x[i] for x in nums_bin]
            nb_ones = len([y for y in bit_val if y == '1'])
            res += nb_ones * (n - nb_ones)
        
        return res