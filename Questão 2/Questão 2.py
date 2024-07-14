class Solution:
    def areConnected(self, N: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        if threshold == 0:
            return [True] * len(queries)
        
        par = [x for x in range(N + 1)]

        def ufind(x):
            if x != par[x]:
                par[x] = ufind(par[x])
            return par[x]
        
        def unnion(a, b):
            pa = ufind(a)
            pb = ufind(b)
            par[pa] = pb

        for x in range(threshold + 1, N + 1):
            k = x
            while k <= N:
                unnion(x, k)
                k += x

        return [ufind(a) == ufind(b) for a, b in queries]
