class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        held = -prices[0]
        sold = 0
        rest = 0

        for price in prices[1:]:
            prev_held = held
            prev_sold = sold
            prev_rest = rest

            held = max(prev_held, prev_rest - price)
            sold = prev_held + price
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)