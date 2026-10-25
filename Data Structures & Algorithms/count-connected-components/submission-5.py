class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build adjacency list of undirected graph
        # visit set and count = 0
        # iterate thru every node
        # if node not in visit: run dfs and mark the component as visit, increment count
        # return count
        count = 0
        visit = set()
        graph = {i: [] for i in range(n)}
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        def dfs(node):
            visit.add(node)
            for nei in graph[node]:
                if nei not in visit:
                    dfs(nei)
            
        for node in range(n):
            if node not in visit:
                dfs(node)
                count+=1

        return count

