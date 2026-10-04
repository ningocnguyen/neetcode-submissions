class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        if m<n:
            return -1
        
        for i in range(m):
            if haystack[i:i+n] == needle:
                return i
        
        return -1