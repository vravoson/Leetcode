class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        eligible = []
        for row in bank:
            nb_ones = row.count('1')
            if nb_ones > 0:
                eligible.append(nb_ones)
        if len(eligible) == 1:
            return 0
        res = 0
        for i in range(len(eligible)-1):
            res += eligible[i] * eligible[i+1]
        return res
        
