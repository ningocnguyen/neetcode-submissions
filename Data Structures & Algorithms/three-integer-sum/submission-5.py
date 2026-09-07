class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        s=sorted(nums)
        for i in range(len(nums)-1):
            if i>0 and s[i]==s[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                threeSum=s[i]+s[l]+s[r]
                if threeSum<0:
                    l+=1
                elif threeSum>0:
                    r-=1
                else:
                    res.append([s[i],s[l],s[r]])
                    l+=1
                    while l<r and s[l]==s[l-1]:
                        l+=1
        return res
                    
                
                
                