class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def eratosthenes_sieve(n):
            prime, result, sqrt_n = [True] * n, [2], (int(n ** .5) + 1) | 1
            for p in range(3, sqrt_n, 2):
                if prime[p]:
                    result.append(p)
                    prime[p * p::p << 1] = [False] * ((n - p * p - 1) // (p << 1) + 1)

            return result + [p for p in range(sqrt_n, n, 2) if prime[p]]
    

        primes = eratosthenes_sieve(n + 1)
        result = []
    
        dico_seen = {}
        for elem in primes:
            if elem*2 == n:
                result.append([elem, elem])
            else:
                if not(elem in dico_seen):
                    dico_seen[n-elem] = elem
                else:
                    x,y = elem, dico_seen[elem]
                    if x<=y:
                        result.append([x,y])
                    else:
                        result.append([y,x])


        return sorted(list(set(map(tuple,result))))
     
        
