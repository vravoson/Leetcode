class Solution:
    def calculate(self, s: str) -> int:
        if  not( '*' in s or '+' in s or '-' in s or '/' in s):
            return int(s)
        s = s.replace(' ','')
        n = len(s)
        s_list = []
        ind_prev = 0
        ind_curr = ind_prev+1
        
        while ind_curr < n:
            if s[ind_curr] in "+-*/":
                s_list.append(s[ind_prev : ind_curr])
                s_list.append(s[ind_curr])
                ind_prev = ind_curr+1
            if ind_curr == n-1:
                s_list.append(s[ind_prev:])
            ind_curr += 1


        m = len(s_list)
        s_list = [int(x) if not(x in "+-*/") else x for x in s_list]
        

        while '*' in s_list or '/' in s_list:
            ind = 0
            seen = False
            while ind < len(s_list) and not(seen):
                if str(s_list[ind]) in '*/':
                    seen = True
                    if s_list[ind] == "*":
                        to_add = s_list[ind-1] * s_list[ind+1]
                    else:
                        to_add = s_list[ind-1] // s_list[ind+1]
                    
                    s_list.pop(ind-1)
                    s_list.pop(ind-1)
                    s_list.pop(ind-1)
                    s_list.insert(ind-1, to_add)
            
                ind+=1
        
        if len(s_list) == 1:
            return int(s_list[0])
        
        res = s_list[0]
        ind = 1
        m = len(s_list)
        
        while ind < m:
            if s_list[ind] == '+':
                res += s_list[ind+1]
            elif s_list[ind] == '-':
                res -= s_list[ind+1]
            ind+=2
            
        return int(res)

        
