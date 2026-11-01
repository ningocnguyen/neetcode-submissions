class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(haystack)
        b = len(needle)
        if a<b:
            return -1
        for i in range(a):
            if haystack[i:i+b] == needle:
                return i

        return -1