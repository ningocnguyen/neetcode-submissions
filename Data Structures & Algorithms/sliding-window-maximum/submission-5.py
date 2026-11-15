class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # double ended queue store indices
        res = []

        for i, n in enumerate(nums):
            while q and q[0] < i-k+1:
                q.popleft()
            while q and n > nums[q[-1]]:
                q.pop()
            q.append(i)
            if i>=k-1:
                res.append(nums[q[0]])
            
        return res
