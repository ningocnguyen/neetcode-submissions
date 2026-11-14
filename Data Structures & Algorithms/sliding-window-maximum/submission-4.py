class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # double ended queue: monotonic decreasing queue storing index 
        # nums[q[0]] always the highest number
        # iterate through each n in nums
        # keep valid window of k each time: q[0]<i-k+1
        # every time move window, append the maximum element to res
        res = []
        q = deque()

        for i,n in enumerate(nums):
            while q and q[0] < i-k+1:
                q.popleft()
            while q and n > nums[q[-1]]:
                q.pop()
            
            q.append(i)
            if i>=k-1:
                res.append(nums[q[0]])

        return res
