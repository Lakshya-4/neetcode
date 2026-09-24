class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minB = prices[0]
        maxS = 0

        for i in prices:
            maxS = max(maxS, i - minB)
            minB = min(minB, i)
        return maxS