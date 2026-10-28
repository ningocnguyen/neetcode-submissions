class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # use first string as benchmark
        # iterate thru each character in first string
            # iterate thru each latter string
                


        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if i == len(s) or s[i] != char:
                    return strs[0][:i]
        
        return strs[0]
