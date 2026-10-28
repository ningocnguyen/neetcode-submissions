class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # use first string in strs as benchmark
        # iterate through each character in the string
        # if sth not match --> return strs[0][:i] immediately

        first = strs[0]

        for i in range(len(first)):
            for string in strs[1:]:
                if len(string) == i or string[i] != first[i]:
                    return first[:i]

        return first # for case that after iterating thru all elements in first but find no mismatch