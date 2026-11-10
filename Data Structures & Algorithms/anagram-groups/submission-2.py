class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}

        for word in strs:
            key = tuple(sorted(word))
            if key not in wordDict:
                wordDict[key] = []
            wordDict[key].append(word)
        
        return list(wordDict.values())