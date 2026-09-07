class Solution(object):
    def pacificAtlantic(self, heights):
        pac, atl = set(), set()
        rows, cols = len(heights), len(heights[0])
        res = []

        def dfs(r,c,visit,prev_height):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visit or heights[r][c] < prev_height:
                return
            visit.add((r,c))
            dfs(r-1,c,visit,heights[r][c])
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])


        # traverse top and bottom
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])

        # traverse left and right
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res

        

