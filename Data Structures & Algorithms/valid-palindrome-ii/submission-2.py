class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 2 pointer
        def helper_function(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1
            return True

        l=0
        r=len(s)-1
        while l<r:
            if s[l] != s[r]:
                return helper_function(l+1, r) or helper_function(l, r-1)
            l+=1
            r-=1
        
        return True