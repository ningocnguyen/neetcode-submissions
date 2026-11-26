class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]

        for i in range(len(word)):
            for w in strs[1:]:
                if i == len(w) or word[i] != w[i]:
                    return word[:i]

        return word