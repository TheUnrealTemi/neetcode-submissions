class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]

        for i in range(len(prices)):
            cur_profit = prices[i] - buy_price
            max_profit = max(max_profit, cur_profit)
            if prices[i] < buy_price:
                buy_price = prices[i]

        return max_profit