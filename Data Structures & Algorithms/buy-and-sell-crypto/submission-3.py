class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # the largest profit for any date is the max of the 
        # remaining elements to the right

        prev = 0

        if len(prices) == 1:
            return prev

        for i in range(len(prices) - 1):
            curr = max(prices[i + 1:]) - prices[i]
            if curr > prev:
                prev = curr

        return prev


        