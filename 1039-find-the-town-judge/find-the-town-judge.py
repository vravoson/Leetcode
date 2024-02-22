class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1
        dico_trust = defaultdict(lambda: [0,0]) # trusts, trusted by
        for i in range(len(trust)):
            a,b = trust[i][0]-1, trust[i][1]-1
            dico_trust[a][0] += 1
            dico_trust[b][1] += 1
        judges = []
        for ppl, trust_list in dico_trust.items():
            if trust_list == [0, n-1]:
                judges.append(ppl)
        if len(judges) == 0 or len(judges) > 1:
            return -1
        return judges[0]+1
        
        