class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in visit or board[r][c] != word[i]:
                return False
            visit.add((r,c))
            res = (dfs(r+1,c,i+1)
            or dfs(r,c+1,i+1)
            or dfs(r-1,c,i+1)
            or dfs(r,c-1,i+1))
            visit.remove((r,c))
            return res

        visit = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False