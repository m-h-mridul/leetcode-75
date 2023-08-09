from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        profit=0
        prebuy=prices[0]
        for i in range(1,n):
            profit=max(profit,prices[i]-prebuy-fee)
            prebuy=min(prebuy,prices[i]-profit)
        return profit