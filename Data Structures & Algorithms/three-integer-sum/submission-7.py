class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        for i, n in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                threeSum = n + nums[l] + nums[r]
                if threeSum < 0:
                    l+=1
                elif threeSum > 0:
                    r-=1
                else:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return res                
