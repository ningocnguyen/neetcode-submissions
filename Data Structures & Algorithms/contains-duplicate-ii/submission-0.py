class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numDict = {}

        for i, n in enumerate(nums):
            if n in numDict and i - numDict[n] <= k:
                    return True
            numDict[n] = i

        return False