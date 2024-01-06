class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0
        
        if len(s) >= 2 and s[-1] == '0' and int(s[-2:]) > 26:
            return 0

        @lru_cache
        def dp_num(s):
            n = len(s)
            if s[0] == '0':
                return 0

            if n == 1:
                return 1

            if n == 2:
                if s in ['10', '20']:
                    return 1
                elif int(s) not in range(10,27):
                    return 1
                else:
                    return 2

            if int(s[:2]) not in range(10,27):
                return dp_num(s[1:])
            
            return dp_num(s[1:]) + dp_num(s[2:])
        
        return dp_num(s)

