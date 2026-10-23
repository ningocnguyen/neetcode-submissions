class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # initiate 2 visit set that can flow to ocean for both pac and atl
        # run dfs traverse from top and left for pac:
        # if the cell > previous visited cell -> then add to pac
        # run dfs traverse from bottom and right for atl:
        # if the cell > previous visited cell -> then add to atl
        # if a cell in both pac and atl --> result

        pac = set()
        atl = set()
        rows, cols = len(heights), len(heights[0])
        res = []

        def dfs(r,c,ocean,prev):
            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in ocean or heights[r][c] < prev:
                return
            ocean.add((r,c))
            # traverse up, down, left, or right
            dfs(r+1,c,ocean,heights[r][c])
            dfs(r-1,c,ocean,heights[r][c])
            dfs(r,c+1,ocean,heights[r][c])
            dfs(r,c-1,ocean,heights[r][c])

        
        # pac top & atl bottom
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])

        # pac left and atl right
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))

        return res




