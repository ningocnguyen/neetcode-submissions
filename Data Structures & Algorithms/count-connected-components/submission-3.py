class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        res = 0

        def dfs(node):
            visit.add(node)
            for neighbor in adj[node]:
                if neighbor not in visit:
                    dfs(neighbor)

        visit = set()

        for node in range(n):
            if node not in visit:
                dfs(node)
                res+=1

        return res



