class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        res = "1"

        for i in range(n-1):
            new_res = ''
            count = 0
            l = len(res)
            ind = 0
            number = res[0]
            while ind < l:
                if res[ind] != number:
                    new_res += f"{count}{number}"
                    count = 1
                    number = res[ind]
                elif res[ind] == number:
                    count += 1
                ind += 1
            if count == 0:
                new_res += f"{count+1}{number}"
            else:
                new_res += f"{count}{number}"
            res = new_res
        
        return res

