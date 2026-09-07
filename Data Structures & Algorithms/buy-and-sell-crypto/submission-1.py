class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        max_profit = 0

        for r in range(len(prices)):
            if prices[r] > prices[l]:
                diff = prices[r]-prices[l]
                if diff > max_profit:
                    max_profit = diff
            else:
                l = r
        
        return max_profit
