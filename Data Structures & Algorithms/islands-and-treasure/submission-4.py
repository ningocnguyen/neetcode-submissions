class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        t = deque()

        # find all treasures and put in queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    t.append((r,c))

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        while t:
            r,c = t.popleft()
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                if nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = 1 + grid[r][c]
                t.append((nr,nc))


                
            
