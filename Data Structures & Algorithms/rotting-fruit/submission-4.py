class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        fresh = 0

        # rot until fresh = 0 and not q
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while fresh > 0 and q:
            minutes += 1
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr = dr+r
                    nc = dc+c
                    if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -=1
                    q.append((nr,nc))

        return minutes if fresh == 0 else -1

        


