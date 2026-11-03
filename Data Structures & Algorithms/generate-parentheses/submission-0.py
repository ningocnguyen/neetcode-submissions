class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_b, closed_b = 0, 0
        res = []
        def backtrack(current_string, open_b, closed_b):
            if len(current_string) == 2*n:
                res.append(current_string)
                return
            if open_b < n:
                backtrack(current_string + "(", open_b+1, closed_b)
            if closed_b < open_b:
                backtrack(current_string + ")", open_b, closed_b + 1)

        backtrack("", 0, 0)
        return res