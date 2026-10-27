class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] is the min cost of reaching ith floor
        # nth floor is top floor where n = len(cost)
        # dp[0] = 0 and dp[1] = 0 since can either start at floor 0 or 1
        # formula: dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-1])

        n = len(cost)
        # dp = [0] * (n+1)
        one = 0
        two = 0

        for i in range(2, n+1):
            min_cost = min(one + cost[i-1], two + cost[i-2])
            two = one
            one = min_cost

        return min_cost


