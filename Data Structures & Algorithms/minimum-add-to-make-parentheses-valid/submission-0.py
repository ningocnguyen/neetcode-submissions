class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if s == "":
            return 0
        
        open_b = 0
        add = 0

        for c in s:
            if c == '(':
                open_b += 1
            else:
                if open_b > 0:
                    open_b -= 1
                else:
                    add += 1
        
        return add + open_b
