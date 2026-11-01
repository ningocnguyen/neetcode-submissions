class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_dict = dict(sorted(count.items(), key = lambda x: x[1], reverse=True))
        res = []
        
        for char, freq in sorted_dict.items():
            for i in range(freq):
                res.append(char)
        
        return ''.join(res)