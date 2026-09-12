class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # held = max(held, rest - p)
        # sold = held + p: must have held a stock yesterday to sell today
        # rest = max(sold, rest) 

        held = -prices[0]
        sold = float('-inf') # invalid state
        rest = 0

        for price in prices:
            prev_held = held
            prev_sold = sold
            prev_rest = rest

            held = max(prev_rest - price, prev_held)
            sold = prev_held + price
            rest = max(prev_sold, prev_rest)

        return max(sold, rest)