class Solution:
  def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
    n = len(edges)
    # parent[i] stores who node i points to. Initially each points to itself.
    parent = [i for i in range(n + 1)]

    # walk up the chain until finding the root leader
    def find(x: int) -> int:
      while parent[x] != x:
        x = parent[x]
      return x

    # try to merge groups; returns False if already in the same group
    def union(x: int, y: int) -> bool:
      root_x = find(x)
      root_y = find(y)

      if root_x == root_y:
        return False  # Already connected -> cycle detected!

      parent[root_x] = root_y  # Merge the two roots
      return True

    # Process each edge one by one
    for u, v in edges:
      if not union(u, v):
        return [u, v]

    return []