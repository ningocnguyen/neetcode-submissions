class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid: 
            # no cycle
            # no isolated components

        adj = {i: [] for i in range(n)}
        for u,v in edges:
            adj[v].append(u)
            adj[u].append(v)

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

        return len(visit) == n # confirm all nodes are reached
        