class UnionFind:
    def __init__(self, N):
        self.parents = list(range(N))

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])  # Path compression
        return self.parents[x]
    
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.parents[rootB] = rootA

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, N: int, edges: List[List[int]]) -> List[List[int]]:
        E = len(edges)
        e = sorted(enumerate(edges), key=lambda x: x[1][2])

        def mst(exclude_index=None, include_index=None):
            uf = UnionFind(N)
            total = 0
            edges_used = 0

            if include_index is not None:
                u, v, w = edges[include_index]
                uf.union(u, v)
                total += w
                edges_used += 1
            
            for index, (u, v, w) in e:
                if index == exclude_index:
                    continue
                
                if uf.find(u) != uf.find(v):
                    uf.union(u, v)
                    total += w
                    edges_used += 1

                    if edges_used == N - 1:
                        break

            if edges_used == N - 1:
                return total
            else:
                return float('inf')

        base_mst = mst()
        critical = []
        pseudocritical = []

        for i in range(E):
            if mst(exclude_index=i) > base_mst:
                critical.append(i)
            elif mst(include_index=i) == base_mst:
                pseudocritical.append(i)

        return [critical, pseudocritical]
