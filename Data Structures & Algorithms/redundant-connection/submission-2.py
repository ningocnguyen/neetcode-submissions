class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges)+1)]

        # find parents of x
        def find(x):
            while parents[x] != x:
                x = parents[x]
            return x

        # union merge parent of node1 -> node2
        def union(node1, node2):
            root_x = find(node1)
            root_y = find(node2)

            if root_x == root_y:
                return False
            else:
                parents[root_x] = root_y
                return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]