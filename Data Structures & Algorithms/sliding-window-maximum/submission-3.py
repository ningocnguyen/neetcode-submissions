class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for i, val in enumerate(nums):
            # monotonic decreasing queue
            while q and q[0] < i-k+1:
                q.popleft()
            
            while q and nums[q[-1]] < val:
                q.pop()
            
            q.append(i)
            
            if i>= k-1:
                res.append(nums[q[0]])

        return res