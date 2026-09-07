class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for neighbor in adj[node]:
                if prev == neighbor:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
        
        return len(visit) == n

            
            
