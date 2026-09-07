class Solution:
    def isValid(self, s: str) -> bool:
        # stack: last in first out
        parendict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for char in s:
            if char in parendict:
                if stack and stack[-1] == parendict[char]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)
        
        if not stack:
            return True
        return False

