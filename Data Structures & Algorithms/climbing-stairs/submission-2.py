class Solution:
    def climbStairs(self, n: int) -> int:
        # store 2 previous steps
        prev2 = 1
        prev1 = 2
        if n<=2:
            return n

        for _ in range(3, n+1):
            current = prev2 + prev1
            prev2 = prev1
            prev1 = current

        return current
