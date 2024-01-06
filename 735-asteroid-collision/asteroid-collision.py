class Solution:
    def asteroidCollision(self, li: List[int]) -> List[int]:
        def process_time(li):
            n = len(li)
            if n <= 1:
                return li
            new_li = []
            i = 0
            while i < n:
                if i== n-1:
                    new_li.append(li[i])
                    i+=1
                elif li[i]>0 and li[i+1] < 0:
                    if abs(li[i]) > abs(li[i+1]):
                        new_li.append(li[i])
                    elif abs(li[i]) < abs(li[i+1]):
                        new_li.append(li[i+1])
                    i+=2
                else:
                    new_li.append(li[i])
                    i+=1
            
            return new_li

        while li != process_time(li):
            li =  process_time(li)
        
        return li
            
        