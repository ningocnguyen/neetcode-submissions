class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = r+dr
                nc = c+dc
                if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = 1 + grid[r][c]
                q.append((nr,nc))
