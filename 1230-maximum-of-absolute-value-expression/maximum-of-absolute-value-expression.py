class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # abs(a) + abs(b) = max(a+b, a-b, -a+b, -a-b)
        n = len(arr1)
        a_11 = max([arr1[i]+arr2[i]+i for i in range(n)]) +  max([-arr1[j]-arr2[j]-j for j in range(n)])
        a_12 = max([arr1[i]+arr2[i]-i for i in range(n)]) +  max([-arr1[j]-arr2[j]+j for j in range(n)])
        
        a_21 = max([-arr1[i]+arr2[i]+i for i in range(n)])+  max([arr1[j]-arr2[j]-j for j in range(n)])
        a_22 = max([-arr1[i]+arr2[i]-i for i in range(n)])+  max([arr1[j]-arr2[j]+j for j in range(n)])
        
        a_31 = max([arr1[i]-arr2[i]+i for i in range(n)]) +  max([-arr1[j]+arr2[j]-j for j in range(n)])
        a_32 = max([arr1[i]-arr2[i]-i for i in range(n)]) +  max([-arr1[j]+arr2[j]+j for j in range(n)])
        
        a_41 = max([-arr1[i]-arr2[i]+i for i in range(n)]) +  max([arr1[j]+arr2[j]-j for j in range(n)])
        a_42 = max([-arr1[i]-arr2[i]-i for i in range(n)]) +  max([arr1[j]+arr2[j]+j for j in range(n)])
        
        return max(a_11, a_12, a_21, a_22, a_31, a_32, a_41, a_42)