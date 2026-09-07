class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        max_len=0
        char_set=set()

        while r<len(s):
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.add(s[r])
            curr_len=len(char_set)
            if max_len<curr_len:
                max_len=curr_len
            r+=1
        
        return max_len



