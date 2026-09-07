class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            key = tuple(sorted(word))
            if key not in res:
                res[key] = []
            res[key].append(word)

        return list(res.values())
        