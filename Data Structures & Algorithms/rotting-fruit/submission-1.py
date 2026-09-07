class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rot = deque()
        minutes = 0

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rot.append((r,c))

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while rot and fresh > 0:
            for i in range(len(rot)):
                r,c = rot.popleft()

                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    rot.append((nr,nc))
            minutes+=1

        return minutes if fresh == 0 else -1



