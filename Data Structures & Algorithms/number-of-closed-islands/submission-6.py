class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # eliminate all cells connected to border --> dfs to turn all to 1
        # iterate thru each cell in board (excluding border):
        # if still 0: count of closed islands += 1, dfs for neighboring
        # return count

        closed_count = 0
        rows, cols = len(grid), len(grid[0])

        # eliminate all cells connected to border --> dfs to turn all to 1
        def bfs(start_r,start_c):
            stack = [(start_r,start_c)]
            grid[start_r][start_c] = 1
            while stack:
                r, c = stack.pop()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr=dr+r
                    nc=dc+c
                    if nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc] == 1:
                        continue
                    grid[nr][nc] = 1
                    stack.append((nr,nc))
            
        for r in range(rows):
            for c in range(cols):
                if ((r == 0 or r == rows - 1 or c == 0 or c == cols - 1)and grid[r][c] == 0):
                    bfs(r,c)
        
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if grid[r][c] == 0:
                    closed_count+=1
                    bfs(r,c)

        return closed_count
