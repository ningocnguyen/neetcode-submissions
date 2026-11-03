class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        # sort nums
        # loop i: have pointers l=i+1, r=len(nums)-1
        # if nums[i] != nums[i-1: continue
        # if nums[l] == nums[l-1]: continue

        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = n-1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r-=1
                elif total < 0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        
        return res

