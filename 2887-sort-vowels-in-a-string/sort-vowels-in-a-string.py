class Solution:
    def sortVowels(self, s: str) -> str:
        voy = [l for l in s if l.lower() in 'aeiou']
        voy = sorted(voy, key = lambda s: -sum(map(ord, s)), reverse=True)
        i, n = 0, len(s)
        while i<n:
            if s[i] not in 'aeiouAEIOU':
                voy.insert(i, s[i])
            i+=1
        return "".join(voy)
        