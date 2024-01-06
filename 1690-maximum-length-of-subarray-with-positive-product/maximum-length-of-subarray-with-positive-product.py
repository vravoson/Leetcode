class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def sign(x): return 1 if x > 0 else 2 if x < 0 else 0
        def process_str(s):
            l = len(s)
            nb_neg = s.count('2')
            if nb_neg % 2 == 0:
                return l
            if nb_neg == 1:
                pos_neg = s.find('2')
                return max(max(pos_neg-1,0)+1, 
                            l-min(pos_neg+1, l-1))
            else:
                left_pos, right_pos = s.find('2'), l-1-s[::-1].find('2')
                return max(l-min(left_pos+1, l-1),
                           max(0, right_pos-1) + 1)
            
        if set(nums) == {0}: return 0
        if len(nums) == 1: return 1 if nums[0]>0 else 0
        nums = list(map(sign, nums))
        nums = "".join(map(str, nums)).split('0')
        print(nums)
        max_length = max(map(process_str, nums))
        return max_length


        