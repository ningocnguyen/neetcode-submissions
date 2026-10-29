class Solution:

  def closedIsland(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    edges = set()
    count = 0

    for c in range(cols):
      edges.add((0, c))
      edges.add((rows - 1, c))
    for r in range(rows):
      edges.add((r, 0))
      edges.add((r, cols - 1))

    visit = set()

    for r in range(1, rows - 1):
      for c in range(1, cols - 1):
        if grid[r][c] == 0 and (r, c) not in visit:
          is_closed = True
          stack = [(r, c)]
          visit.add((r, c))

          while stack:
            curr_r, curr_c = stack.pop()

            if (curr_r, curr_c) in edges:
              is_closed = False

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
              nr, nc = curr_r + dr, curr_c + dc
              if (
                  0 <= nr < rows
                  and 0 <= nc < cols
                  and grid[nr][nc] == 0
                  and (nr, nc) not in visit
              ):
                visit.add((nr, nc))
                stack.append((nr, nc))

          if is_closed:
            count += 1

    return count