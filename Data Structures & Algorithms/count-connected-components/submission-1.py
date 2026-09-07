class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            visit.add(node)
            for neighbor in adj[node]:
                if neighbor not in visit:
                    
                    dfs(neighbor)


        visit = set()
        components = 0
        for course in range(n):
            if course not in visit:
                dfs(course)
                components += 1

        return components
