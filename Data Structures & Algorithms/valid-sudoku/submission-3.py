class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # track existence of rows and cols and group
        # loop then if board[r][c] == '.' then skip
        rows = defaultdict(set)
        cols = defaultdict(set)
        groups = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                key = (r//3, c//3)
                
                if val in rows[r] or val in cols[c] or val in groups[key]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                groups[key].add((val))

        return True