class Solution:
    def findArray(self, pref: List[int]) -> List[int]:

        n = len(pref)

        if n == 1:
            return pref
        
        acc = pref[0]
        pref_bin = [bin(x).replace('0b', '') for x in pref]
        res = [pref[0]]
        
        for i in range(1, n):
            x = bin(acc).replace('0b', '')
            y = pref_bin[i]
        
            if len(x) > len(y):
                y = '0'*(len(x)-len(y)) + y
            elif len(x) < len(y):
                x = '0'*(len(y) - len(x)) + x
            
            l = len(x)
            
            to_add = ''

            for j in range(l):
                if x[j] == '0' and y[j] == '0':
                    to_add += '0'
                
                elif x[j] == '1' and y[j] == '0':
                    to_add += '1'
                
                elif x[j] == '0' and y[j] == '1':
                    to_add += '1'
                
                elif x[j] == '1' and y[j] == '1':
                    to_add += '0'
            
            dec_add = int(to_add, 2)
            res.append(dec_add)
            acc ^= dec_add

        return res