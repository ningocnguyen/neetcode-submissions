class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # visit set to tract visited nodes
        # count to track # of components
        # iterate thru every node
        # if node not in visit dfs for each components and find all connected nodes -> mark as visited
        # increment count 
        # return count

        count = 0
        visit = set()

        graph = {i: [] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in graph[node]:
                if nei not in visit:
                    dfs(nei)

        for i in range(n):
            if i not in visit:
                dfs(i)
                count+=1

        return count

            
            

