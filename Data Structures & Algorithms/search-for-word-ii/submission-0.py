class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        
class Solution(object):
    def findWords(self, board, words):
        res = []
        rows, cols = len(board), len(board[0])
        root = TrieNode()

        # build Trie from list of words
        for w in words:
            curr = root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = w

        # build DFS traversal
        def dfs(r,c,node):
            char = board[r][c]
            if char not in node.children:
                return
            cur_node = node.children[char]

            if cur_node.word:
                res.append(cur_node.word)
                cur_node.word = None
            
            board[r][c] = "#"

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr,nc,cur_node)

            board[r][c] = char

        # loop thru every cell in board
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)

        return res