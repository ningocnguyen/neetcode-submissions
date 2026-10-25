class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # check if graph has exactly n-1 edges
        # build an adjacency list of undirected edges
        # run dfs starting from node 0
        # visit set to detect cycle
        # have a prev node to track if its the previous visited to we can skip without return false
        # return len(visited) == n
        if len(edges) != n - 1:
            return False
        graph = {i: [] for i in range(n)}
        # Undirected path: connect both directions
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        visited = set()
        
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
        
        return len(visited) == n