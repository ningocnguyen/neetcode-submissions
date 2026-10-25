class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        graph = {i: [] for i in range(n)}
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visit = set()

        def dfs(node):
            if node in visit:
                return False
            visit.add(node)
            for nei in graph[node]:
                dfs(nei)
        
        for node in range(n):
            if node not in visit:
                dfs(node)
                count += 1
        
        return count
                
