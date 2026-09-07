class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        root = TrieNode()
        res = []

        for w in words:
            cur = root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur= cur.children[c]
            cur.word = w

        def dfs(r,c,node):
            char = board[r][c]

            if char not in node.children:
                return
            
            cur = node.children[char]
            if cur.word:
                res.append(cur.word)
                cur.word = None
            
            board[r][c]= '#'

            for dr, dc in [(0,1), (0,-1), (-1,0), (1,0)]:
                nr = dr + r
                nc = dc + c
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] != '#':
                    dfs(nr,nc,cur)

            if not cur.children:
                del node.children[char]

            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)

        return res




