class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check if graph has exactly n-1 edges
        # build an adjacency list of undirected edges
        # run dfs starting from node 0
        # visit set to detect cycle
        # return len(visited) == n
        if len(edges) != n - 1:
            return False
        graph = [[] for i in range(n)]
        # Undirected prah: connect both directions
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        visited = set()
        
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        dfs(0)
        return len(visited) == n
