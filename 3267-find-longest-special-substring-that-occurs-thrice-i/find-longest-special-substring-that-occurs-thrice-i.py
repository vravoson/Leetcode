class Solution:
    def maximumLength(self, s: str) -> int:
        def find_overlaps(string, substring):
            count = start = 0
            while True:
                start = string.find(substring, start)
                if start == -1: 
                    return count
                count += 1
                start += 1 
                
        n = len(s)
        subs = set()
        for i in range(n):
            for j in range(i+1, n+1):
                w = s[i:j]
                if len(set(w)) == 1:
                    subs.add(w)

        res = -1
        for sub in subs:
            print(s, sub, find_overlaps(s, sub))
            if find_overlaps(s, sub) >= 3:
                res = max(res, len(sub))
                
        return res