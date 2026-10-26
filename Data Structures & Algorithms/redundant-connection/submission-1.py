class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # if 2 nodes have same root but connected -> redundant
        # parents list [0, 1, ..., n] parents[i] stores who node i points to: initially itself
        # [0, 2, 3, 4, 4]
        # iterate thru every edge
        # find parent and union-merge parent root
        # if see equal edge -> immediately return redundant connection

        parents = [i for i in range(len(edges)+1)]

        def find(x):
            while parents[x] != x:
                x = parents[x]
            return x

        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return False # --> already connected: cycle detected

            else:
                parents[root_u] = root_v # merge 2 roots
                return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []



