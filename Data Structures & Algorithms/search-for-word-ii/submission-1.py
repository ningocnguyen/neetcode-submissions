class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = None

class Solution(object):
    def findWords(self, board, words):
        root = TrieNode()
        rows = len(board)
        cols = len(board[0])
        res = []

        for w in words:
            cur = root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = w

        def dfs(r,c,node):
            char = board[r][c]
            if char not in node.children:
                return
            cur = node.children[char]
            if cur.word:
                res.append(cur.word)
                cur.word = None

            board[r][c] = '#'

            for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr,nc,cur)
            
            if not cur.children:
                del node.children[char]

            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)
        
        return res
            

                

            


