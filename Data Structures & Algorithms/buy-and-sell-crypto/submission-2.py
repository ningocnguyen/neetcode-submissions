class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l=r
            max_profit = max(max_profit, prices[r] - prices[l])
        
        return max_profit

