class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows,cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r<0 or c<0 or c>=cols or r>=rows or grid[r][c]=='0':
                return
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    islands+=1
                    
        return islands 
            
