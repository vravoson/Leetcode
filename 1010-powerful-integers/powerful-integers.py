import numpy as np
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
      #  2M^i <= bound  log(bound/2)/log(M)

        if bound == 0:
            return []
        
        if (x,y) == (1,1):
            if bound < 2:
                return []
            return [2]
        
        seen = set()

        M = min(x,y)

        if M == 1:
            n_max = 1 + int(log(bound - 1)/log(max(x,y)))
        else:
            n_max = 1 + int(np.log(bound/2)/np.log(M))

        for i in range(n_max + 1):
            for j in range(n_max + 1):
                power = x**i + y**j
                if power <= bound:
                    seen.add(power)
        
        return list(seen)
