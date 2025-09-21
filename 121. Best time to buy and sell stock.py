class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestprice = prices[0]
        maxprofit = 0
        for i in prices[1:]:
            if lowestprice > i:
                lowestprice = i
            elif i - lowestprice > maxprofit:
                maxprofit = i - lowestprice
        return maxprofit
