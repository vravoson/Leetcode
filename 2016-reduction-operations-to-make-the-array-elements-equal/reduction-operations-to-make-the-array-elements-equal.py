class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        occ = dict(Counter(nums))
        vals = sorted(occ.keys())
        return sum([k*occ[vals[k]] for k in range(len(vals))])