class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper_func(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return helper_func(left+1,right) or helper_func(left,right-1)
            left+=1
            right-=1
        
        return True
