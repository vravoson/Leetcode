class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        i = 0
        while i < n - 2:
			# we check this condition so that we dont get same triplets twice
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                lo = i + 1
                hi = n - 1

                while lo < hi:
                    if nums[lo] + nums[hi] == -nums[i]:
                        ans += [nums[i], nums[lo], nums[hi]],
						# increment lo till we get different element so as to not get same triplet twice
                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
						# decrement hi till we get different element so as to not get same triplet twice
                        while lo < hi and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < -nums[i]:
                        lo += 1
                    else:
                        hi -= 1
            i += 1

        return ans