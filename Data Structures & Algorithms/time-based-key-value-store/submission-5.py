class TimeMap:

    def __init__(self):
        # {"alice": [[1, "happy"],[3, "sad"]]}
        # {key: [[timestamp, value],...]}
        self.timeDict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeDict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # binary search within values by list[0]: timestamp already sorted ascending
        if key not in self.timeDict:
            return ""
        values = self.timeDict[key]
        l, r = 0, len(values)-1
        res = ""
        while l<=r:
            mid = (l+r)//2
            if timestamp >= values[mid][0]:
                res = values[mid][1]
                l=mid+1
            else:
                r=mid-1
  
        return res


        # {'alice':[[1, 'happy'], [3, 'sad']]}



        
