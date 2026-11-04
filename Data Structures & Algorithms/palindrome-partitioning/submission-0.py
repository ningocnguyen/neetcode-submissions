class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # keep track of start of substring
        # slice prefixes of length (0, len(s))
        # check if palindrome before recursing
        # if palindrome -> add to cur
        # call backtrack(end+1)
        cur, res = [], []
        
        def is_palindrome(n):
            return n == n[::-1]

        def backtrack(start):
            if start == len(s):
                res.append(cur[:])
                return
            
            for end in range(start, len(s)):
                sub = s[start:end+1]

                if is_palindrome(sub):
                    cur.append(sub)
                    backtrack(end+1) # explore remaining substring
                    cur.pop()

        backtrack(0)
        return res
                    