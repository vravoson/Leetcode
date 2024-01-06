class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:

        def is_unhappy(x,y,u,v):
            return rank_dico[(x,u)] < rank_dico[(x,y)] and rank_dico[(u,x)] < rank_dico[(u,v)]

        rank_dico = {}

        for i in range(n):
            for j in range(n-1):
                rank_dico[(i, preferences[i][j])] = j
        
        p = len(pairs)

        if p == 1:
            return 0
        
        seen = set()

        for i in range(p-1):
            for j in range(i+1, p):

                x,y = tuple(pairs[i])
                u,v = tuple(pairs[j])

                if x not in seen:
                    if is_unhappy(x,y,u,v) or is_unhappy(x,y,v,u):
                        seen.add(x)
                
                if y not in seen:
                    if is_unhappy(y,x,u,v) or is_unhappy(y,x,v,u):
                        seen.add(y)
                
                if u not in seen:
                    if is_unhappy(u,v,x,y) or is_unhappy(u,v,y,x):
                        seen.add(u)
                
                if v not in seen:
                    if is_unhappy(v,u,x,y) or is_unhappy(v,u,y,x):
                        seen.add(v)
        
        return len(seen)

                        