class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = 0  # Left pointer (buy)
        maxP = 0
        
        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r  # Found a lower buy price, update left pointer
                
        return maxP