class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minB = prices[0]
        maxS = 0

        for ii in prices:
            maxS = max(maxS, it - minB)
            minB = min(minB, it)
        return maxS