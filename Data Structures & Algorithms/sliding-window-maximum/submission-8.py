class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonic non-decreasing queue: double ended queue
        # queue stores index
        # nums[q[0]] alwasy the highest number
        # keep window of k: q[0] < i-k+1

        res = []
        q = deque()
        for i,n in enumerate(nums):
            # n > values in q
            while q and n > nums[q[-1]]:
                q.pop()
            # keep window of size k
            while q and q[0] < i-k+1:
                q.popleft()

            q.append(i)
            if i-k+1>=0:
                res.append(nums[q[0]])

        return res
